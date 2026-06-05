---
data: 2026-06-05
stato: aperto
---

# Scorporo concettuale: artefatto cognitivo, sistema, due agenti, Goal

Task scorporato da `rifondazione-input-output` per non gonfiarlo: raccoglie i concetti di
quota superiore emersi nelle sessioni 04-06 e 05-06 (vedi `log.md`). Asse: *cosa è* l'oggetto
che il metodo coltiva, distinto dal *come funziona* la struttura i/o.

## Materiale già formulato (in log.md, da portare nei nodi)

- **Tripartizione** (scioglie la sineddoche "KB = metodo"):
  - *artefatto cognitivo* (Norman, *Cognitive Artifacts* 1991) = la rappresentazione esterna
    che si progetta e persiste (KB + strato output + strato input + struttura). È ciò che il
    metodo coltiva; **è portabile** (sopravvive al cambio di modello/harness).
  - *sistema cognitivo* (Hutchins, cognizione distribuita) = artefatto + umano + LLM + harness
    accoppiati. È dove la cognizione accade; non portabile, emerge dall'uso.
  - *metodo* = la pratica con cui si coltiva l'artefatto perché il sistema performi.
- **Argomento decisivo**: la tesi "harness portabile, vendor-neutro" è dicibile solo con
  definizione artefatto-centrica, non sistema-centrica.
- **Ciclo a due agenti**: l'artefatto è letto e rielaborato da una seconda mente (LLM) → il
  ciclo d'azione va riscritto per due agenti che condividono lo stesso system image.
  Asimmetria dei modelli mentali: per l'umano la KB è impalcatura esterna a un modello che già
  possiede; per l'LLM la KB *è* il modello mentale (riparte da zero ogni sessione).
- **Stack a livelli**: L0 modello → L1 harness tecnico (Claude Code/Codex, sostituibile) → L2
  metodo come harness cognitivo portabile e leggibile dall'umano. Norman vive a L2.
- **Gerarchia del Goal** (activity theory): motivo (attività) → goal (azione) → operazione
  (task). `goal`/`task`/`todo` sono tre altitudini, non sinonimi. Deciso: **non** rinominare
  `todo/`→`goals/`; scrivere il *nodo* sul Goal e far emergere l'apparato quando serve.

## Due gerarchie e la relazione genus/species (2026-06-05)

Riflessione che affina la tripartizione e blocca un appiattimento. Stessa sessione del
caso `bi`/1018022.

**Non rinominare L→a.** I tre livelli `L0/L1/L2` (modello → harness → metodo) **non** sono
tre "artefatti" dello stesso tipo: sono un agente, un'infrastruttura e una rappresentazione.
Chiamarli tutti `a0/a1/a2` (artefatto) cancella due distinzioni costate al 04-06: che L0
(LLM) è un *agente*, non un artefatto (l'originalità "l'artefatto che legge" regge solo se
artefatto ≠ agente — materialmente il modello è un oggetto, ma nel sistema cognitivo occupa
il *ruolo* di agente); e che il metodo è la rappresentazione portabile, non un peer
sostituibile dell'agente. Il costo dell'appiattimento è la tesi di portabilità stessa, che
vive nel distinguere *cosa è portabile* (rappresentazione) da *cosa è sostituibile* (agente +
harness). Tenere quindi `L0/L1/L2` come livelli neutri e riservare "artefatto cognitivo" alle
sole KB (rappresentazioni).

**Due gerarchie ortogonali, da non conflare.**

- *(A) Stack di messa-in-opera* = il sistema cognitivo di Hutchins, per sessione: agente
  (LLM, L0) + infrastruttura (harness, L1) + artefatto (l'istanza-di-metodo, L2).
- *(B) Discendenza degli artefatti* = genus → species: il **metodo è il genere** (pattern
  d'artefatto portabile), i progetti `bi`/`salute`/`economia`/`nixos` sono le **specie** (lo
  stesso pattern personalizzato su un dominio). Ognuna è un artefatto cognitivo con i propri
  Goal e i propri cicli d'azione annidati.

Legame fra le due: **L2 in (A) non è una cosa sola — è un *tipo* con istanze, cioè la
gerarchia (B).** Lavorando su `bi`, l'artefatto-L2 nello stack è "la KB di bi" (il genere
istanziato). Auto-riferimento: `metodo` è un artefatto cognitivo *il cui dominio è "costruire
artefatti cognitivi di dominio"* — di secondo ordine, si applica a sé stesso, ed è insieme il
genere **e** una quinta specie su cui si può lavorare.

**Payoff sulla missione del repo.** Il genus/species dà il vocabolario all'osservatorio
cross-repo: il *genere* è ciò che generalizza, i *tratti di specie* sono ciò che resta locale
— la domanda "cosa generalizzare, cosa lasciare locale" del README diventa precisa.

**Due annidamenti diversi, non sovrapporli.** Verticale (tipo → istanza): metodo → progetti
— *di cosa un artefatto è fatto come specie*. Temporale (ciclo → ciclo): sviluppo → runtime,
dentro ogni artefatto — *come un artefatto si produce e si valuta nel tempo* (cfr.
`ciclo-azione`, sezione cicli annidati).

## Nodi candidati

- ✅ `artefatto-cognitivo` → `kb/artefatto-cognitivo.md` (bozza, 2026-06-05)
- ✅ `sistema-cognitivo` → `kb/sistema-cognitivo.md` (bozza, 2026-06-05) — asimmetria dei
  modelli mentali, tripartizione artefatto/sistema/metodo; manca fonte primaria Hutchins
- `goal` (nuovo, gerarchia dell'azione)
- `ciclo-azione` (riscritto come ciclo a due agenti) — **cerniera con
  `rifondazione-input-output`**: coordinare con la conversione L→o/i, stessa passata sul nodo

## Connessioni

- [rifondazione-input-output](rifondazione-input-output.md)
- [ciclo-azione](../kb/ciclo-azione.md)
- [ingest-norman](ingest-norman.md)
