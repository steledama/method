---
data: 2026-06-13
stato: aperto
---

# Migrazione dei nomi-nodo verso l'inglese

I nodi `kb/` stanno migrando gradualmente verso nomi inglesi. È lavoro **finito a
termine**: una lista che si chiude. Per questo vive qui come task e non come
regola permanente in `CLAUDE.md` (una regola sopravviverebbe alla migrazione e
invecchierebbe).

Modo: **rename-on-touch** — quando si modifica un nodo per altri motivi, lo si
rinomina nello stesso colpo, così l'aggiornamento dei backlink si fa una volta
sola insieme alle altre modifiche. La migrazione può anche essere batchata se
conviene. Il task si chiude quando la lista è vuota.

Costo per ogni rename (cfr. `CLAUDE.md`, propagazione): aggiornare l'H1 e le
righe `Connessioni` di tutti i nodi citanti, il catalogo in `README.md`/`kb.md`,
e i link nei `CLAUDE.md`/`README.md` dei repo adottanti. `tools/kb_tools.py` ha
supporto migrazione/backlink da sfruttare.

## Lista (nome attuale → target proposto, da confermare al rename)

- `agente.md` → `agent.md`
- `artefatto-cognitivo.md` → `cognitive-artifact.md`
- `ciclo-azione.md` → `action-cycle.md`
- `confronto-progetti-adottanti.md` → `adopter-comparison.md`
- `connessione.md` → `connection.md`
- `consenso.md` → `consent.md`
- `fedelta-cognitiva.md` → `cognitive-fidelity.md`
- `fonte-di-verita.md` → `source-of-truth.md`
- `indice.md` → `index.md`
- `matrice-ciclo-azione.md` → `action-cycle-matrix.md`
- `nodo.md` → `node.md`
- `osservatorio-metodo.md` → `method-observatory.md`
- `sistema-cognitivo.md` → `cognitive-system.md`
- `strumenti-kb.md` → `kb-tools.md`
- `struttura-progetto.md` → `project-structure.md`
- `sviluppo-metodo.md` → `method-development.md`
- `vincolo.md` → `constraint.md`

Borderline (decidere se toccare): `pattern-karpathy.md` → `karpathy-pattern.md`
("pattern" è uguale nelle due lingue; rename solo se si vuole l'ordine
aggettivo-nome inglese).

Connessioni:

- [nodo](../kb/nodo.md)
- [struttura-progetto](../kb/struttura-progetto.md)
