"""Lettura degli adottanti per il giro e per le sessioni: storia e interfaccia col canone.

Il giro non concede `git -C` (aggirerebbe i pattern dei permessi) e fuori dalla
cartella di lavoro nega anche le letture: questo script è il gesto concesso al
posto loro (`kb/agent-as-user.md`). È di sola lettura per costruzione: nessun
sottocomando scrive, e git gira senza lock opzionali.

Gli adottanti vengono da `world.md`, il register che li dichiara. Il checkout
si riconosce dal remote `origin`, fra le cartelle della home, perché la
disposizione cambia da host a host (su `svezia` `~/nixos` è il repo di lavoro,
su `deck` quello di casa); il nome dichiarato vale solo senza un remote GitHub.
Un adottante senza clone sull'host, dichiarato `su` un altro host, si legge
lì via `ssh <host> git -C <cartella>`, solo con `--ssh`: da `deck` gli
adottanti di lavoro non hanno copie secondarie (decisione del custode del
2026-11-12). Gli stessi comandi git, di sola lettura, girano sul checkout
remoto. Il giro autonomo passa `--ssh` a questo script e a `prescrizioni.py`,
unici gesti ssh che ha (custode, 2026-11-12): `ssh` diretto gli resta negato,
e ref e path non portano metacaratteri alla shell remota.
Un adottante che non ha clone e non si raggiunge è assente, non un marker che
non recepisce.
`show` legge solo i file con cui un adottante recepisce il canone; il resto del
dominio, dati personali compresi, resta fuori.

`audit` è la parte meccanica di `/adottanti`: legge `origin/main` dopo il
`fetch` che il chiamante ha già fatto, ricostruisce le viste in una cartella
temporanea che poi rimuove e interroga `/_stato` delle viste pubblicate. Del
dominio tocca solo i conteggi del plan e i nomi delle catture «da inoltrare»;
non scrive nei checkout. Delle trascrizioni dei giri legge, con
`commit_gate.py stadi`, solo skill invocate e path toccati. Stampa un rapporto i1 dove ogni scarto è una riga
`ROSSO`: la classificazione resta al giudizio della skill.
"""

from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import json
import os
import re
import shlex
import socket
import subprocess
import sys
import tempfile
import urllib.request
from functools import lru_cache
from pathlib import Path
from typing import NamedTuple

ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()
QUI = socket.gethostname()
REMOTI = False  # `--ssh`: legge i checkout dichiarati su altri host
SSH = ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=10"]


class Remoto(NamedTuple):
    """Il checkout dichiarato di un adottante su un altro host, letto via ssh."""

    host: str
    cartella: str  # relativa alla home remota
    windows: bool = False  # sshd con shell `cmd`, come su `danea2`

    def __str__(self) -> str:
        return f"{self.host}:~/{self.cartella}"


Checkout = Path | Remoto


def ASSENTE() -> str:  # noqa: N802
    return "checkout assente su questo host" + (
        " e non raggiungibile" if REMOTI else " (remoti con --ssh)"
    )


# L'interfaccia di un adottante col canone: regole, delega, marker, ciclo, skill.
INTERFACCIA = [
    "CLAUDE.md",
    "AGENTS.md",
    "autonomy.md",
    "i3/allineamento-metodo.md",
    "o3/ciclo/prompt.md",
    "o3/ciclo/permessi.json",
    ".claude/ciclo-prompt.md",
    ".claude/settings.json",
    ".claude/skills/*/SKILL.md",
    ".codex/skills/*/SKILL.md",
]

VOCE = re.compile(r"^- \*\*\[([\w-]+)\]\(([^)]*)\)\*\*(.*)")
REPO = re.compile(r"github\.com[:/]([\w.-]+/[\w.-]+?)(?:\.git)?/?$")
CHECKOUT = re.compile(r"checkout `~/([\w.-]+)`(?: su `([\w.-]+)`)?")
ACCENTO = re.compile(r"#[0-9a-fA-F]{6}\b")
VISTA = re.compile(r"vista (?:su )?`([\w.-]+):(\d+)`")

