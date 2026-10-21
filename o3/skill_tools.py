"""Guardiano quantitativo delle skill: misure e controlli deterministici, nessun giudizio.

Il criterio vive nei nodi `skill`, `skill-composition` e `agent-as-user`; qui
si producono evidenze. Le skill si leggono da `.claude/skills/*/SKILL.md` (i
wrapper di altri harness rinviano lì); i permessi da `.claude/settings.json`
(sessione) e `o3/ciclo/permessi.json` (giro). Il canone si trova dal symlink
`method/` dell'adottante; in `method` il canone è il repo stesso.

L'estrazione dei comandi è euristica: legge gli span di codice con almeno un
argomento e le righe dei blocchi di codice il cui primo token è un eseguibile.
I candidati vanno classificati, non corretti alla cieca.
"""

from __future__ import annotations

import argparse
import difflib
import fnmatch
import importlib.util
import json
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

SKILLS = Path(".claude/skills")
SETTINGS = Path(".claude/settings.json")
PERMESSI_GIRO = Path("o3/ciclo/permessi.json")
PROMPT_GIRO = Path("o3/ciclo/prompt.md")
GATE = Path("o3/commit_gate.py")
GIORNI = 30

SPAN = re.compile(r"`([^`\n]+)`")
FENCE = re.compile(r"^```")
SEPARATORI = re.compile(r"\s*(?:&&|\|\||;|\|)\s*")
SEGNAPOSTO = re.compile(r"<[^>]+>|…|\.\.\.")
VARIABILE = re.compile(r"\$\{?\w+")
# Un gesto retto da una negazione annuncia un vincolo, non lo esegue: «senza `X`»,
# «non usare `X`», oppure «`X` … le fa negare».
ANNUNCIO_PRIMA = re.compile(
    r"(?<!\w)(né|senza|niente|mai|non usare|non usarl[oa]|non lanciare|non eseguire|non si concede)"
    r"\s+(?:(?:un|uno|una|il|lo|la|l'|i|gli|le)\s+)?$",
    re.IGNORECASE,
)
ANNUNCIO_DOPO = re.compile(r"^[^.;:]{0,40}\b(negat\w*|negar\w*|vietat\w*)", re.IGNORECASE)
COMPONE = re.compile(r"^\s+compone:\s*(.+)$")
CARTELLO = re.compile(
    r"\b(non usare|non usarl[oa]|non è concess[oa]|non sono concessi|è negat[oa]|sono negati"
    r"|vietat[oa]|mai usare|non lanciare|non eseguire)\b",
    re.IGNORECASE,
)
VERBO_CHIAMATA = re.compile(
    r"\b(esegui|invoca|chiama|lancia|avvia|segui|seguendo)\b", re.IGNORECASE
)
RIMANDO = re.compile(r"(?<![\w.])(?:\.\./)*(?:kb|o3|method)/[\w./-]+")
ESEMPIO_PROSSIMO = re.compile(r"^Prossimo: (.+)$")
ESEGUIBILI_SHELL = {"git", "python3", "jq", "sed", "grep", "rg", "ls", "cat", "head", "tail"}


@dataclass
class Skill:
    nome: str
    path: Path
    righe: list[str]
    accanto: int = 0
    comandi: list[tuple[int, str]] = field(default_factory=list)
    compone: list[str] | None = None


def composizione(righe: list[str]) -> list[str] | None:
    """Le skill dichiarate in `metadata: compone:` del frontmatter, o None."""
    if not righe or righe[0] != "---":
        return None
    in_metadata = False
    for riga in righe[1:]:
        if riga == "---":
            break
        if not riga.startswith((" ", "\t")):
            in_metadata = riga.startswith("metadata:")
        elif in_metadata and (match := COMPONE.match(riga)):
            return match.group(1).replace(",", " ").split()
    return None


def leggi_skill(root: Path) -> list[Skill]:
    trovate = []
    for path in sorted((root / SKILLS).glob("*/SKILL.md")):
        righe = path.read_text(encoding="utf-8").splitlines()
        accanto = sum(
            len(altro.read_text(encoding="utf-8", errors="replace").splitlines())
            for altro in path.parent.rglob("*")
            if altro.is_file() and altro != path and altro.suffix in {".md", ".txt"}
        )
        skill = Skill(path.parent.name, path, righe, accanto)
        skill.comandi = comandi(righe)
        skill.compone = composizione(righe)
        trovate.append(skill)
    return trovate


