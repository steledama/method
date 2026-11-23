"""La chat del coordinatore: sessioni ACP nei repo del gruppo, da browser.

    python3 method/../o3/chat/serve.py --istanza ~/nixos [--port 8100]

`--istanza` è il checkout dell'istanza del gruppo: i repo tra cui scegliere
sono l'istanza stessa e i membri della sezione `## Membri` del suo
`world.md` (`o3/view/gruppo.py`), ciascuno nel checkout accanto all'istanza
(`<genitore dell'istanza>/<nome>`). Un membro senza checkout non compare.

Chi raggiunge la chat fa agire un agente sui repo del gruppo con
l'abbonamento del custode: il server ascolta solo su loopback e lo rifiuta
altrimenti (task `chat-del-coordinatore`, «Accesso»). Contro una pagina di
un altro sito aperta nello stesso browser, ogni richiesta deve avere un
`Host` di loopback e le scritture un `Origin` uguale, o nessuno.

Rotte:

- `GET /`: la pagina; `GET /repo`: i repo e gli harness;
- `GET /sessioni`: le sessioni aperte; `POST /sessioni` `{repo, harness}`;
- `GET /sessioni/<id>/eventi?da=N`: gli eventi in Server-Sent Events;
- `POST /sessioni/<id>/prompt` `{testo}`, `/permesso` `{id, optionId}`,
  `/modo` `{modo}`, `/annulla`, `/chiudi`.

Il governo del repo non cambia: le modifiche le fa l'agente con i permessi
del repo e dell'harness, e i commit passano da `/commit`. La chat non tiene
memoria propria. Solo libreria standard.
"""

from __future__ import annotations

import argparse
import ipaddress
import json
import sys
import threading
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

QUI = Path(__file__).resolve().parent
sys.path.insert(0, str(QUI))
sys.path.insert(0, str(QUI.parent / "view"))

import acp
import gruppo

PORTA = 8100
PAGINA = QUI / "chat.html"
MASSIMO_CORPO = 1 << 20


def repo_del_gruppo(istanza: Path) -> dict[str, Path]:
    """Nome → checkout: l'istanza e i membri che hanno un checkout accanto."""
    trovati = {istanza.name: istanza}
    for membro in gruppo.membri(istanza) or []:
        cartella = istanza.parent / membro.nome
        if (cartella / ".git").exists():
            trovati[membro.nome] = cartella
    return trovati


def loopback(indirizzo: str) -> bool:
    if indirizzo == "localhost":
        return True
    try:
        return ipaddress.ip_address(indirizzo).is_loopback
    except ValueError:
        return False