# Le skill che ogni adottante porta: il quartetto, la composta e l'allineamento.
SKILL_COMUNI = {"commit", "cycle", "eval", "exec", "method"}
# Canone che pesa sul recepimento: nodi, strumenti e skill canoniche.
CANONE = ("kb/", "o3/", ".claude/skills/")
SOGLIA_CANONE = 14  # giorni oltre i quali il canone non recepito è rosso
SOGLIA_CASI = 7  # giorni oltre i quali una cattura «da inoltrare» è ferma
FINESTRA_GIRI = 30  # giorni contati per i giri autonomi
LINK_MD = re.compile(r"\]\(([\w./-]+\.md)\)")


def dichiarati(world: Path = ROOT / "world.md") -> dict[str, tuple[str | None, str, str | None]]:
    """Nome → (repo GitHub `owner/nome` o None, cartella e host dichiarati), dalle voci col checkout."""
    trovati: dict[str, tuple[str | None, str, str | None]] = {}
    voce = repo = None
    for riga in world.read_text(encoding="utf-8").splitlines():
        if match := VOCE.match(riga):
            voce, repo = match.group(1), repo_di(match.group(2))
            riga = match.group(3)
        elif not riga.startswith("  "):
            voce = None
        if voce and (match := CHECKOUT.search(riga)):
            trovati[voce] = (repo, match.group(1), match.group(2))
            voce = None
    return trovati


def repo_di(url: str) -> str | None:
    match = REPO.search(url.strip())
    return match.group(1).lower() if match else None


def cloni(home: Path = HOME) -> dict[str, Path]:
    """Repo GitHub `owner/nome` → primo checkout della home col remote `origin` su quel repo."""
    trovati: dict[str, Path] = {}
    try:
        cartelle = sorted(p for p in home.iterdir() if (p / ".git").exists())
    except OSError:
        return trovati
    for cartella in cartelle:
        repo = repo_di(git(cartella, "config", "--get", "remote.origin.url").stdout)
        if repo:
            trovati.setdefault(repo, cartella)
    return trovati


@lru_cache(maxsize=None)
def raggiungibile(remoto: Remoto) -> bool:
    """Il checkout remoto risponde a `git rev-parse` via ssh; annota se l'host è Windows."""
    try:
        sonda = subprocess.run(
            [*SSH, remoto.host, "echo %OS%"], capture_output=True, text=True, check=False
        )
    except OSError:  # ssh assente dal PATH
        return False
    if sonda.returncode:
        return False
    WINDOWS[remoto.host] = "Windows_NT" in sonda.stdout
    remoto = remoto._replace(windows=WINDOWS[remoto.host])
    return git(remoto, "rev-parse", "--git-dir").returncode == 0


WINDOWS: dict[str, bool] = {}  # host → shell `cmd`, dalla sonda di `raggiungibile`


def adottanti(
    world: Path = ROOT / "world.md", home: Path = HOME, qui: str = QUI, prova=None
) -> dict[str, Checkout]:
    """Nome → checkout locale, o remoto se dichiarato su un altro host; gli assenti li dice `assenti`."""
    if prova is None:
        prova = raggiungibile if REMOTI else (lambda remoto: False)
    trovati, presenti = {}, None
    for nome, (repo, cartella, host) in dichiarati(world).items():
        if repo is None:
            trovati[nome] = home / cartella
            continue
        presenti = cloni(home) if presenti is None else presenti
        if repo in presenti:
            trovati[nome] = presenti[repo]
        elif host and host != qui and prova(remoto := Remoto(host, cartella)):
            trovati[nome] = remoto._replace(windows=WINDOWS.get(host, False))
    return trovati


def assenti(
    world: Path = ROOT / "world.md", home: Path = HOME, qui: str = QUI, prova=None
) -> list[str]:
    """Gli adottanti dichiarati senza un clone su questo host né uno remoto raggiungibile."""
    presenti = adottanti(world, home, qui, prova)
    return [nome for nome in dichiarati(world) if nome not in presenti]


def voci(world: Path = ROOT / "world.md") -> dict[str, str]:
    """Nome → testo intero della voce in grassetto di `world.md`, righe di seguito comprese."""
    trovate: dict[str, str] = {}
    voce = None
    for riga in world.read_text(encoding="utf-8").splitlines():
        if match := VOCE.match(riga):
            voce = match.group(1)
            trovate[voce] = match.group(3)
        elif voce and riga.startswith("  "):
            trovate[voce] += " " + riga.strip()
        else:
            voce = None
    return trovate


