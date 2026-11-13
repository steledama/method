"""Controllo di scadenze e ricorrenze: il contratto di `kb/plan.md`, deterministico.

Legge `o1/plan.md` del repo da cui è lanciato e stampa:

- la catena cronologica di `## Scadenze` e `## Ricorrenze`. Una ricorrenza è
  `dovuta` dalla data raggiunta e `saltata` quando è passata anche la data più
  una cadenza. Una data passata in `## Scadenze` e un `entro` passato in
  `## Ricorrenze` contano come scaduti; l'orologio nostro passato no. I `by:` in
  arrivo entrano nella catena come riesami, senza contare come scadenze;
- i rilievi di forma: ogni voce delle due sezioni è una data interpretata o un
  rilievo col suo testo, mai uno scarto in silenzio;
- le attese a finestra (`!`), a ogni esecuzione e senza condizione di distanza;
- i riesami: i `by:` passati delle chiose, che non sono scadenze.

È un segnale, non un gate: esce con 1 se c'è una scaduta, con 2 se non riesce a
leggere plan o profilo, altrimenti con 0. Non valuta le `probe:` e non prende
comandi dal plan.

Un adottante lo lancia dal checkout del canone, nella radice del proprio repo:
`python3 method/../o3/scadenze.py`. Il profilo locale `o3/scadenze.toml` è
opzionale e riguarda solo la forma delle righe di `## Scadenze`:

    formati_data = ["it"]               # oltre a iso: 9/12/26, nov 2027
    marcatori_chiusura = ["eseguito"]   # riga fatta, da togliere dal plan

La grammatica di `Prossima`, cadenze e legenda coincide con quella di
`o3/view/sources.py`: lo verifica `tests/test_scadenze.py`, perché lo strumento
non dipende dai builder delle viste.
"""

from __future__ import annotations

import argparse
import calendar
import re
import sys
import tomllib
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

PLAN = Path("o1/plan.md")
PROFILO = Path("o3/scadenze.toml")
FINESTRA = 45

# Un intervallo in giorni o in mesi di calendario, che non hanno durata fissa.
CADENZE: dict[str, timedelta | int] = {
    "quotidiano": timedelta(days=1),
    "settimanale": timedelta(weeks=1),
    "mensile": 1,
    "trimestrale": 3,
    "semestrale": 6,
    "annuale": 12,
    "biennale": 24,
}
COLONNE_RICORRENZE = 5
PROSSIMA = re.compile(r"(entro )?(\d{4})-(\d{2})(?:-(\d{2}))?")
LEGENDA = re.compile(r"^\s*[-*]\s+[*`]*([wp]\d+)!?[*`]*\s*[—–:→·-]", re.MULTILINE)
INDICE = re.compile(r"\b([wp]\d+)(!?)(?![\w])")
BY = re.compile(r"\bby:(?:\*\*)?\s*(\d{4})-(\d{2})(?:-(\d{2}))?(?![\d-])")
LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")

_TESTA = r"^- (?:\*\*)?(?P<entro>entro )?"
_CODA = r"(?P<nota>[^—→]*?)\s*[—→]\s*(?P<testo>.*)$"
_ISO = r"(?P<anno>\d{4})-(?P<mese>\d{2})(?:-(?P<giorno>\d{2}))?(?![\d-])"
_GIORNI_IT = r"(?:(?:lun|mar|mer|gio|ven|sab|dom) )?"
_MESI_IT = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
_IT = (
    rf"{_GIORNI_IT}(?:(?P<giorno>\d{{1,2}})/(?P<mese>\d{{1,2}})/(?P<anno>\d{{4}}|\d{{2}})(?![\d/])"
    rf"|(?P<nome_mese>{'|'.join(_MESI_IT)}) (?P<anno_mese>\d{{4}})(?!\d))"
)


class ErroreProfilo(ValueError):
    """Un profilo che non si sa leggere ferma lo strumento, non si ignora."""


def _giorno(anno: int, mese: int, giorno: int | None) -> date:
    """Il solo mese vale come il suo ultimo giorno (`kb/plan.md`)."""
    return date(anno, mese, giorno or calendar.monthrange(anno, mese)[1])


def _campi_iso(m: re.Match[str]) -> tuple[int, int, int | None]:
    giorno = m["giorno"]
    return int(m["anno"]), int(m["mese"]), int(giorno) if giorno else None


def _campi_it(m: re.Match[str]) -> tuple[int, int, int | None]:
    if m["nome_mese"]:
        return int(m["anno_mese"]), _MESI_IT.index(m["nome_mese"]) + 1, None
    anno = int(m["anno"])
    return anno + 2000 if anno < 100 else anno, int(m["mese"]), int(m["giorno"])


