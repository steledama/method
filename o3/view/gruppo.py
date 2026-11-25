"""Il sito di gruppo: i membri dell'istanza e la home che li elenca.

Un gruppo è un'istanza del metodo più i repo che coordina. L'istanza li
dichiara nel proprio `world.md`, in una sezione `## Membri` con una voce per
repo e il nome del checkout in grassetto:

    ## Membri

    Titolo: Casa
    Introduzione: Gli artefatti e i repository di casa.

    - **[salute](https://github.com/...)** — Benessere e salute personale
    - **economia** — Gestione finanziaria
      - indirizzo: http://10.0.0.4:8001/
    - **gestionale** — Danea Easyfatt
      - fuori metodo
      - descrizione: Tre o quattro righe su cosa fa, mandate a capo
        liberamente.

La riga `Titolo:` dà il nome del sito (senza, «Gruppo <istanza>»),
`Introduzione:` la frase sotto il titolo. Il link sul nome in grassetto è
l'URL del repo, che il riquadro offre come «Repository». La lingua delle
etichette è `LINGUA` del `project.py` dell'istanza. Il testo
del riquadro di un membro del metodo è l'incipit del suo README, che la sua
vista pubblica (`build_system_image.readme_incipit`). Sotto ogni voce, campi
facoltativi in un elenco annidato: `descrizione` (il testo dei membri fuori
metodo, e il ripiego di chi non pubblica ancora), `indirizzo` (la vista è servita da
un altro host: il riquadro la collega lì e ne legge `/_stato`), `fuori
metodo` (un membro del gruppo che non adotta il metodo: riquadro statico,
senza link né versione). Gli indirizzi dei servizi interni sono IP, non
nomi host: la rete mista Windows/Linux non li risolve tutti.

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
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

FILE = "gruppo.json"

_SECTION = re.compile(r"^## Membri[ \t]*\n(?P<body>.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
_ENTRY = re.compile(
    r"^- \*\*(?:\[(?P<link>[^\]]+)\]\((?P<url>[^)]*)\)|(?P<plain>[^*]+))\*\*(?P<rest>.*)$"
)
# Righe della sezione che valgono per tutto il sito, fuori dalle voci.
_INTESTAZIONE = re.compile(r"^(?P<key>Titolo|Introduzione):[ \t]*(?P<value>\S.*?)[ \t]*$")
_URL = re.compile(r"https?://\S+")
_FIELD = re.compile(r"^(?P<key>[a-z][a-z ]*?)(?::[ \t]*(?P<value>.*))?$")
FIELDS = {"descrizione", "indirizzo", "fuori metodo"}
# Una vista remota che non risponde non deve fermare la home.
TIMEOUT = 2.0
NAME = re.compile(r"[a-z0-9][a-z0-9._-]*")

LABELS = {
    "it": {
        "title": "Gruppo",
        "instance": "coordinatore del gruppo",
        "outside": "fuori metodo",
        "canon": "method",
        "commit": "commit pubblicato",
        "repo": "Repository",
        "pending": "richiesto {sha}, non ancora pubblicato",
        "failed": "ultima pubblicazione fallita",
        "unreachable": "stato non raggiungibile",
        "views": "Artefatto",
        "presentation": "Presentazione",
        "unpublished": "non ancora pubblicato",
        "intro": "Gli artefatti e i repository del gruppo.",
        "chat": "Chat di coordinamento",
        "chat_open": "Apri a tutta pagina",
        "chat_note": "Raggiungibile solo dal PC che la ospita: ascolta su loopback.",
    },
    "en": {
        "title": "Group",
        "instance": "group coordinator",
        "outside": "outside the method",
        "canon": "method",
        "commit": "published commit",
        "repo": "Repository",
        "pending": "requested {sha}, not published yet",
        "failed": "last publication failed",
        "unreachable": "status unreachable",
        "views": "Artifact",
        "presentation": "Presentation",
        "unpublished": "not published yet",
        "intro": "The artifacts and repositories of the group.",
        "chat": "Coordination chat",
        "chat_open": "Open full page",
        "chat_note": "Reachable only from the host PC: it listens on loopback.",
    },
}


@dataclass(frozen=True)
class Membro:
    nome: str
    descrizione: str
    testo: str = ""
    indirizzo: str | None = None
    fuori: bool = False
    repo: str | None = None

    @property
    def locale(self) -> bool:
        """Servito da questo sito, sotto `/<nome>/`."""
        return not self.fuori and self.indirizzo is None

    def dati(self) -> dict:
        data: dict = {"nome": self.nome, "descrizione": self.descrizione}
        if self.testo:
            data["testo"] = self.testo
        if self.indirizzo:
            data["indirizzo"] = self.indirizzo
        if self.fuori:
            data["fuori_metodo"] = True
        if self.repo:
            data["repo"] = self.repo
        return data


@dataclass(frozen=True)
class Gruppo:
    titolo: str | None
    membri: list[Membro]
    intro: str | None = None


def _errore(text: str) -> SystemExit:
    return SystemExit(f"world.md, «Membri»: {text}")


def gruppo(root: Path) -> Gruppo | None:
    """Titolo e membri dichiarati nel `world.md` dell'istanza, o None se non è un'istanza."""
    world = root / "world.md"
    if not world.exists():
        return None
    match = _SECTION.search(world.read_text(encoding="utf-8"))
    if not match:
        return None
    titolo = intro = None
    # Voci: [riga della voce, {campo: valore}]. Il formatter manda a capo le
    # righe lunghe: quelle rientrate continuano la voce o il campo aperto.
    entries: list[tuple[list[str], dict[str, str]]] = []
    current: tuple[list[str], dict[str, str]] | None = None
    field: str | None = None
    for line in match.group("body").splitlines():
        stripped = line.strip()
        if line.startswith("- "):
            current = ([stripped], {})
            entries.append(current)
            field = None
        elif stripped and line.startswith((" ", "\t")):
            if current is None:
                raise _errore(f"riga rientrata fuori da una voce — «{stripped}»")
            head, fields = current
            if stripped.startswith("- "):
                parsed = _FIELD.match(stripped[2:].strip())
                key = parsed.group("key") if parsed else None
                if key not in FIELDS:
                    raise _errore(f"campo sconosciuto — «{stripped}»")
                if key in fields:
                    raise _errore(f"campo «{key}» ripetuto — «{head[0]}»")
                fields[key] = (parsed.group("value") or "").strip()
                field = key
            elif field:
                fields[field] = f"{fields[field]} {stripped}".strip()
            else:
                head[0] += " " + stripped
        else:
            # Una riga vuota o la prosa della sezione chiudono la voce.
            current, field = None, None
            header = _INTESTAZIONE.match(stripped)
            if header and header.group("key") == "Titolo":
                titolo = header.group("value")
            elif header:
                intro = header.group("value")
    found: list[Membro] = []
    for (line,), fields in entries:
        entry = _ENTRY.match(line)
        if not entry:
            raise _errore(f"voce senza nome in grassetto — «{line}»")
        name = (entry.group("link") or entry.group("plain")).strip()
        if not NAME.fullmatch(name):
            raise _errore(f"«{name}» non è il nome di un checkout")
        if any(member.nome == name for member in found):
            raise _errore(f"«{name}» compare due volte")
        description = entry.group("rest").strip().removeprefix("—").strip()
        description = description.split(" — ")[0].strip()
        fuori = "fuori metodo" in fields
        if fuori and fields["fuori metodo"]:
            raise _errore(f"«fuori metodo» non prende un valore — «{name}»")
        indirizzo = fields.get("indirizzo")
        if indirizzo is not None and not re.fullmatch(r"https?://\S+", indirizzo):
            raise _errore(f"«{name}»: l'indirizzo non è un URL http — «{indirizzo}»")
        if fuori and indirizzo:
            raise _errore(f"«{name}»: un membro fuori metodo non ha un indirizzo di vista")
        if "descrizione" in fields and not fields["descrizione"]:
            raise _errore(f"«{name}»: descrizione vuota")
        # Il link sul nome è l'URL del repo; uno che non è http non si offre.
        url = (entry.group("url") or "").strip()
        url = url if _URL.fullmatch(url) else ""
        found.append(
            Membro(name, description, fields.get("descrizione", ""), indirizzo, fuori, url or None)
        )
    return Gruppo(titolo, found, intro)


def membri(root: Path) -> list[Membro] | None:
    """I membri dichiarati nel `world.md` dell'istanza, o None se non è un'istanza."""
    found = gruppo(root)
    return None if found is None else found.membri


def manifest(group: Gruppo | list[Membro], lingua: str) -> str:
    """Il contenuto di `view/gruppo.json`."""
    if isinstance(group, list):
        group = Gruppo(None, group)
    data: dict = {"lingua": lingua}
    if group.titolo:
        data["titolo"] = group.titolo
    if group.intro:
        data["introduzione"] = group.intro
    data["membri"] = [m.dati() for m in group.membri]
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


def leggi(base: Path, istanza: str) -> tuple[str, Gruppo]:
    """Lingua, titolo e membri dall'elenco pubblicato dell'istanza; nessun elenco, nessun membro."""
    folder = release(base, istanza)
    path = folder / FILE if folder else None
    if not path or not path.is_file():
        return "it", Gruppo(None, [])
    data = json.loads(path.read_text(encoding="utf-8"))
    members = []
    for m in data.get("membri", []):
        if not NAME.fullmatch(m.get("nome", "")):
            continue
        indirizzo = m.get("indirizzo")
        if indirizzo and not _URL.fullmatch(indirizzo):
            indirizzo = None
        repo = m.get("repo")
        if repo and not _URL.fullmatch(repo):
            repo = None
        members.append(
            Membro(
                m["nome"],
                m.get("descrizione", ""),
                m.get("testo", ""),
                indirizzo,
                bool(m.get("fuori_metodo")),
                repo,
            )
        )
    lingua = data.get("lingua", "it")
    titolo = data.get("titolo") or None
    intro = data.get("introduzione") or None
    return (lingua if lingua in LABELS else "it"), Gruppo(titolo, members, intro)


def nomi(base: Path, istanza: str) -> set[str]:
    """I prefissi serviti: l'istanza e i membri serviti da questo sito."""
    return {istanza} | {m.nome for m in leggi(base, istanza)[1].membri if m.locale}