def di_metodo(world: Path = ROOT / "world.md") -> str:
    """Il paragrafo di `world.md` che dichiara accento e vista di `method`."""
    testo = world.read_text(encoding="utf-8")
    return next((p for p in testo.split("\n\n") if "Quello di `method`" in p), "")


# Ref e path passano anche per la shell remota (`cmd` su Windows): niente
# metacaratteri, così un argomento non diventa un secondo comando.
SICURO = re.compile(r"^[A-Za-z0-9_./-]+$")


def ammesso(path: str) -> bool:
    if ".." in Path(path).parts or not SICURO.match(path):
        return False
    return any(fnmatch.fnmatchcase(path, schema) for schema in INTERFACCIA)


def comando(checkout: Checkout, args: tuple[str, ...]) -> list[str]:
    """Il comando git sul checkout: locale, o via ssh sull'host dichiarato."""
    if isinstance(checkout, Remoto) and checkout.windows:
        # `cmd` non ha `env` né le virgolette singole: quoting di Windows.
        remoto = subprocess.list2cmdline(["git", "-C", checkout.cartella, *args])
        return [*SSH, checkout.host, f"set GIT_OPTIONAL_LOCKS=0&& {remoto}"]
    if isinstance(checkout, Remoto):
        remoto = ["env", "GIT_OPTIONAL_LOCKS=0", "git", "-C", checkout.cartella, *args]
        return [*SSH, checkout.host, shlex.join(remoto)]
    return ["git", "-C", str(checkout), *args]


def git(checkout: Checkout, *args: str) -> subprocess.CompletedProcess:
    env = {**os.environ, "GIT_OPTIONAL_LOCKS": "0"}
    try:
        return subprocess.run(
            comando(checkout, args), capture_output=True, text=True, env=env, check=False
        )
    except OSError as errore:  # ssh assente dal PATH
        return subprocess.CompletedProcess(args, 127, "", str(errore))


def commit(checkout: Checkout, ref: str) -> str:
    esito = git(checkout, "log", "-1", "--format=%h %ad %s", "--date=iso-strict", ref)
    return esito.stdout.strip() if esito.returncode == 0 else f"assente ({ref})"


def stato(nome: str, checkout: Checkout) -> list[str]:
    if isinstance(checkout, Path) and not (checkout / ".git").exists():
        return [f"{nome}: checkout assente in {checkout}"]
    righe = [f"{nome} ({checkout})"]
    righe.append(f"  HEAD         {commit(checkout, 'HEAD')}")
    righe.append(f"  origin/main  {commit(checkout, 'origin/main')}")
    conto = git(checkout, "rev-list", "--left-right", "--count", "HEAD...origin/main")
    if conto.returncode == 0:
        avanti, indietro = conto.stdout.split()
        righe.append(f"  rispetto a origin/main: {avanti} avanti, {indietro} indietro")
    tree = git(checkout, "status", "--porcelain")
    if tree.returncode == 0:
        sporchi = len(tree.stdout.splitlines())
        righe.append(f"  working tree: {'pulito' if not sporchi else f'{sporchi} file modificati'}")
    return righe


def scegli(nome: str, tutti: dict[str, Checkout]) -> Checkout:
    if nome not in tutti:
        if nome in dichiarati():
            sys.exit(f"{nome}: {ASSENTE()}")
        sys.exit(f"adottante sconosciuto: {nome}; adottanti in world.md: {', '.join(tutti)}")
    return tutti[nome]


def frontmatter(testo: str) -> dict[str, str]:
    if not testo.startswith("---\n"):
        return {}
    corpo = testo[4:].split("\n---", 1)[0]
    return dict(
        (chiave.strip(), valore.strip())
        for chiave, _, valore in (r.partition(":") for r in corpo.splitlines())
        if valore
    )


def conteggio_plan(testo: str) -> tuple[int, int]:
    """Righe `dev` e `runtime` della tabella del plan."""
    righe = [r.split("|")[1].strip() for r in testo.splitlines() if r.startswith("|")]
    return righe.count("dev"), righe.count("runtime")