FORMATI: dict[str, tuple[re.Pattern[str], Callable[..., tuple[int, int, int | None]]]] = {
    "iso": (re.compile(_TESTA + _ISO + _CODA), _campi_iso),
    "it": (re.compile(_TESTA + _IT + _CODA), _campi_it),
}


@dataclass(frozen=True)
class Profilo:
    formati: tuple[str, ...] = ("iso",)
    marcatori_chiusura: tuple[str, ...] = ()


def leggi_profilo(path: Path) -> Profilo:
    if not path.exists():
        return Profilo()
    try:
        dati = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as errore:
        raise ErroreProfilo(f"{path}: {errore}") from errore
    ignote = dati.keys() - {"formati_data", "marcatori_chiusura"}
    if ignote:
        raise ErroreProfilo(f"{path}: chiavi sconosciute {sorted(ignote)}")
    formati = dati.get("formati_data", [])
    sconosciuti = [formato for formato in formati if formato not in FORMATI]
    if sconosciuti:
        raise ErroreProfilo(f"{path}: formati di data sconosciuti {sconosciuti}")
    marcatori = tuple(marcatore.lower() for marcatore in dati.get("marcatori_chiusura", []))
    return Profilo(("iso", *(f for f in formati if f != "iso")), marcatori)


@dataclass(frozen=True)
class Voce:
    """Una riga datata della catena; solo le ricorrenze hanno una cadenza."""

    data: date
    testo: str
    cadenza: str | None = None
    solo_mese: bool = False
    entro: bool = True
    chiusa: bool = False

    def _dopo(self, cadenze: int) -> date:
        """La data più `cadenze` intervalli: col solo mese resta a fine mese."""
        passo = CADENZE[self.cadenza or ""]
        if isinstance(passo, timedelta):
            return self.data + passo * cadenze
        mesi = self.data.year * 12 + self.data.month - 1 + passo * cadenze
        anno, mese = mesi // 12, mesi % 12 + 1
        ultimo = calendar.monthrange(anno, mese)[1]
        return date(anno, mese, ultimo if self.solo_mese else min(self.data.day, ultimo))

    def occorrenze_perse(self, oggi: date) -> int:
        perse = 0
        while oggi > self._dopo(perse + 1):
            perse += 1
        return perse

    def _stato_ricorrenza(self, oggi: date) -> str:
        perse = self.occorrenze_perse(oggi)
        stato = f"saltata ({perse})" if perse else "dovuta"
        return f"SCADUTA; {stato}" if self.entro and self.data < oggi else stato

    def stato(self, oggi: date, finestra: int) -> str | None:
        """Lo stato da stampare, `None` se la voce è oltre la finestra."""
        if self.chiusa and self.data <= oggi:
            return "CHIUSA_DA_ARCHIVIARE"
        distanza = (self.data - oggi).days
        if self.cadenza and distanza <= 0:
            return self._stato_ricorrenza(oggi)
        if distanza < 0:
            return "SCADUTA"
        if distanza == 0:
            return "OGGI"
        return f"{distanza} giorni" if distanza <= finestra else None

    def scaduta(self, oggi: date, finestra: int) -> bool:
        stato = self.stato(oggi, finestra) or ""
        return stato.startswith(("SCADUTA", "CHIUSA_DA_ARCHIVIARE"))


@dataclass(frozen=True)
class Lettura:
    voci: list[Voce]
    rilievi: list[tuple[str, str]]
    config: int


def _sezione(testo: str, titolo: str) -> list[str]:
    righe: list[str] = []
    dentro = False
    for riga in testo.splitlines():
        if riga.startswith("## "):
            dentro = riga.rstrip() == titolo
        elif dentro:
            righe.append(riga)
    return righe


def _voci_elenco(righe: list[str]) -> list[str]:
    """Unisce ogni bullet alle sue continuazioni: il formatter va a capo ovunque."""
    voci: list[list[str]] = []
    aperta = False
    for riga in righe:
        if riga.startswith("- "):
            voci.append([riga])
            aperta = True
        elif aperta and riga.startswith("  "):
            voci[-1].append(riga)
        elif riga.strip():
            aperta = False
    return [" ".join(parte.strip() for parte in voce) for voce in voci]


def _celle(riga: str) -> list[str]:
    return [cella.strip() for cella in riga.strip().strip("|").split("|")]


def _separatore(celle: list[str]) -> bool:
    return not set("".join(celle)) - set("-: ")