_TITLE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
_ACCENT = re.compile(r"--accent:\s*(#[0-9a-fA-F]{6})")
_INCIPIT = re.compile(r'<meta\s+name="description"\s+content="([^"]*)"')


@dataclass(frozen=True)
class Scheda:
    """Ciò che la home mostra della versione servita di un membro."""

    titolo: str | None = None
    accento: str | None = None
    incipit: str | None = None
    deck: bool = False
    stato: dict | None = None
    raggiunto: bool = True


def _da_testi(index: str | None, theme: str | None) -> tuple[str | None, str | None, str | None]:
    """Titolo, accento e incipit del README, come la vista li pubblica."""
    title = _TITLE.search(index) if index else None
    accent = _ACCENT.search(theme) if theme else None
    incipit = _INCIPIT.search(index) if index else None
    return (
        html.unescape(title.group(1).strip()) if title else None,
        accent.group(1) if accent else None,
        html.unescape(incipit.group(1)).strip() or None if incipit else None,
    )


def _scheda(base: Path, name: str) -> Scheda:
    """Titolo, accento, deck e stato di pubblicazione di un membro servito qui."""
    try:
        stato = json.loads((base / name / "status.json").read_text(encoding="utf-8"))
    except (FileNotFoundError, NotADirectoryError, json.JSONDecodeError):
        stato = None
    folder = release(base, name)
    if folder is None:
        return Scheda(stato=stato)
    theme = folder / "assets" / "theme.css"
    title, accent, incipit = _da_testi(
        (folder / "index.html").read_text(encoding="utf-8"),
        theme.read_text(encoding="utf-8") if theme.is_file() else None,
    )
    return Scheda(title, accent, incipit, (folder / "presentation.html").is_file(), stato)


