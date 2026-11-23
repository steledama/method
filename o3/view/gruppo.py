"""Il sito di gruppo: i membri dell'istanza e la home che li elenca.

Un gruppo è un'istanza del metodo più i repo che coordina. L'istanza li
dichiara nel proprio `world.md`, in una sezione `## Membri` con una voce per
repo e il nome del checkout in grassetto:

    ## Membri

    - **[salute](https://github.com/...)** — Benessere e salute personale
    - **economia** — Gestione finanziaria

La build dell'istanza rende l'elenco in `view/gruppo.json` (`membri`): anche
l'elenco servito viene da un commit pulito. Un `world.md` senza la sezione
non è un'istanza di gruppo e non produce il file; una sezione vuota è il
caso minimo, l'istanza che serve sé sola.

`serve.py --gruppo BASE --istanza NOME` serve il sito: `BASE/<repo>` è la
cartella di pubblicazione di ciascun repo (`build.py --publish`), `/` la home
composta qui a ogni richiesta, `/<repo>/` la versione pubblicata di quel
repo. Solo libreria standard: gira anche sugli host Windows.
"""

from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass
from pathlib import Path

FILE = "gruppo.json"

_SECTION = re.compile(r"^## Membri[ \t]*\n(?P<body>.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
_ENTRY = re.compile(r"^- \*\*(?:\[(?P<link>[^\]]+)\]\([^)]*\)|(?P<plain>[^*]+))\*\*(?P<rest>.*)$")
NAME = re.compile(r"[a-z0-9][a-z0-9._-]*")

LABELS = {
    "it": {
        "title": "Gruppo",
        "instance": "istanza",
        "views": "Viste",
        "presentation": "Presentazione",
        "unpublished": "non ancora pubblicato",
        "intro": "I repo del gruppo, ciascuno con le sue viste.",
        "chat": "Chat di coordinamento",
        "chat_open": "Apri a tutta pagina",
        "chat_note": "Raggiungibile solo dal PC che la ospita: ascolta su loopback.",
    },
    "en": {
        "title": "Group",
        "instance": "instance",
        "views": "Views",
        "presentation": "Presentation",
        "unpublished": "not published yet",
        "intro": "The repos of the group, each with its views.",
        "chat": "Coordination chat",
        "chat_open": "Open full page",
        "chat_note": "Reachable only from the host PC: it listens on loopback.",
    },
}


@dataclass(frozen=True)
class Membro:
    nome: str
    descrizione: str


def membri(root: Path) -> list[Membro] | None:
    """I membri dichiarati nel `world.md` dell'istanza, o None se non è un'istanza."""
    world = root / "world.md"
    if not world.exists():
        return None
    match = _SECTION.search(world.read_text(encoding="utf-8"))
    if not match:
        return None
    # Il formatter manda a capo le voci lunghe: le righe rientrate continuano la voce.
    lines: list[str] = []
    for line in match.group("body").splitlines():
        if line.startswith("- "):
            lines.append(line.strip())
        elif lines and line.startswith((" ", "\t")) and line.strip():
            lines[-1] += " " + line.strip()
        else:
            lines.append("")
    found: list[Membro] = []
    for line in filter(None, lines):
        entry = _ENTRY.match(line)
        if not entry:
            raise SystemExit(f"world.md, «Membri»: voce senza nome in grassetto — «{line}»")
        name = (entry.group("link") or entry.group("plain")).strip()
        if not NAME.fullmatch(name):
            raise SystemExit(f"world.md, «Membri»: «{name}» non è il nome di un checkout")
        if any(member.nome == name for member in found):
            raise SystemExit(f"world.md, «Membri»: «{name}» compare due volte")
        description = entry.group("rest").strip().removeprefix("—").strip()
        description = description.split(" — ")[0].strip()
        found.append(Membro(name, description))
    return found


def manifest(members: list[Membro], lingua: str) -> str:
    """Il contenuto di `view/gruppo.json`."""
    data = {
        "lingua": lingua,
        "membri": [{"nome": m.nome, "descrizione": m.descrizione} for m in members],
    }
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


# --- Lato servitore ---------------------------------------------------------------


def release(base: Path, name: str) -> Path | None:
    """La versione pubblicata servita per `name`, o None se non ce n'è una valida."""
    try:
        current = (base / name / "current").read_text(encoding="utf-8").strip()
    except (FileNotFoundError, NotADirectoryError):
        return None
    folder = base / name / "releases" / current
    if current and (folder / "index.html").is_file():
        return folder
    return None


def leggi(base: Path, istanza: str) -> tuple[str, list[Membro]]:
    """Lingua e membri dall'elenco pubblicato dell'istanza; nessun elenco, nessun membro."""
    folder = release(base, istanza)
    path = folder / FILE if folder else None
    if not path or not path.is_file():
        return "it", []
    data = json.loads(path.read_text(encoding="utf-8"))
    members = [
        Membro(m["nome"], m.get("descrizione", ""))
        for m in data.get("membri", [])
        if NAME.fullmatch(m.get("nome", "")) and m.get("nome") != istanza
    ]
    lingua = data.get("lingua", "it")
    return (lingua if lingua in LABELS else "it"), members


def nomi(base: Path, istanza: str) -> set[str]:
    """I prefissi serviti: l'istanza e i suoi membri."""
    return {istanza} | {m.nome for m in leggi(base, istanza)[1]}


_TITLE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
_ACCENT = re.compile(r"--accent:\s*(#[0-9a-fA-F]{6})")


def _scheda(folder: Path | None) -> tuple[str | None, str | None, bool]:
    """Titolo, accento e presenza del deck di una versione pubblicata."""
    if folder is None:
        return None, None, False
    title = _TITLE.search((folder / "index.html").read_text(encoding="utf-8"))
    theme = folder / "assets" / "theme.css"
    accent = _ACCENT.search(theme.read_text(encoding="utf-8")) if theme.is_file() else None
    return (
        html.unescape(title.group(1).strip()) if title else None,
        accent.group(1) if accent else None,
        (folder / "presentation.html").is_file(),
    )


def _codice(text: str) -> str:
    """Il codice inline del Markdown, l'unico che le descrizioni portano."""
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", text)


def home(base: Path, istanza: str, chat: str | None = None) -> str:
    """La home del gruppo: l'istanza e i membri, ciascuno verso le sue viste.

    Con `chat`, l'indirizzo della chat del coordinatore (`o3/chat/serve.py`), la
    home la incorpora in un riquadro. La chat ascolta solo su loopback: il
    riquadro funziona dal browser del PC che la ospita, altrove resta vuoto.
    """
    lingua, members = leggi(base, istanza)
    labels = LABELS[lingua]
    cards = []
    for member, role in [(Membro(istanza, ""), labels["instance"])] + [(m, "") for m in members]:
        title, accent, deck = _scheda(release(base, member.nome))
        name = html.escape(member.nome)
        style = f' style="--accent: {accent}"' if accent else ""
        heading = html.escape(title) if title else f"<code>{name}</code>"
        tag = f' <span class="role">{html.escape(role)}</span>' if role else ""
        description = (
            f"<p>{_codice(html.escape(member.descrizione))}</p>" if member.descrizione else ""
        )
        if title is None:
            links = f'<p class="missing">{html.escape(labels["unpublished"])}</p>'
        else:
            links = f'<a href="{name}/">{html.escape(labels["views"])}</a>'
            if deck:
                links += f' · <a href="{name}/presentation.html">{html.escape(labels["presentation"])}</a>'
            links = f"<p>{links}</p>"
        cards.append(
            f'      <li class="member"{style}>\n'
            f"        <h2>{heading}{tag}</h2>\n"
            f"        {description}{links}\n"
            "      </li>"
        )
    group_title = f"{labels['title']} {istanza}"
    chat_section = ""
    if chat:
        address = html.escape(chat, quote=True)
        chat_section = (
            '      <section class="chat">\n'
            f"        <h2>{html.escape(labels['chat'])}"
            f' <a href="{address}" target="_blank" rel="noopener">{html.escape(labels["chat_open"])}</a></h2>\n'
            f'        <iframe src="{address}" title="{html.escape(labels["chat"], quote=True)}"></iframe>\n'
            f'        <p class="note">{html.escape(labels["chat_note"])}</p>\n'
            "      </section>\n"
        )
    return f"""<!doctype html>
<html lang="{lingua}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(group_title)}</title>
    <style>
      :root {{ color-scheme: light dark; --ink: #1f2937; --muted: #6b7280; --bg: #f9fafb; --card: #ffffff; --line: #e5e7eb; }}
      @media (prefers-color-scheme: dark) {{ :root {{ --ink: #e5e7eb; --muted: #9ca3af; --bg: #111827; --card: #1f2937; --line: #374151; }} }}
      body {{ margin: 0; padding: 2rem 1rem; background: var(--bg); color: var(--ink); font: 16px/1.5 system-ui, sans-serif; }}
      main {{ max-width: 46rem; margin: 0 auto; }}
      h1 {{ margin: 0 0 .25rem; }}
      .intro {{ color: var(--muted); margin: 0 0 1.5rem; }}
      ul {{ list-style: none; padding: 0; margin: 0; display: grid; gap: 1rem; }}
      .member {{ background: var(--card); border: 1px solid var(--line); border-left: 6px solid var(--accent, var(--muted)); border-radius: 8px; padding: 1rem 1.25rem; }}
      .member h2 {{ font-size: 1.15rem; margin: 0 0 .25rem; }}
      .member p {{ margin: .25rem 0; }}
      .role {{ font-size: .8rem; font-weight: normal; color: var(--muted); }}
      .missing {{ color: var(--muted); font-style: italic; }}
      a {{ color: var(--accent, inherit); font-weight: 600; }}
      .chat {{ margin: 0 0 1.5rem; }}
      .chat h2 {{ font-size: 1.15rem; margin: 0 0 .5rem; display: flex; justify-content: space-between; align-items: baseline; gap: 1rem; }}
      .chat h2 a {{ font-size: .85rem; }}
      .chat iframe {{ display: block; width: 100%; height: 75vh; border: 1px solid var(--line); border-radius: 8px; background: var(--card); }}
      .note {{ color: var(--muted); font-size: .85rem; margin: .25rem 0 0; }}
    </style>
  </head>
  <body>
    <main>
      <h1>{html.escape(group_title)}</h1>
      <p class="intro">{html.escape(labels["intro"])}</p>
{chat_section}      <ul>
{chr(10).join(cards)}
      </ul>
    </main>
  </body>
</html>
"""
