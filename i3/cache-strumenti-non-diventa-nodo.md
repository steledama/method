---
ciclo: dev
---

# La cache degli strumenti resta esempio nel canone esistente, non nodo nuovo

Ratificato (2026-07-11), dalla valutazione i2→i3 della percezione «pattern
cache degli strumenti Python replicato in tre adottanti senza nodo canonico»
(catturata da `nixos`, commit `20fbc3f`, consumata da questo filo).

Il segnale osservava che `economia`, `method` e `nixos` avevano convergito
per imitazione diretta sullo stesso schema — `pyproject.toml` minimale che
dirige le cache di `ruff`/`pytest` sotto un'unica cartella locale gitignorata
— senza un nodo `kb/` che lo descrivesse, pur soddisfacendo la soglia dei due
progetti diversi per l'ingresso di un nodo (cfr. CLAUDE.md, «Quando
aggiungere un nodo»).

**Verdetto: non nasce un nodo dedicato.** Il concetto metodologico —
classificare il traffico runtime come superficie di membrana, mai voce
versionata senza classe — era già canone in `project-structure`
(«L'inventario dell'atrio»). Lo schema `pyproject.toml` è l'implementazione
di quel principio per il tooling Python, non un secondo principio: creare un
nodo per ogni ricetta di configurazione strumento avrebbe reso la KB
enciclopedica proprio dove `node.md` mette in guardia. Il bar dei due
progetti (CLAUDE.md) è necessario ma non sufficiente — il concetto deve
anche essere metodologico, non solo replicato.

Trattamento scelto: **rafforzare il nodo esistente**, non crearne uno nuovo
— «aggiornare un nodo esistente quando la nuova informazione rafforza un
concetto già presente» (`kb/node.md`). La voce «traffico runtime» in
`project-structure` guadagna la ricetta collaudata (file di configurazione
minimale, cartella unica gitignorata) come esempio ora validato su tre
adottanti, senza nominare lo strumento specifico (Python-only, non generalizza
ad adottanti non-Python).

Il corollario delle directory vuote (`scripts/`, `tools/` non tracciate,
rimovibili) resta fuori: igiene repo situazionale, non pattern ricorrente —
nessun secondo segnale finora lo corrobora.