def eseguibile(token: str) -> bool:
    if token in ESEGUIBILI_SHELL or token.startswith(("o3/", "./")):
        return True
    return bool(re.fullmatch(r"[a-z][\w.+-]*", token)) and shutil.which(token) is not None


def comandi(righe: list[str]) -> list[tuple[int, str]]:
    """(riga, comando) dagli span con argomenti e dalle righe dei blocchi di codice."""
    trovati: list[tuple[int, str]] = []
    in_blocco = False
    for numero, riga in enumerate(righe, 1):
        if FENCE.match(riga.strip()):
            in_blocco = not in_blocco
            continue
        candidati = [riga.strip()] if in_blocco else SPAN.findall(riga)
        for testo in candidati:
            if not testo or (not in_blocco and " " not in testo):
                continue
            primo = testo.split()[0]
            if eseguibile(primo):
                trovati.append((numero, testo))
    return trovati


def regole(path: Path) -> tuple[list[str], list[str]]:
    if not path.exists():
        return [], []
    dati = json.loads(path.read_text(encoding="utf-8")).get("permissions", {})

    def bash(voci: list[str]) -> list[str]:
        return [v[5:-1] for v in voci if v.startswith("Bash(") and v.endswith(")")]

    return bash(dati.get("allow", [])), bash(dati.get("deny", []))


def corrisponde(comando: str, schema: str) -> bool:
    schema = schema.replace(":*", " *")
    if fnmatch.fnmatchcase(comando, schema):
        return True
    return schema.endswith(" *") and comando == schema[:-2]


def parti(comando: str) -> list[str]:
    testo = SEGNAPOSTO.sub("X", comando)
    pezzi = [p.strip() for p in SEPARATORI.split(testo) if p.strip()]
    # Uno script di o3/ scritto senza interprete si lancia come lo concedono i permessi.
    return [f"python3 {p}" if re.match(r"o3/\S+\.py\b", p) else p for p in pezzi]


def negato(comando: str, deny: list[str]) -> bool:
    return any(corrisponde(p, s) for p in parti(comando) for s in deny)


def concesso(comando: str, allow: list[str], deny: list[str]) -> bool:
    pezzi = parti(comando)
    return all(any(corrisponde(p, s) for s in allow) for p in pezzi) and not negato(comando, deny)


def skill_del_giro(skills: list[Skill]) -> set[str]:
    """`cycle` e, a cascata, ciò che le composte dichiarano di comporre."""
    per_nome = {s.nome: s for s in skills}
    giro: set[str] = set()
    da_visitare = ["cycle"] if "cycle" in per_nome else []
    while da_visitare:
        nome = da_visitare.pop()
        if nome in giro or nome not in per_nome:
            continue
        giro.add(nome)
        da_visitare += per_nome[nome].compone or []
    return giro


def tipo(comando: str, riga: str) -> str:
    """annuncio di un vincolo, modello con segnaposti, oppure comando."""
    prima_del_gesto = riga.split(f"`{comando}`")[0] if f"`{comando}`" in riga else ""
    dopo_il_gesto = riga.split(f"`{comando}`", 1)[-1] if f"`{comando}`" in riga else ""
    if ANNUNCIO_PRIMA.search(prima_del_gesto) or ANNUNCIO_DOPO.search(dopo_il_gesto):
        return "annuncio"
    if SEGNAPOSTO.search(comando) or VARIABILE.search(comando):
        return "modello"
    return "comando"


def chiamate(skill: Skill, nomi: set[str]) -> list[tuple[int, str]]:
    trovate = []
    for numero, riga in enumerate(skill.righe, 1):
        if not VERBO_CHIAMATA.search(riga):
            continue
        for nome in nomi - {skill.nome}:
            match = re.search(rf"`/{re.escape(nome)}\b", riga)
            if match and not ANNUNCIO_PRIMA.search(riga[: match.start()]):
                trovate.append((numero, nome))
    return trovate


def storia(root: Path, path: Path) -> tuple[int | None, int | None]:
    """Righe alla nascita e GIORNI fa, dalla storia git del file."""
    rel = str(path.relative_to(root))

    def git(*args: str) -> str:
        esito = subprocess.run(
            ["git", "-C", str(root), *args], capture_output=True, text=True, check=False
        )
        return esito.stdout.strip() if esito.returncode == 0 else ""

    def righe_a(sha: str) -> int | None:
        testo = git("show", f"{sha}:{rel}") if sha else ""
        return len(testo.splitlines()) if testo else None

    nascita = git("log", "--diff-filter=A", "--format=%H", "--follow", "--", rel).splitlines()
    prima = git("log", "-1", f"--before={GIORNI}.days", "--format=%H", "--", rel)
    return righe_a(nascita[-1] if nascita else ""), righe_a(prima)