class Chat(BaseHTTPRequestHandler):
    istanza: Path
    sessioni: dict[str, acp.Sessione]
    blocco: threading.Lock
    comandi: dict[str, list[str]] | None = None  # i test sostituiscono gli adattatori

    protocol_version = "HTTP/1.1"

    def log_message(self, formato, *args):  # le richieste SSE sarebbero rumore
        pass

    # --- presidi -----------------------------------------------------------------

    def ammessa(self, scrittura: bool) -> bool:
        host = (self.headers.get("Host") or "").rsplit(":", 1)[0].strip("[]")
        if not loopback(host):
            self.rispondi(HTTPStatus.FORBIDDEN, {"errore": "Host non di loopback"})
            return False
        origine = self.headers.get("Origin")
        if scrittura and origine is not None:
            atteso = f"http://{self.headers.get('Host')}"
            if origine != atteso:
                self.rispondi(HTTPStatus.FORBIDDEN, {"errore": "Origin estranea"})
                return False
        return True

    def corpo(self) -> dict:
        lunghezza = int(self.headers.get("Content-Length") or 0)
        if lunghezza > MASSIMO_CORPO:
            raise ValueError("corpo troppo grande")
        grezzo = self.rfile.read(lunghezza)
        try:
            dati = json.loads(grezzo or b"{}")
        except json.JSONDecodeError as errore:
            raise ValueError(f"JSON non valido: {errore}") from errore
        if not isinstance(dati, dict):
            raise ValueError("atteso un oggetto JSON")
        return dati

    def rispondi(self, stato: HTTPStatus, dati, tipo: str = "application/json; charset=utf-8"):
        corpo = (
            dati
            if isinstance(dati, bytes)
            else json.dumps(dati, ensure_ascii=False).encode("utf-8")
        )
        self.send_response(stato)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(corpo)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(corpo)

    # --- GET --------------------------------------------------------------------

    def do_GET(self):
        if not self.ammessa(scrittura=False):
            return
        parti = urlsplit(self.path)
        path = parti.path
        if path == "/":
            return self.rispondi(HTTPStatus.OK, PAGINA.read_bytes(), "text/html; charset=utf-8")
        if path == "/repo":
            return self.rispondi(
                HTTPStatus.OK,
                {
                    "istanza": self.istanza.name,
                    "repo": list(repo_del_gruppo(self.istanza)),
                    "harness": list(acp.ADATTATORI),
                },
            )
        if path == "/sessioni":
            return self.rispondi(
                HTTPStatus.OK,
                [
                    {"id": s.id, "repo": s.repo, "harness": s.harness, "chiusa": s.chiusa}
                    for s in self.sessioni.values()
                ],
            )
        pezzi = path.strip("/").split("/")
        if len(pezzi) == 3 and pezzi[0] == "sessioni" and pezzi[2] == "eventi":
            sessione = self.sessioni.get(pezzi[1])
            if sessione is None:
                return self.rispondi(HTTPStatus.NOT_FOUND, {"errore": "sessione sconosciuta"})
            da = int((parse_qs(parti.query).get("da") or ["0"])[0])
            return self.flusso(sessione, da)
        self.rispondi(HTTPStatus.NOT_FOUND, {"errore": "rotta sconosciuta"})

    def flusso(self, sessione: acp.Sessione, da: int):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Connection", "close")
        self.end_headers()
        self.close_connection = True
        try:
            while True:
                nuovi = sessione.attendi(da, timeout=15)
                if not nuovi:
                    if sessione.chiusa:
                        return
                    self.wfile.write(b": viva\n\n")
                for evento in nuovi:
                    dati = json.dumps(evento, ensure_ascii=False)
                    self.wfile.write(f"id: {evento['n']}\ndata: {dati}\n\n".encode())
                    da = evento["n"] + 1
                self.wfile.flush()
                if sessione.chiusa and da >= len(sessione.eventi):
                    return
        except (BrokenPipeError, ConnectionResetError):
            return

    # --- POST -------------------------------------------------------------------

    def do_POST(self):
        # Il corpo si legge prima di ogni rifiuto: lasciato nel socket, sarebbe
        # letto come la richiesta seguente della stessa connessione.
        try:
            dati = self.corpo()
        except ValueError as errore:
            self.close_connection = True
            return self.rispondi(HTTPStatus.BAD_REQUEST, {"errore": str(errore)})
        if not self.ammessa(scrittura=True):
            return
        pezzi = urlsplit(self.path).path.strip("/").split("/")
        if pezzi == ["sessioni"]:
            return self.nuova(dati)
        if len(pezzi) != 3 or pezzi[0] != "sessioni":
            return self.rispondi(HTTPStatus.NOT_FOUND, {"errore": "rotta sconosciuta"})
        sessione = self.sessioni.get(pezzi[1])
        if sessione is None:
            return self.rispondi(HTTPStatus.NOT_FOUND, {"errore": "sessione sconosciuta"})
        if sessione.chiusa and pezzi[2] != "chiudi":
            return self.rispondi(HTTPStatus.CONFLICT, {"errore": "sessione chiusa"})
        try:
            match pezzi[2]:
                case "prompt":
                    testo = str(dati.get("testo", "")).strip()
                    if not testo:
                        return self.rispondi(HTTPStatus.BAD_REQUEST, {"errore": "prompt vuoto"})
                    sessione.prompt(testo)
                case "permesso":
                    opzione = dati.get("optionId")
                    sessione.rispondi(
                        str(dati.get("id")), None if opzione is None else str(opzione)
                    )
                case "modo":
                    sessione.modo(str(dati.get("modo")))
                case "annulla":
                    sessione.annulla()
                case "chiudi":
                    sessione.chiudi()
                case _:
                    return self.rispondi(HTTPStatus.NOT_FOUND, {"errore": "atto sconosciuto"})
        except acp.Occupata:
            return self.rispondi(HTTPStatus.CONFLICT, {"errore": "un turno è già in corso"})
        except KeyError:
            return self.rispondi(
                HTTPStatus.NOT_FOUND, {"errore": "permesso sconosciuto o già chiuso"}
            )
        except ValueError:
            return self.rispondi(HTTPStatus.BAD_REQUEST, {"errore": "opzione non offerta"})
        except (RuntimeError, TimeoutError, OSError) as errore:
            return self.rispondi(HTTPStatus.BAD_GATEWAY, {"errore": str(errore)})
        self.rispondi(HTTPStatus.OK, {"ok": True})

    def nuova(self, dati: dict):
        repo, harness = str(dati.get("repo", "")), str(dati.get("harness", ""))
        cartelle = repo_del_gruppo(self.istanza)
        if repo not in cartelle:
            return self.rispondi(
                HTTPStatus.BAD_REQUEST, {"errore": f"«{repo}» non è un repo del gruppo"}
            )
        if harness not in acp.ADATTATORI:
            return self.rispondi(
                HTTPStatus.BAD_REQUEST, {"errore": f"harness «{harness}» sconosciuto"}
            )
        comando = (self.comandi or {}).get(harness)
        try:
            sessione = acp.Sessione(repo, cartelle[repo], harness, comando)
        except OSError as errore:
            return self.rispondi(
                HTTPStatus.BAD_GATEWAY, {"errore": f"adattatore non avviato: {errore}"}
            )
        with self.blocco:
            self.sessioni[sessione.id] = sessione
        try:
            sessione.apri()
        except (RuntimeError, TimeoutError, OSError) as errore:
            sessione.chiudi()
            return self.rispondi(HTTPStatus.BAD_GATEWAY, {"errore": str(errore), "id": sessione.id})
        self.rispondi(HTTPStatus.OK, {"id": sessione.id})


