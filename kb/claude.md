---
stato: bozza
---

# CLAUDE

CLAUDE.md è la costituzione operativa del progetto per gli agenti. Risponde alla domanda: come devo agire in questo repo? Contiene regole d'azione, vincoli, permessi, procedure sicure e riferimenti rapidi; non contiene conoscenza stabile del dominio.

La distinzione è essenziale. Se CLAUDE.md spiega come funziona il sistema, diventa documentazione narrativa e compete con la KB. Se invece resta costituzione operativa, può essere caricato spesso senza gonfiare il contesto e senza creare una seconda fonte di verità.

Regole:

- apre con il bootstrap di sessione esplicito: ordine di lettura `README → CLAUDE → nodo` (`CLAUDE.md` è già in contesto; i cataloghi trasversali e i register, incluso `map` dove esiste, si aprono on-demand)
- contiene comportamenti consentiti, proibiti o da chiedere
- include il controllo iniziale sui task aperti quando il progetto usa `plan.md` + tasks/
- nei repo adottanti, può ricordare di controllare la storia recente di `method`
  quando serve recepire generalizzazioni portabili, ma non deve trattare
  `../method/tasks/` come backlog operativo locale
- indica operativamente gli strumenti: quale usare per quale intento, con i
  comandi minimi ad alta frequenza
- può elencare i comandi quotidiani ad alta frequenza (formatter, validazione locale, entry point KB) ma rimanda alla KB per la reference completa
- rimanda ai nodi KB per architettura, procedure e spiegazioni stabili
- chiude con un elenco "Riferimenti rapidi" che mappa intenti operativi ai nodi KB
- preferisce elenchi puntati alle tabelle markdown per confronti, riferimenti e
  liste di voci, perché le tabelle diventano illeggibili su schermi stretti;
  restano ammesse le forme intrinsecamente tabulari, come `plan.md`, matrici di
  lookup e dati numerici nei quali la conversione perderebbe informazione
- non è fonte di fatti per audit o fedeltà cognitiva
- la dimensione è un segnale: oltre ~100 righe è probabile sovrapposizione con la KB, e il contenuto in eccesso va trasferito nei nodi tematici

## Applicazione nei progetti adottanti

- **`nixos`** — situazione attuale: bootstrap esplicito, permessi, validazione, formatter, vincoli e riferimenti rapidi. Confronto con il metodo: molto vicino alla teoria — file operativo, compatto e non usato come fonte di verità del dominio.
- **`bi`** — situazione attuale: revisione completata dopo la fotografia iniziale: `CLAUDE.md` compattato e task locale di dettaglio chiuso. Confronto con il metodo: sotto monitoraggio qualitativo — il criterio resta che `CLAUDE.md` deve essere costituzione operativa, non manuale di dominio.
- **`economia`** — situazione attuale: bootstrap con `stato.md`, `scadenze.md` e mappa, comandi, risorse esterne e riferimenti rapidi. Confronto con il metodo: buon adattamento — include vincoli di dominio e stato corrente senza trasformarsi in manuale esteso.
- **`salute`** — situazione attuale: il più esteso: project overview, filosofia, struttura, guidelines e operazioni; ora rimanda a `kb/verifica-nel-vivere.md` per il filing back. Confronto con il metodo: eredita la fase storica del progetto — utile, ma può alleggerirsi progressivamente usando pointer verso `metodo/` e nodi locali.

Il caso `bi` ha mostrato perché il metodo insiste sulla separazione tra costituzione operativa e documentazione. Più `CLAUDE.md` diventa completo, più diventa costoso da caricare e più rischia di divergere dai nodi. La regola pratica è: se un paragrafo spiega come funziona il sistema, appartiene a `kb/`; se dice cosa l'agente può o deve fare, appartiene a `CLAUDE.md`.

La preferenza per gli elenchi è emersa bottom-up in `nixos`: la conversione di
`CLAUDE.md` e `map.md` ha risolto un problema concreto di lettura su schermi
stretti. Il criterio è stato poi generalizzato in `method`, applicato ai
confronti nella KB e infine propagato nei `CLAUDE.md` e nella documentazione dei
quattro progetti adottanti. Le eccezioni conservate durante la propagazione
chiariscono il confine: il problema non è la sintassi tabellare in sé, ma usarla
per contenuti discorsivi o comparativi che un elenco rende riflowable senza
perdita.

Per gli strumenti, CLAUDE.md è il livello operativo della tripartizione README/CLAUDE/nodi descritta in `kb-tools`: dice quando usare uno strumento, quali comandi minimi sono sicuri e quando leggere il nodo di dettaglio; la reference estesa resta nei nodi o negli script versionati.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [agents](agents.md)
- [readme](readme.md)
- [project-structure](project-structure.md)
- [skill](skill.md)
- [kb-tools](kb-tools.md)