def _voce_scadenza(testo: str, profilo: Profilo) -> Voce | None:
    for formato in profilo.formati:
        modello, campi = FORMATI[formato]
        trovata = modello.match(testo)
        if not trovata:
            continue
        anno, mese, giorno = campi(trovata)
        try:
            data = _giorno(anno, mese, giorno)
        except ValueError:
            return None
        chiusa = any(marcatore in testo.lower() for marcatore in profilo.marcatori_chiusura)
        return Voce(data, trovata["testo"].strip(), solo_mese=giorno is None, chiusa=chiusa)
    return None


def leggi_scadenze(testo: str, profilo: Profilo) -> tuple[list[Voce], list[tuple[str, str]]]:
    voci: list[Voce] = []
    rilievi: list[tuple[str, str]] = []
    for riga in _voci_elenco(_sezione(testo, "## Scadenze")):
        voce = _voce_scadenza(riga, profilo)
        if voce is None:
            rilievi.append(("RIGA_NON_RICONOSCIUTA", riga))
            continue
        if voci and voce.data < voci[-1].data:
            rilievi.append(("FUORI_ORDINE", riga))
        voci.append(voce)
    return voci, rilievi


def _voce_ricorrenza(celle: list[str]) -> Voce | None:
    prossima, cadenza, esecutore, _, titolo = celle
    trovata = PROSSIMA.fullmatch(prossima)
    if not trovata or cadenza not in CADENZE:
        return None
    entro, anno, mese, giorno = trovata.groups()
    try:
        data = _giorno(int(anno), int(mese), int(giorno) if giorno else None)
    except ValueError:
        return None
    nome = LINK.sub(r"\1", titolo)
    return Voce(
        data,
        f"{nome} ({cadenza}, {esecutore})",
        cadenza=cadenza,
        solo_mese=giorno is None,
        entro=bool(entro),
    )


def leggi_ricorrenze(testo: str) -> tuple[list[Voce], list[tuple[str, str]], int]:
    voci: list[Voce] = []
    rilievi: list[tuple[str, str]] = []
    config = 0
    for riga in _sezione(testo, "## Ricorrenze"):
        if not riga.startswith("|"):
            continue
        celle = _celle(riga)
        if celle[0] == "Prossima" or _separatore(celle):
            continue
        if len(celle) == COLONNE_RICORRENZE and celle[0] == "config":
            config += 1
            continue
        voce = _voce_ricorrenza(celle) if len(celle) == COLONNE_RICORRENZE else None
        if voce is None:
            rilievi.append(("RIGA_NON_RICONOSCIUTA", riga.strip()))
        else:
            voci.append(voce)
    return voci, rilievi, config


def leggi(testo: str, profilo: Profilo) -> Lettura:
    scadenze, rilievi_scadenze = leggi_scadenze(testo, profilo)
    ricorrenze, rilievi_ricorrenze, config = leggi_ricorrenze(testo)
    return Lettura(scadenze + ricorrenze, rilievi_scadenze + rilievi_ricorrenze, config)


def righe_task(testo: str) -> list[tuple[str, str]]:
    """Coppie (task, dipendenza) dalla tabella con le colonne `Task` e `Dip.`."""
    colonne: tuple[int, int] | None = None
    coppie: list[tuple[str, str]] = []
    for riga in testo.splitlines():
        if not riga.startswith("|"):
            colonne = None
            continue
        celle = _celle(riga)
        if colonne is None:
            if "Task" in celle and "Dip." in celle:
                colonne = celle.index("Task"), celle.index("Dip.")
            continue
        if not _separatore(celle) and len(celle) > max(colonne):
            coppie.append((celle[colonne[0]], celle[colonne[1]]))
    return coppie


def finestre(testo: str) -> list[tuple[str, str]]:
    """Le attese marcate `!`: nessuna data le farebbe emergere."""
    return [
        (f"{indice}!", task)
        for task, dipendenza in righe_task(testo)
        for indice, marcato in INDICE.findall(dipendenza)
        if marcato
    ]


@dataclass(frozen=True)
class Attesa:
    """La chiosa di una `w` o di una `p`, col suo termine di riesame."""

    indice: str
    task: str
    by: date | None
    by_illeggibile: bool
    risveglio: bool

    def rilievo(self) -> str | None:
        if self.indice.startswith("w") and not self.risveglio:
            return "SENZA_PROBE_NE_ARRIVAL"
        if self.by_illeggibile:
            return "BY_NON_VALIDO"
        return "SENZA_BY" if self.by is None else None


def _by(corpo: str) -> tuple[date | None, bool]:
    trovato = BY.search(corpo)
    if trovato is None:
        return None, "by:" in corpo
    anno, mese, giorno = trovato.groups()
    try:
        return _giorno(int(anno), int(mese), int(giorno) if giorno else None), False
    except ValueError:
        return None, True


