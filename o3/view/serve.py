"""Serve `view/` sulle reti private: lancio manuale o servizio permanente.

Stesso comando in ogni repo: `python3 o3/view/serve.py`, su Windows
`py o3\\view\\serve.py`, porta 8000, Ctrl-C per chiudere: serve l'anteprima
generata in `view/` dal working tree. Il servizio permanente dell'host
privilegiato lancia questo stesso script del checkout con `--port` e
`--publish-root` (`kb/view-publishing.md`, «Pubblicazione»). Solo libreria standard, così gira
anche sugli host Windows. Pubblica la sola cartella servita, che è chiusa
su se stessa (`kb/view.md`, «Compartimento stagno»): niente
dotfile e niente elenchi di cartella. La porta va ammessa dal firewall
dell'host solo verso le reti private; il server non lo tocca.

Con `--publish-root DIR` serve invece la versione pubblicata da
`build.py --publish DIR`: il puntatore `current` si rilegge a ogni
richiesta, così uno scambio di versione non chiede riavvii e una richiesta
già iniziata finisce sulla sua versione. `/_stato` rende `status.json`:
revisione servita, ultimo tentativo ed eventuale errore. Senza alcuna
versione valida il server non parte, dice perché ed esce con il codice 3,
distinto dagli altri errori; `--check` fa solo questo controllo (0 o 3), per
esempio come `ExecCondition` di un servizio.

Con `--gruppo BASE --istanza NOME` serve il sito di un gruppo (`gruppo.py`):
`BASE/<repo>` è la cartella di pubblicazione di ciascun repo, `/` la home del
gruppo, `/<repo>/` la versione pubblicata di quel repo con il suo `/_stato`.
L'elenco dei membri si rilegge a ogni richiesta dalla versione pubblicata
dell'istanza; senza una versione valida dell'istanza il server non parte,
come con `--publish-root`.
"""

from __future__ import annotations

import argparse
import io
import socket
import sys
from functools import partial
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

# Lanciato con `runpy` (il servizio di `danea-auto` su Windows) la cartella
# dello script non è in `sys.path`.
sys.path.insert(0, str(Path(__file__).resolve().parent))

import radice

VIEW = radice.attiva() / "view"

import gruppo

PORT = 8000
# Uscita per «nessuna versione valida»: un servizio la distingue da un crash.
NO_VALID_VERSION = 3


class ViewHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        path = unquote(urlsplit(self.path).path)
        if any(part.startswith(".") for part in path.split("/") if part):
            self.send_error(HTTPStatus.NOT_FOUND)
            return None
        return super().send_head()

    def list_directory(self, path):
        self.send_error(HTTPStatus.NOT_FOUND)


class PublishedHandler(ViewHandler):
    """Serve la versione nominata dal puntatore al momento della richiesta."""

    root: Path

    def __init__(self, *args, **kwargs):
        name = (self.root / "current").read_text(encoding="utf-8").strip()
        super().__init__(*args, directory=str(self.root / "releases" / name), **kwargs)

    def send_head(self):
        if urlsplit(self.path).path == "/_stato":
            try:
                data = (self.root / "status.json").read_bytes()
            except FileNotFoundError:
                self.send_error(HTTPStatus.NOT_FOUND)
                return None
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            return io.BytesIO(data)
        return super().send_head()


class GroupHandler(ViewHandler):
    """Il sito di gruppo: la home a `/`, ogni repo sotto il proprio nome."""

    base: Path
    istanza: str
    chat: str | None = None

    def send_head(self):
        parts = urlsplit(self.path)
        path = unquote(parts.path)
        if path in {"/", "/index.html"}:
            return self.send_bytes(
                "text/html; charset=utf-8",
                gruppo.home(self.base, self.istanza, self.chat).encode("utf-8"),
            )
        name, slash, rest = path.lstrip("/").partition("/")
        if name not in gruppo.nomi(self.base, self.istanza):
            self.send_error(HTTPStatus.NOT_FOUND)
            return None
        if not slash:
            # Senza la barra i path relativi della vista uscirebbero dal prefisso.
            self.send_response(HTTPStatus.MOVED_PERMANENTLY)
            self.send_header("Location", f"/{name}/" + (f"?{parts.query}" if parts.query else ""))
            self.send_header("Content-Length", "0")
            self.end_headers()
            return None
        if rest == "_stato":
            try:
                data = (self.base / name / "status.json").read_bytes()
            except FileNotFoundError:
                self.send_error(HTTPStatus.NOT_FOUND)
                return None
            return self.send_bytes("application/json; charset=utf-8", data)
        folder = gruppo.release(self.base, name)
        if folder is None:
            self.send_error(HTTPStatus.NOT_FOUND)
            return None
        target = folder / rest
        if rest and not rest.endswith("/") and target.is_dir():
            self.send_response(HTTPStatus.MOVED_PERMANENTLY)
            self.send_header("Location", f"/{name}/{rest}/")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return None
        self.directory = str(folder)
        self.path = "/" + rest + (f"?{parts.query}" if parts.query else "")
        return super().send_head()

    def send_bytes(self, content_type: str, data: bytes):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        return io.BytesIO(data)