def _get(url: str, method: str = "GET") -> str | None:
    try:
        request = urllib.request.Request(url, method=method)
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return response.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, OSError, ValueError):
        return None


def _remota(indirizzo: str) -> Scheda:
    """La scheda di un membro servito da un altro host, letta dal suo sito."""
    root = indirizzo if indirizzo.endswith("/") else indirizzo + "/"
    index = _get(root)
    if index is None:
        return Scheda(raggiunto=False)
    raw = _get(root + "_stato")
    try:
        stato = json.loads(raw) if raw else None
    except json.JSONDecodeError:
        stato = None
    title, accent, incipit = _da_testi(index, _get(root + "assets/theme.css"))
    deck = _get(root + "presentation.html", "HEAD") is not None
    return Scheda(title, accent, incipit, deck, stato if isinstance(stato, dict) else None)


def _breve(sha: object) -> str | None:
    return sha[:7] if isinstance(sha, str) and sha else None


def _versione(scheda: Scheda, labels: dict[str, str]) -> str:
    """Marker del canone, commit servito e data; in evidenza se non è il richiesto."""
    if not scheda.raggiunto:
        return f'<p class="version warn">{html.escape(labels["unreachable"])}</p>'
    stato = scheda.stato or {}
    parts = []
    marker = stato.get("served_marker")
    if isinstance(marker, dict):
        version = marker.get("method_version") or _breve(marker.get("method_commit"))
        if version:
            parts.append(f"{html.escape(labels['canon'])} <code>{html.escape(str(version))}</code>")
    served = _breve(stato.get("served_commit"))
    if served:
        text = f"{html.escape(labels['commit'])} <code>{html.escape(served)}</code>"
        date = stato.get("served_date")
        if isinstance(date, str) and date:
            text += f" · {html.escape(date[:10])}"
        parts.append(text)
    line = f'<p class="version">{" · ".join(parts)}</p>' if parts else ""
    warnings = []
    requested = stato.get("requested")
    if isinstance(requested, str) and requested and requested != stato.get("served_commit"):
        warnings.append(labels["pending"].format(sha=_breve(requested)))
    if stato.get("ok") is False:
        warnings.append(labels["failed"])
    if warnings:
        line += f'<p class="version warn">{html.escape(" · ".join(warnings))}</p>'
    return line


