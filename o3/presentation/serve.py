"""Serve `presentation/` sulla LAN, su richiesta: si avvia, si usa, Ctrl-C.

Stesso comando in ogni repo: `python3 o3/presentation/serve.py`, su Windows
`py o3\\presentation\\serve.py`. Solo libreria standard, così gira anche sugli
host Windows. Pubblica la sola cartella `presentation/`, che è chiusa su se
stessa (`kb/presentation.md`, «Compartimento stagno»): niente dotfile e niente
elenchi di cartella. Non è un servizio permanente; la porta va ammessa dal
firewall dell'host solo verso la rete privata.
"""

from __future__ import annotations

import argparse
import socket
from functools import partial
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

PRESENTATION = Path(__file__).resolve().parents[2] / "presentation"
PORT = 8765


class PresentationHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        path = unquote(urlsplit(self.path).path)
        if any(part.startswith(".") for part in path.split("/") if part):
            self.send_error(HTTPStatus.NOT_FOUND)
            return None
        return super().send_head()

    def list_directory(self, path):
        self.send_error(HTTPStatus.NOT_FOUND)


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
    parser = argparse.ArgumentParser(description="Serve presentation/ sulla LAN, su richiesta")
    parser.add_argument("--port", type=int, default=PORT, help=f"porta TCP (default {PORT})")
    parser.add_argument(
        "--bind", default="0.0.0.0", help="indirizzo d'ascolto (default: tutte le interfacce)"
    )
    args = parser.parse_args()

    if not (PRESENTATION / "index.html").exists():
        raise SystemExit("serve: presentation/index.html assente, esegui prima build.py")

    handler = partial(PresentationHandler, directory=str(PRESENTATION))
    with ThreadingHTTPServer((args.bind, args.port), handler) as server:
        hosts = ["localhost"]
        if args.bind in {"0.0.0.0", ""}:
            hosts += lan_addresses() + [socket.gethostname()]
        elif args.bind not in {"127.0.0.1", "localhost"}:
            hosts = [args.bind]
        print(f"Presentazione da {PRESENTATION} — Ctrl-C per chiudere", flush=True)
        for host in hosts:
            print(f"  http://{host}:{args.port}/", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nChiuso.")


if __name__ == "__main__":
    main()
