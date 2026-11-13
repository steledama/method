"""L'ultimo giro del repo e l'ultimo `Prossimo:`, senza scrivere un `git log`.

Le due letture con cui `eval` ed `exec` aprono il giro costavano un diniego
quasi a ogni giro, in quattro repo: la grafia `--grep=^docs(ciclo)` o
`--format=%(trailers:…)` senza virgolette ha parentesi che l'harness nega
(`o3/dinieghi.py`, classe `parentesi`, 13 giri fra il 06 e il 12/11/2026).
La regola c'era già nelle skill, scritta quotata, e l'agente la perdeva
lo stesso. Il custode ha deciso il 2026-10-27 che una ricorrenza dopo il
recepimento chiede uno strumento che renda superflua la grafia, non un'altra
frase (task chiuso il 2026-11-13, in git). Questo è lo strumento: un comando
concesso per nome, senza argomenti da quotare.

Gira nel repo della cartella corrente, in sola lettura. Il giro è l'ultimo
commit con oggetto `docs(ciclo)` e trailer `Esiti:` (la forma di `/cycle`):
un commit di sessione su file del ciclo non lo è. `Prossimo:` è
l'ultimo trailer con quel nome, anche di un commit di sessione. Con
`--corpo` stampa anche il messaggio intero del commit del giro.
"""

from __future__ import annotations

import argparse
import subprocess
import sys

CAMPO, VOCE = "\x1f", "\x1e"
FORMATO = (
    CAMPO.join(
        [
            "%h",
            "%cd",
            "%s",
            "%(trailers:key=Esiti,valueonly,separator=%x20)",
            "%(trailers:key=Prossimo,valueonly,separator=%x20)",
            "%B",
        ]
    )
    + VOCE
)
LIMITE = 500  # commit letti all'indietro


def storia(limite: int = LIMITE) -> list[list[str]]:
    esito = subprocess.run(
        ["git", "log", f"-{limite}", f"--format={FORMATO}", "--date=format:%Y-%m-%d %H:%M"],
        capture_output=True,
        text=True,
        check=False,
    )
    if esito.returncode:
        sys.exit(esito.stderr.strip() or "git log fallito")
    voci = [v.strip("\n") for v in esito.stdout.split(VOCE) if v.strip()]
    return [v.split(CAMPO) for v in voci]


def ultimo(voci: list[list[str]], corpo: bool = False) -> list[str]:
    righe = []
    giro = next((v for v in voci if v[2].startswith("docs(ciclo)") and v[3].strip()), None)
    if giro:
        righe.append(f"giro: {giro[0]} {giro[1]} {giro[2]}")
        if giro[3].strip():
            righe.append(f"Esiti: {giro[3].strip()}")
        if corpo:
            righe += ["", giro[5].strip(), ""]
    else:
        righe.append(f"giro: nessun commit docs(ciclo) con Esiti: negli ultimi {LIMITE}")
    prossimo = next((v for v in voci if v[4].strip()), None)
    if prossimo:
        righe.append(f"Prossimo: {prossimo[4].strip()} ({prossimo[0]} {prossimo[1]})")
    else:
        righe.append(f"Prossimo: nessun trailer negli ultimi {LIMITE} commit")
    return righe


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--corpo", action="store_true", help="messaggio intero del giro")
    args = parser.parse_args(argv)
    print("\n".join(ultimo(storia(), args.corpo)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