def _codice(text: str) -> str:
    """Il codice inline del Markdown, l'unico che le descrizioni portano."""
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", text)


def home(base: Path, istanza: str, chat: str | None = None) -> str:
    """La home del gruppo: l'istanza e i membri, ciascuno verso le sue viste.

    Con `chat`, l'indirizzo della chat del coordinatore (`o3/chat/serve.py`), la
    home la incorpora in un riquadro. La chat ascolta solo su loopback: il
    riquadro funziona dal browser del PC che la ospita, altrove resta vuoto.
    """
    lingua, group = leggi(base, istanza)
    labels = LABELS[lingua]
    cards = []
    # L'istanza può dichiarare anche sé stessa, per la descrizione: resta in
    # testa e servita qui, qualunque campo porti la voce.
    own = next((m for m in group.membri if m.nome == istanza), None)
    coordinatore = Membro(
        istanza,
        own.descrizione if own else "",
        own.testo if own else "",
        repo=own.repo if own else None,
    )
    others = [m for m in group.membri if m.nome != istanza]
    for member in [coordinatore, *others]:
        name = html.escape(member.nome)
        tags = []
        if member is coordinatore:
            tags.append(f'<span class="badge">{html.escape(labels["instance"])}</span>')
        repo = (
            f'<a href="{html.escape(member.repo, quote=True)}">{html.escape(labels["repo"])}</a>'
            if member.repo
            else ""
        )
        text = member.testo or member.descrizione
        description = f"<p>{_codice(html.escape(text))}</p>" if text else ""
        if member.fuori:
            heading = (
                html.escape(member.descrizione) if member.descrizione else f"<code>{name}</code>"
            )
            if member.descrizione and member.testo:
                description = f"<p>{_codice(html.escape(member.testo))}</p>"
            elif member.descrizione:
                description = ""
            tags.append(f'<span class="outside">{html.escape(labels["outside"])}</span>')
            cards.append(
                '      <li class="member static">\n'
                f"        <h2>{heading} {' '.join(tags)}</h2>\n"
                f"        {description}{f'<p>{repo}</p>' if repo else ''}\n"
                "      </li>"
            )
            continue
        if member.indirizzo:
            scheda = _remota(member.indirizzo)
            href = member.indirizzo if member.indirizzo.endswith("/") else member.indirizzo + "/"
        else:
            scheda = _scheda(base, member.nome)
            href = f"{member.nome}/"
        href = html.escape(href, quote=True)
        # L'incipit del README, pubblicato dalla vista, vince sul testo
        # dichiarato nell'istanza: quello resta il ripiego di chi non pubblica.
        if scheda.incipit:
            description = f"<p>{html.escape(scheda.incipit)}</p>"
        style = f' style="--accent: {scheda.accento}"' if scheda.accento else ""
        heading = html.escape(scheda.titolo) if scheda.titolo else f"<code>{name}</code>"
        anchors = []
        if scheda.titolo is not None or not scheda.raggiunto:
            anchors.append(f'<a href="{href}">{html.escape(labels["views"])}</a>')
        if scheda.titolo is not None and scheda.deck:
            anchors.append(
                f'<a href="{href}presentation.html">{html.escape(labels["presentation"])}</a>'
            )
        if repo:
            anchors.append(repo)
        links = f"<p>{' · '.join(anchors)}</p>" if anchors else ""
        if scheda.titolo is None and scheda.raggiunto:
            links = f'<p class="missing">{html.escape(labels["unpublished"])}</p>' + links
        tag = f" {' '.join(tags)}" if tags else ""
        cards.append(
            f'      <li class="member"{style}>\n'
            f"        <h2>{heading}{tag}</h2>\n"
            f"        {description}{_versione(scheda, labels)}{links}\n"
            "      </li>"
        )
    group_title = group.titolo or f"{labels['title']} {istanza}"
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
      :root {{ color-scheme: light dark; --ink: #1f2937; --muted: #6b7280; --bg: #f9fafb; --card: #ffffff; --line: #e5e7eb; --warn: #b45309; }}
      @media (prefers-color-scheme: dark) {{ :root {{ --ink: #e5e7eb; --muted: #9ca3af; --bg: #111827; --card: #1f2937; --line: #374151; --warn: #fbbf24; }} }}
      body {{ margin: 0; padding: 2rem 1rem; background: var(--bg); color: var(--ink); font: 16px/1.5 system-ui, sans-serif; }}
      main {{ max-width: 46rem; margin: 0 auto; }}
      h1 {{ margin: 0 0 .25rem; }}
      .intro {{ color: var(--muted); margin: 0 0 1.5rem; }}
      ul {{ list-style: none; padding: 0; margin: 0; display: grid; gap: 1rem; }}
      .member {{ background: var(--card); border: 1px solid var(--line); border-left: 6px solid var(--accent, var(--muted)); border-radius: 8px; padding: 1rem 1.25rem; }}
      .member h2 {{ font-size: 1.15rem; margin: 0 0 .25rem; }}
      .member p {{ margin: .25rem 0; }}
      .badge {{ display: inline-block; font-size: .75rem; font-weight: 600; vertical-align: middle; color: #fff; background: var(--accent, var(--muted)); border-radius: 999px; padding: .1rem .6rem; }}
      .outside {{ display: inline-block; font-size: .75rem; font-weight: 600; vertical-align: middle; color: var(--muted); border: 1px solid var(--line); border-radius: 999px; padding: .05rem .55rem; }}
      .static {{ border-left-style: dashed; }}
      .version {{ color: var(--muted); font-size: .85rem; }}
      .warn {{ color: var(--warn); font-weight: 600; }}
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
      <p class="intro">{html.escape(group.intro or labels["intro"])}</p>
{chat_section}      <ul>
{chr(10).join(cards)}
      </ul>
    </main>
  </body>
</html>
"""