def attese(testo: str) -> list[Attesa]:
    titoli: dict[str, str] = {}
    for task, dipendenza in righe_task(testo):
        for indice, _ in INDICE.findall(dipendenza):
            titoli.setdefault(indice, task)
    trovate: list[Attesa] = []
    for riga in _voci_elenco(testo.splitlines()):
        chiosa = LEGENDA.match(riga)
        if chiosa is None:
            continue
        indice = chiosa[1]
        by, illeggibile = _by(riga)
        risveglio = "probe:" in riga or "arrival:" in riga
        trovate.append(Attesa(indice, titoli.get(indice, "—"), by, illeggibile, risveglio))
    return trovate


def _blocco(titolo: str, righe: list[str]) -> str:
    return "\n".join(["", titolo, "", *righe]) + "\n" if righe else ""


def _riesami_in_arrivo(testo: str, oggi: date, finestra: int) -> list[tuple[date, str]]:
    """I `by:` entro la finestra: restano date nostre, non contano come scadenze."""
    arrivo: list[tuple[date, str]] = []
    for attesa in attese(testo):
        if attesa.by is None or not 0 <= (attesa.by - oggi).days <= finestra:
            continue
        distanza = (attesa.by - oggi).days
        quando = f"fra {distanza} giorni" if distanza else "oggi"
        nome = attesa.indice if attesa.task == "—" else f"{attesa.indice} · {attesa.task}"
        arrivo.append((attesa.by, f"- riesame {quando} — {attesa.by.isoformat()} — {nome}"))
    return arrivo


def rapporto(testo: str, profilo: Profilo, oggi: date, finestra: int) -> tuple[str, bool]:
    lettura = leggi(testo, profilo)
    catena = [
        (voce.data, f"- {stato} — {voce.data.isoformat()} — {voce.testo}")
        for voce in lettura.voci
        if (stato := voce.stato(oggi, finestra)) is not None
    ]
    catena += _riesami_in_arrivo(testo, oggi, finestra)
    if catena:
        righe = [riga for _, riga in sorted(catena, key=lambda coppia: coppia[0])]
        uscita = "\n".join([f"Catena entro {finestra} giorni da {oggi.isoformat()}:", "", *righe])
        uscita += "\n"
    else:
        uscita = f"Nessuna voce entro {finestra} giorni da {oggi.isoformat()}.\n"
    uscita += _blocco(
        "Rilievi di forma, non toccano il codice di uscita:",
        [f"- {tipo} — {riga}" for tipo, riga in lettura.rilievi],
    )
    uscita += _blocco(
        "Attese a finestra, l'opzione può chiudersi senza preavviso:",
        [f"- {indice} — {task}" for indice, task in finestre(testo)],
    )
    riesami: list[str] = []
    for attesa in attese(testo):
        rilievo = attesa.rilievo()
        if rilievo:
            riesami.append(f"- {rilievo} — {attesa.indice} — {attesa.task}")
        elif attesa.by is not None and attesa.by < oggi:
            riesami.append(
                f"- RIESAME — {attesa.indice} — by {attesa.by.isoformat()} — {attesa.task}"
            )
    uscita += _blocco("Attese da riesaminare, i termini non sono scadenze:", riesami)
    uscita += (
        f"\nLette: {len(lettura.voci)} voci datate, {lettura.config} config, "
        f"{sum(tipo == 'RIGA_NON_RICONOSCIUTA' for tipo, _ in lettura.rilievi)} non riconosciute.\n"
    )
    return uscita, any(voce.scaduta(oggi, finestra) for voce in lettura.voci)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Controllo di scadenze e ricorrenze del plan")
    parser.add_argument("--plan", type=Path, default=PLAN)
    parser.add_argument("--profilo", type=Path, default=PROFILO)
    parser.add_argument("--today", type=date.fromisoformat, default=date.today())
    parser.add_argument("--days", type=int, default=FINESTRA)
    args = parser.parse_args(argv)
    try:
        testo = args.plan.read_text(encoding="utf-8")
        profilo = leggi_profilo(args.profilo)
    except (OSError, ErroreProfilo) as errore:
        print(f"scadenze: {errore}", file=sys.stderr)
        return 2
    uscita, scaduta = rapporto(testo, profilo, args.today, args.days)
    # Su Windows lo stdout rediretto non è UTF-8 e le frecce del plan romperebbero.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(uscita, end="")
    return 1 if scaduta else 0


if __name__ == "__main__":
    raise SystemExit(main())