def prescrizioni_aperte(indice: str) -> list[str]:
    """I nomi delle prescrizioni nei Contenuti di `o3/prescriptions.md`."""
    contenuti = indice.split("## Contenuti", 1)[-1].split("\n## ", 1)[0]
    return [m.removesuffix(".md") for m in LINK_MD.findall(contenuti) if "/" not in m]


def casi_da_inoltrare(file: dict[str, str]) -> list[str]:
    """Le catture i1 «da inoltrare»: nel corpo o nella voce d'indice che le linka.

    Lo stato lo dichiara la voce d'indice: una cattura che l'indice dà
    «acquisita» è passata anche se il corpo dice ancora «da inoltrare». Un
    indice che descrive gli stati senza linkare una cattura non conta.
    """
    trovati, acquisite = set(), set()
    for path, testo in file.items():
        nome = Path(path).name
        if nome != "perceptions.md":
            if "da inoltrare" in testo and "acquisita da method" not in testo:
                trovati.add(nome)
            continue
        for voce in re.split(r"\n(?=- )", testo):
            catture = {Path(link).name for link in LINK_MD.findall(voce)}
            if "acquisita" in voce:
                acquisite |= catture
            elif "da inoltrare" in voce:
                trovati |= catture
    return sorted(trovati - acquisite)


def accenti_ripetuti(accenti: dict[str, str]) -> list[str]:
    visti: dict[str, list[str]] = {}
    for nome, colore in accenti.items():
        visti.setdefault(colore.lower(), []).append(nome)
    return [f"{c} in {', '.join(n)}" for c, n in visti.items() if len(n) > 1]


def mostra(checkout: Checkout, path: str, ref: str = "origin/main") -> str:
    esito = git(checkout, "show", f"{ref}:{path}")
    return esito.stdout if esito.returncode == 0 else ""


def giorni_fa(checkout: Checkout, ref: str, *path: str) -> int | None:
    esito = git(checkout, "log", "-1", "--format=%ct", ref, "--", *path)
    if esito.returncode or not esito.stdout.strip():
        return None
    quando = dt.datetime.fromtimestamp(int(esito.stdout), dt.timezone.utc)
    return (dt.datetime.now(dt.timezone.utc) - quando).days


def canale(nome: str, checkout: Checkout) -> list[str]:
    marker = frontmatter(mostra(checkout, "i3/allineamento-metodo.md"))
    commit_m = marker.get("method_commit", "")
    stato_m = marker.get("status", "?")
    if not commit_m:
        return [f"ROSSO {nome}: marker senza method_commit su origin/main"]
    conto = git(ROOT, "rev-list", "--count", f"{commit_m}..HEAD").stdout.strip() or "?"
    righe = [
        f"{nome}: {stato_m} a {commit_m[:7]} ({marker.get('reviewed_at', '?')}), {conto} dietro"
    ]
    if stato_m != "aligned":
        righe.append(f"ROSSO {nome}: status {stato_m}")
    limite = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=SOGLIA_CANONE)
    vecchi = git(
        ROOT,
        "log",
        "--format=%h %s",
        f"--until={limite.isoformat()}",
        f"{commit_m}..HEAD",
        "--",
        *CANONE,
    ).stdout.splitlines()
    if vecchi:
        righe.append(
            f"ROSSO {nome}: {len(vecchi)} commit di canone oltre {SOGLIA_CANONE} giorni non recepiti, "
            f"il più vecchio {vecchi[-1]}"
        )
    return righe


def prescrizioni(tutti: dict[str, Checkout]) -> list[str]:
    import prescrizioni as presc  # importa adottanti: qui per non chiudere il cerchio

    righe = []
    for nome in prescrizioni_aperte((ROOT / "o3" / "prescriptions.md").read_text(encoding="utf-8")):
        esiti = presc.esiti(nome)
        # Gli assenti dall'host sono già rossi nel canale: qui contano i marker letti.
        mancano = [a for a, ok in esiti.items() if ok is False]
        if not mancano and None not in esiti.values():
            righe.append(f"ROSSO {nome}: recepita da tutti secondo lo strumento, da chiudere")
            continue
        for adottante in mancano:
            riga = riga_marker(mostra(tutti[adottante], "i3/allineamento-metodo.md"), nome)
            if riga is None:
                righe.append(f"{nome}: {adottante} non la nomina nel marker")
            elif SODDISFATTA.search(riga):
                righe.append(
                    f"ROSSO {nome}: {adottante} la dà soddisfatta, lo strumento non la riconosce"
                )
            else:
                righe.append(f"{nome}: {adottante} «{riga[:100]}»")
    return righe