def canone_di(root: Path) -> Path | None:
    link = root / "method"
    if link.is_symlink() or link.is_dir():
        canone = link.resolve().parent
        if canone != root.resolve() and (canone / SKILLS).is_dir():
            return canone
    return None


def divergenza(skill: Skill, canone: Path | None) -> tuple[int, int] | None:
    if canone is None:
        return None
    originale = canone / SKILLS / skill.nome / "SKILL.md"
    if not originale.exists():
        return None
    diff = difflib.ndiff(originale.read_text(encoding="utf-8").splitlines(), skill.righe)
    aggiunte = rimosse = 0
    for riga in diff:
        aggiunte += riga.startswith("+ ")
        rimosse += riga.startswith("- ")
    return aggiunte, rimosse


def gate_prossimo(root: Path, canone: Path | None) -> re.Pattern[str] | None:
    path = (canone or root) / GATE
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location("commit_gate", path)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.PROSSIMO


def esempi_prossimo(righe: list[str]) -> list[tuple[int, str]]:
    """Esempi di trailer `Prossimo:` nei blocchi di codice e negli span."""
    trovati, blocco = [], False
    for numero, riga in enumerate(righe, 1):
        if FENCE.match(riga.strip()):
            blocco = not blocco
            continue
        candidati = [riga.strip()] if blocco else SPAN.findall(riga)
        for testo in candidati:
            if m := ESEMPIO_PROSSIMO.match(testo.strip()):
                trovati.append((numero, m.group(1)))
    return trovati