def main() -> None:
    parser = argparse.ArgumentParser(description="Chat del coordinatore, solo su loopback")
    parser.add_argument(
        "--istanza", type=Path, required=True, help="checkout dell'istanza del gruppo"
    )
    parser.add_argument("--port", type=int, default=PORTA, help=f"porta TCP (default {PORTA})")
    parser.add_argument(
        "--bind", default="127.0.0.1", help="indirizzo di loopback (default 127.0.0.1)"
    )
    args = parser.parse_args()
    if not loopback(args.bind):
        parser.error("la chat ascolta solo su loopback finché non ha un'autenticazione")
    istanza = args.istanza.expanduser().resolve()
    if gruppo.membri(istanza) is None:
        parser.error(f"{istanza}: world.md senza «## Membri», non è un'istanza di gruppo")
    gestore = type(
        "Gestore", (Chat,), {"istanza": istanza, "sessioni": {}, "blocco": threading.Lock()}
    )
    with ThreadingHTTPServer((args.bind, args.port), gestore) as server:
        server.daemon_threads = True
        print(
            f"Chat del gruppo {istanza.name}: http://{args.bind}:{args.port}/ — Ctrl-C per chiudere",
            flush=True,
        )
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            for sessione in list(gestore.sessioni.values()):
                sessione.chiudi()
            print("\nChiuso.")


if __name__ == "__main__":
    main()