SODDISFATTA = re.compile(r"(?<!non )soddisfatt", re.IGNORECASE)


def riga_marker(testo: str, nome: str) -> str | None:
    """La voce del marker che nomina la prescrizione, sulle righe di seguito comprese."""
    righe = testo.splitlines()
    for i, riga in enumerate(righe):
        if f"`{nome}`" in riga:
            voce = [riga.strip()]
            for seguito in righe[i + 1 : i + 3]:
                if not seguito.startswith("  "):
                    break
                voce.append(seguito.strip())
            return re.sub(r"^[-*] ", "", " ".join(voce))
    return None


def costruisci(nome: str, checkout: Checkout, base: Path) -> str | None:
    """Estrae origin/main in `base/<nome>` e lancia `build.py --check`: None se passa."""
    archivio = git_bytes(checkout, "archive", "origin/main")
    if archivio is None:
        return "git archive fallito"
    destinazione = base / nome
    destinazione.mkdir()
    # tar e non tarfile: i symlink `../method/...` escono dall'estratto per costruzione.
    estratto = subprocess.run(
        ["tar", "-x", "-C", str(destinazione)], input=archivio, capture_output=True, check=False
    )
    if estratto.returncode:
        return "estrazione fallita"
    try:
        esito = subprocess.run(
            [sys.executable, "o3/view/build.py", "--check"],
            cwd=destinazione,
            capture_output=True,
            text=True,
            timeout=600,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return "build oltre 600 secondi"
    if esito.returncode:
        uscita = (esito.stdout + esito.stderr).strip().splitlines()
        return uscita[-1] if uscita else f"uscita {esito.returncode}"
    return None


def git_bytes(checkout: Checkout, *args: str) -> bytes | None:
    env = {**os.environ, "GIT_OPTIONAL_LOCKS": "0"}
    try:
        esito = subprocess.run(comando(checkout, args), capture_output=True, env=env, check=False)
    except OSError:
        return None
    return esito.stdout if esito.returncode == 0 else None


def servita(host: str, porta: str) -> tuple[str | None, str]:
    """(commit servito, nota) da `/_stato`; commit None se la porta non risponde."""
    try:
        with urllib.request.urlopen(f"http://{host}:{porta}/_stato", timeout=5) as risposta:
            stato_v = json.load(risposta)
    except (OSError, ValueError) as errore:
        return None, f"non raggiunta ({errore.__class__.__name__})"
    nota = "" if stato_v.get("ok") else "ok: false"
    return stato_v.get("served_commit", ""), nota


def viste(tutti: dict[str, Checkout], testi: dict[str, str], build: bool) -> list[str]:
    righe = []
    indirizzi = {n: VISTA.search(t) for n, t in testi.items() if n in tutti}
    indirizzi["metodo"] = VISTA.search(di_metodo())
    checkout = {**tutti, "metodo": ROOT}
    with tempfile.TemporaryDirectory(prefix="adottanti-") as tmp:
        base = Path(tmp)
        (base / "method").symlink_to(ROOT)  # i symlink `../method/...` degli estratti
        for nome, match in indirizzi.items():
            origine = git(checkout[nome], "rev-parse", "origin/main").stdout.strip()
            if build and nome != "metodo":
                errore = costruisci(nome, checkout[nome], base)
                righe.append(
                    f"ROSSO {nome}: build --check fallita: {errore}"
                    if errore
                    else f"{nome}: build --check ok"
                )
            if not match:
                righe.append(f"ROSSO {nome}: nessuna vista `host:porta` in world.md")
                continue
            host, porta = match.groups()
            commit_s, nota = servita(host, porta)
            if commit_s is None:
                righe.append(f"ROSSO {nome}: {host}:{porta} {nota}, non verificata")
            elif commit_s != origine or nota:
                righe.append(
                    f"ROSSO {nome}: {host}:{porta} serve {commit_s[:8]}, origin/main {origine[:8]} {nota}".rstrip()
                )
            else:
                righe.append(f"{nome}: {host}:{porta} serve origin/main {origine[:8]}")
    return righe


def accenti(tutti: dict[str, Checkout], testi: dict[str, str]) -> list[str]:
    righe, colori = [], {}
    for nome, checkout in tutti.items():
        dichiarato = ACCENTO.search(testi.get(nome, ""))
        nel_repo = ACCENTO.search(mostra(checkout, "o3/view/project.py"))
        if not (dichiarato and nel_repo):
            righe.append(f"ROSSO {nome}: accento assente in world.md o in o3/view/project.py")
            continue
        colori[nome] = nel_repo.group(0)
        if dichiarato.group(0).lower() != nel_repo.group(0).lower():
            righe.append(
                f"ROSSO {nome}: world.md {dichiarato.group(0)}, project.py {nel_repo.group(0)}"
            )
    if proprio := ACCENTO.search(di_metodo()):
        colori["metodo"] = proprio.group(0)
    righe += [f"ROSSO accento ripetuto: {r}" for r in accenti_ripetuti(colori)]
    return righe or ["accenti: copie coincidenti e tutti distinti"]


def skill(nome: str, checkout: Checkout) -> list[str]:
    def elenco(cartella: str) -> set[str]:
        uscita = git(checkout, "ls-tree", "--name-only", "origin/main", f"{cartella}/").stdout
        return {Path(r).name for r in uscita.splitlines()}

    claude, codex = elenco(".claude/skills"), elenco(".codex/skills")
    righe = [f"{nome}: {' '.join(sorted(claude))}"]
    if mancano := SKILL_COMUNI - claude:
        righe.append(f"ROSSO {nome}: mancano {', '.join(sorted(mancano))}")
    if claude != codex:
        righe.append(f"ROSSO {nome}: wrapper Codex diversi ({' '.join(sorted(claude ^ codex))})")
    return righe


def casi(nome: str, checkout: Checkout) -> list[str]:
    paths = git(checkout, "ls-tree", "--name-only", "origin/main", "i1/").stdout.split()
    file = {p: mostra(checkout, p) for p in paths if p.endswith(".md")}
    in_metodo = " ".join(p.read_text(encoding="utf-8") for p in (ROOT / "i1").glob("*.md"))
    righe = []
    for cattura in casi_da_inoltrare(file):
        eta = giorni_fa(checkout, "origin/main", f"i1/{cattura}")
        nota = (
            "citata in method/i1"
            if cattura.removesuffix(".md") in in_metodo
            else "assente in method/i1"
        )
        riga = (
            f"{nome}: i1/{cattura} da inoltrare da {eta if eta is not None else '?'} giorni, {nota}"
        )
        righe.append(("ROSSO " if eta is not None and eta > SOGLIA_CASI else "") + riga)
    return righe


def numeri(nome: str, checkout: Checkout) -> str:
    dev, runtime = conteggio_plan(mostra(checkout, "o1/plan.md"))
    motivi = git(
        checkout,
        "log",
        "origin/main",
        f"--since={FINESTRA_GIRI} days ago",
        "--format=%(trailers:key=Impatto-motivo,valueonly,separator=%x20)",
    ).stdout.splitlines()
    giri = sum("ciclo-autonomo" in m for m in motivi)
    return (
        f"{nome}: plan {dev} dev, {runtime} runtime; {giri} giri autonomi in {FINESTRA_GIRI} giorni"
    )


def stadi_giro(nome: str, checkout: Checkout) -> list[str]:
    """Stadi di `Esiti:` dell'ultimo giro senza traccia nella trascrizione;
    solo nomi di stadi e di path, il dominio resta fuori."""
    sys.path.insert(0, str(ROOT / "o3"))
    import commit_gate

    if isinstance(checkout, Remoto):
        return [f"{nome}: trascrizione dei giri su {checkout.host}, non letta da qui"]
    if not (checkout / commit_gate.TENTATIVI).exists():
        return [f"{nome}: nessuna trascrizione dei giri sull'host"]
    righe, trovate = commit_gate.verifica_stadi(checkout)
    if not trovate:
        return [f"{nome}: stadi ok" if "dichiarati" in righe[0] else f"{nome}: {righe[0]}"]
    stadi = " ".join(t.split()[0] for t in trovate)
    return [f"ROSSO {nome}: stadi dichiarati senza traccia nell'ultimo giro: {stadi}"]


def audit(tutti: dict[str, Checkout], build: bool = True) -> list[str]:
    testi = voci()
    mancanti = [f"ROSSO {n}: {ASSENTE()}" for n in assenti()]
    sezioni = [
        ("Canale", mancanti + [r for n, c in tutti.items() for r in canale(n, c)]),
        ("Prescrizioni aperte", prescrizioni(tutti)),
        ("Viste", viste(tutti, testi, build)),
        ("Accenti", accenti(tutti, testi)),
        ("Skill", [r for n, c in tutti.items() for r in skill(n, c)]),
        (
            "Casi della delega da inoltrare",
            [r for n, c in tutti.items() for r in casi(n, c)] or ["nessuno"],
        ),
        ("Code e giri", [numeri(n, c) for n, c in tutti.items()]),
        ("Stadi dei giri", [r for n, c in tutti.items() for r in stadi_giro(n, c)]),
    ]
    righe = [
        f"# Audit adottanti, {dt.date.today().isoformat()}, metodo a {commit(ROOT, 'HEAD')}",
        "",
    ]
    for titolo, contenuto in sezioni:
        righe += [f"## {titolo}", "", *[f"- {r}" for r in contenuto], ""]
    rossi = sum(r.startswith("- ROSSO") for r in righe)
    righe.append(f"Rossi: {rossi}")
    return righe


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__.splitlines()[0],
        epilog="File leggibili con show: " + ", ".join(INTERFACCIA),
    )
    parser.add_argument(
        "--ssh",
        action="store_true",
        help="legge via ssh i checkout dichiarati su altri host (in sessione, non nel giro)",
    )
    sub = parser.add_subparsers(dest="comando", required=True)
    p_stato = sub.add_parser("stato", help="HEAD, origin/main, distanza e working tree")
    p_stato.add_argument("nomi", nargs="*", help="adottanti; tutti se omessi")
    p_log = sub.add_parser("log", help="ultimi commit con data e trailer")
    p_log.add_argument("nome")
    p_log.add_argument("-n", type=int, default=5)
    p_log.add_argument("--ref", default="HEAD")
    p_show = sub.add_parser("show", help="un file dell'interfaccia col canone")
    p_show.add_argument("nome")
    p_show.add_argument("path")
    p_show.add_argument("--ref", default="HEAD")
    p_audit = sub.add_parser("audit", help="parte meccanica di /adottanti, dopo il fetch")
    p_audit.add_argument("--senza-build", action="store_true", help="salta build.py --check")
    args = parser.parse_args(argv)
    if not SICURO.match(getattr(args, "ref", "HEAD")):
        sys.exit(f"ref non ammesso: {args.ref}")

    global REMOTI
    REMOTI = args.ssh
    tutti = adottanti()
    if args.comando == "audit":
        print("\n".join(audit(tutti, build=not args.senza_build)))
        return 0
    if args.comando == "stato":
        for nome in args.nomi or dichiarati():
            if nome in dichiarati() and nome not in tutti:
                print(f"{nome}: {ASSENTE()}")
                continue
            print("\n".join(stato(nome, scegli(nome, tutti))))
        return 0
    checkout = scegli(args.nome, tutti)
    if args.comando == "log":
        formato = "%h %ad %s%n%(trailers:unfold,separator=%x0a  )"
        esito = git(
            checkout, "log", f"-{args.n}", f"--format={formato}", "--date=iso-strict", args.ref
        )
    else:
        if not ammesso(args.path):
            sys.exit(
                f"{args.path} è fuori dall'interfaccia col canone; leggibili: "
                + ", ".join(INTERFACCIA)
            )
        esito = git(checkout, "show", f"{args.ref}:{args.path}")
    sys.stdout.write(esito.stdout)
    sys.stderr.write(esito.stderr)
    return esito.returncode


if __name__ == "__main__":
    # `prescrizioni` importa `adottanti`: deve vedere lo stesso `REMOTI`.
    sys.modules.setdefault("adottanti", sys.modules["__main__"])
    sys.exit(main())