def audit(root: Path) -> str:
    skills = leggi_skill(root)
    nomi = {s.nome for s in skills}
    allow_s, deny_s = regole(root / SETTINGS)
    allow_g, deny_g = regole(root / PERMESSI_GIRO)
    giro = skill_del_giro(skills) if (root / PERMESSI_GIRO).exists() else set()
    canone = canone_di(root)
    out = [f"## Skill di {root.resolve().name}", ""]

    out += ["### Dimensioni e rimandi", ""]
    for s in sorted(skills, key=lambda s: -len(s.righe)):
        piene = [r for r in s.righe if r.strip()]
        rimandi = sum(1 for r in piene if RIMANDO.search(r))
        nascita, prima = storia(root, s.path)
        parti_riga = [f"- {s.nome}: {len(s.righe)} righe"]
        if s.accanto:
            parti_riga.append(f"{s.accanto} nei file accanto")
        parti_riga.append(f"rimandi a kb/ o3/ method/ in {rimandi}/{len(piene)} righe piene")
        if nascita is not None:
            parti_riga.append(f"alla nascita {nascita}")
        if prima is not None:
            parti_riga.append(f"{GIORNI} giorni fa {prima}")
        if (diff := divergenza(s, canone)) is not None:
            parti_riga.append(f"rispetto al canone +{diff[0]} −{diff[1]}")
        out.append("; ".join(parti_riga))
    out.append("")

    out += ["### Comandi contro i permessi", ""]
    cycle = next((s for s in skills if s.nome == "cycle"), None)
    if not (root / PERMESSI_GIRO).exists():
        out.append("Nessun `o3/ciclo/permessi.json`: controllato solo il contesto di sessione.")
    elif cycle and cycle.compone is None:
        out.append("`cycle` non dichiara `metadata: compone:`: nel giro si controlla solo `cycle`.")
    else:
        out.append(f"Skill del giro, dalle composizioni dichiarate: {', '.join(sorted(giro))}.")
    out.append("")
    sezioni: dict[str, list[str]] = {"comando": [], "modello": [], "annuncio": []}
    for s in skills:
        for numero, comando in s.comandi:
            nel_giro = s.nome in giro
            vietato_s = negato(comando, deny_s)
            fuori_giro = nel_giro and not concesso(comando, allow_g + allow_s, deny_g + deny_s)
            classe = tipo(comando, s.righe[numero - 1])
            voce = f"- {s.nome}:{numero} `{comando}`"
            if classe == "annuncio":
                if vietato_s or fuori_giro:
                    continue
                stato = "gesto concesso" if nel_giro else "nessun deny in sessione"
                sezioni["annuncio"].append(f"{voce} — {stato}: annuncio senza vincolo dietro?")
                continue
            note = ["negato in sessione"] * vietato_s + ["non concesso nel giro"] * fuori_giro
            if note:
                sezioni[classe].append(f"{voce} — {', '.join(note)}")
    out += sezioni["comando"] or ["- nessun comando scritto fuori dai permessi del suo contesto"]
    out += ["", "### Modelli", ""]
    out.append("Comandi con segnaposti o variabili: spesso testo descrittivo, a volte eseguiti.")
    out.append("")
    out += sezioni["modello"] or ["- nessuno fuori dai permessi"]
    out += ["", "### Vincoli annunciati", ""]
    out.append("Gesti nominati in contesto negativo: coerenti se il vincolo c'è, e non elencati.")
    out.append("")
    out += sezioni["annuncio"] or ["- tutti con il vincolo dietro"]
    out.append("")

    out += ["### Divieti scritti", ""]
    trovati = 0
    for s in skills:
        for numero, riga in enumerate(s.righe, 1):
            if not CARTELLO.search(riga):
                continue
            spans = SPAN.findall(riga)
            if not spans:
                continue
            deny = deny_s + deny_g
            retto = any(
                negato(t, deny) if eseguibile(t.split()[0]) else any(t in d for d in deny)
                for t in spans
                if t.split()
            )
            stato = (
                "con deny"
                if retto
                else "deny non trovato nella stessa grafia: vincolo altrove o lacuna"
            )
            trovati += 1
            out.append(f"- {s.nome}:{numero} — {stato}: {riga.strip()[:140]}")
    if not trovati:
        out.append("- nessuno")
    out.append("")

    out += ["### Esempi di trailer contro il gate", ""]
    prossimo = gate_prossimo(root, canone)
    if prossimo is None:
        out.append(f"- `{GATE}` non trovato nel canone: esempi non controllati")
    else:
        fonti = [(s.nome, s.righe) for s in skills]
        if (root / PROMPT_GIRO).exists():
            testo = (root / PROMPT_GIRO).read_text(encoding="utf-8")
            fonti.append((PROMPT_GIRO.as_posix(), testo.splitlines()))
        fuori = [
            f"- {nome}:{numero} `Prossimo: {valore}` — il gate lo rifiuta"
            for nome, righe in fonti
            for numero, valore in esempi_prossimo(righe)
            if not prossimo.match(valore)
        ]
        out += fuori or ["- tutti gli esempi di `Prossimo:` passano il gate"]
    out.append("")

    out += ["### Composizione", ""]
    for s in skills:
        if s.compone is not None:
            out.append(f"- {s.nome} compone: {', '.join(s.compone)}")
    trovati = 0
    for s in skills:
        lista = chiamate(s, nomi)
        if s.compone is not None:
            lista = [(n, nome) for n, nome in lista if nome not in s.compone]
            motivo = "composta che chiama skill non dichiarate"
        else:
            motivo = "base che chiama altre skill"
        if lista:
            trovati += 1
            dove = ", ".join(f"{nome} (riga {numero})" for numero, nome in lista)
            out.append(f"- {s.nome}: {motivo} → {dove}")
    if not any(s.compone is not None for s in skills) and not trovati:
        out.append("- nessuna composta dichiarata, nessuna chiamata fra skill")
    elif not trovati:
        out.append("- nessuna chiamata fuori dalle composizioni dichiarate")
    out.append("")
    out.append(
        "Limiti: comandi, divieti e chiamate sono candidati estratti dal testo; "
        "la classificazione (vincolo o lacuna, base o composta) resta un giudizio. "
        "Sintassi che somiglia a un segnaposto senza esserlo, come `.#user@host` dei "
        "flake nix, resta fra i comandi."
    )
    return "\n".join(out)


def classifica(root: Path) -> str:
    """Righe di SKILL.md in method e negli adottanti di `world.md`, in ordine."""
    spec = importlib.util.spec_from_file_location("adottanti", root / "o3" / "adottanti.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    repo = {"method": root, **modulo.adottanti(root / "world.md")}
    voci = []
    for nome, checkout in repo.items():
        for s in leggi_skill(checkout):
            voci.append((len(s.righe), nome, s.nome))
    righe = [f"- {nome} {skill} {n}" for n, nome, skill in sorted(voci, reverse=True)]
    return "\n".join(["## Classifica delle skill", "", *righe])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="comando", required=True)
    p_audit = sub.add_parser("audit", help="misure e controlli sulle skill del repo")
    p_audit.add_argument("--root", type=Path, default=Path("."))
    p_class = sub.add_parser("classifica", help="righe delle skill in method e negli adottanti")
    p_class.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args(argv)
    print(audit(args.root) if args.comando == "audit" else classifica(args.root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