def served_folder(root: Path) -> Path:
    """La versione pubblicata, o l'uscita con la diagnosi se non ce n'è una valida."""
    try:
        name = (root / "current").read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        name = ""
    folder = root / "releases" / name
    if name and (folder / "index.html").exists():
        return folder
    status = root / "status.json"
    detail = (
        status.read_text(encoding="utf-8") if status.exists() else "nessun tentativo registrato"
    )
    print(
        f"serve: nessuna versione valida in {root}; esegui build.py --publish {root}\n{detail}",
        file=sys.stderr,
    )
    raise SystemExit(NO_VALID_VERSION)


def lan_addresses() -> list[str]:
    """Gli indirizzi con cui gli altri PC raggiungono questo host."""
    addresses: set[str] = set()
    try:
        # Nessun pacchetto parte: connect su UDP sceglie solo l'interfaccia d'uscita.
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as probe:
            probe.connect(("192.0.2.1", 9))
            addresses.add(probe.getsockname()[0])
    except OSError:
        pass
    try:
        for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET):
            addresses.add(info[4][0])
    except OSError:
        pass
    return sorted(address for address in addresses if not address.startswith("127."))


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve view/ sulle reti private")
    parser.add_argument(
        "--root", type=Path, help="repo da servire, se non è quello di questo script (radice.py)"
    )
    parser.add_argument("--port", type=int, default=PORT, help=f"porta TCP (default {PORT})")
    parser.add_argument(
        "--bind", default="0.0.0.0", help="indirizzo d'ascolto (default: tutte le interfacce)"
    )
    parser.add_argument(
        "--publish-root", type=Path, help="serve la versione pubblicata da build.py --publish"
    )
    parser.add_argument(
        "--gruppo",
        type=Path,
        help="serve il sito di gruppo: cartella con una pubblicazione per repo (gruppo.py)",
    )
    parser.add_argument("--istanza", help="con --gruppo: il repo istanza che dichiara i membri")
    parser.add_argument(
        "--chat",
        help="con --gruppo: indirizzo della chat del coordinatore da incorporare nella home",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help=f"con --publish-root: esce con 0 se c'è una versione valida, {NO_VALID_VERSION} se no",
    )
    args = parser.parse_args()

    if bool(args.gruppo) != bool(args.istanza):
        parser.error("--gruppo e --istanza vanno insieme")
    if args.chat and not args.gruppo:
        parser.error("--chat richiede --gruppo")
    if args.gruppo and args.publish_root:
        parser.error("--gruppo e --publish-root sono alternativi")
    if args.check and not (args.publish_root or args.gruppo):
        parser.error("--check richiede --publish-root o --gruppo")
    if args.gruppo:
        base = args.gruppo.resolve()
        folder = served_folder(base / args.istanza)
        if args.check:
            print(f"serve: versione valida dell'istanza {folder.name}")
            return
        folder = base
        handler = type(
            "Handler",
            (GroupHandler,),
            {"base": base, "istanza": args.istanza, "chat": args.chat},
        )
    elif args.publish_root:
        root = args.publish_root.resolve()
        folder = served_folder(root)
        if args.check:
            print(f"serve: versione valida {folder.name}")
            return
        handler = type("Handler", (PublishedHandler,), {"root": root})
    else:
        folder = VIEW
        if not (VIEW / "index.html").exists():
            raise SystemExit("serve: view/index.html assente, esegui prima build.py")
        handler = partial(ViewHandler, directory=str(VIEW))
    with ThreadingHTTPServer((args.bind, args.port), handler) as server:
        hosts = ["localhost"]
        if args.bind in {"0.0.0.0", ""}:
            hosts += lan_addresses() + [socket.gethostname()]
        elif args.bind not in {"127.0.0.1", "localhost"}:
            hosts = [args.bind]
        print(f"Viste da {folder} — Ctrl-C per chiudere", flush=True)
        for host in hosts:
            print(f"  http://{host}:{args.port}/", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nChiuso.")


if __name__ == "__main__":
    main()
