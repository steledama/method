---
data: 2026-06-21
stato: attiva
target: nixos, bi, economia, salute (round 1 della propagazione del cluster)
---

# Disaccoppiamento adottante↔metodo: dichiara e taci

## Cosa e perché

Il canone ruota: i nodi cambiano nome o si scompongono mentre il metodo
matura. Finché un adottante replica nei propri file un **inventario** dei path
interni del metodo, ogni rotazione si propaga come una bonifica diffusa su
`CLAUDE.md`, `README.md` e nodi locali. È coupling alla **struttura interna** del
canone, non alla sua **interfaccia**.

La regola che scioglie il nodo è **dichiara e taci** (`method-development`, «Il
confine canone↔adottante»): l'adottante dichiara _una volta_ l'adozione del
metodo come insieme, e altrove collega solo ciò da cui il proprio contenuto
dipende davvero. Questo runbook porta ogni adottante a (a) adottare la **sezione
README canonica** come unico luogo della dipendenza generale, e (b) classificare
i link residui al metodo, tenendo gli intenzionali e rimuovendo gli accidentali.

È il **round 1** della propagazione del cluster: riduce i riferimenti
accidentali _prima_ del round 2 (rename `deck→view`, task successivo), così quel
rename toccherà solo le connessioni intenzionali rimaste. La metrica non è «zero
link» ma **«zero link senza funzione locale»**.

## La ricetta (nel lessico del metodo)

1. **Adotta la sezione README canonica.** Porta il README del repo alla forma di
   `kb/readme.md`: heading fissi e machine-readable `## Metodo` (dichiarazione di
   adozione + symlink `method/` + hub `cognitive-artifact-design.md`), `### Goal`
   (il motivo del dominio, in sintesi) e `### World` (i riferimenti **espliciti**
   al Mondo runtime — fonti di verità, **mai** derivati per euristica dal remote).
   È la dichiarazione _una-volta_ della dipendenza generale.
2. **Classifica ogni link al metodo per grado di dipendenza.** Per ogni `method/<nodo>.md`
   nei file del repo decidi a quale dei tre gradi appartiene:
   - **generale** — l'adozione come tale: deve vivere solo nella sezione canonica;
     altrove è ridondante.
   - **intenzionale** (tieni) — link che esprime una dipendenza **semantica** o
     **operativa** reale: un nodo locale che àncora il proprio concetto a uno del
     metodo, una regola/strumento locale che rimanda alla propria specifica
     canonica, un task che usa un nodo come vincolo o contesto necessario.
   - **accidentale** (rimuovi) — inventari diffusi dei nodi del metodo, elenchi
     orientativi che duplicano l'hub, richiami aggiunti solo per dire genericamente
     «questa regola viene dal metodo», path interni copiati in più file senza una
     funzione locale distinta.
3. **Riscrivi `CLAUDE.md`.** È il covo tipico dell'inventario: liste di
   «Riferimenti metodo: …» e «Approfondimento: `method/<nodo>.md`» ripetute. Dove
   il rimando è solo decorativo, rimuovilo o sostituiscilo con l'aggancio all'hub;
   tieni il link solo dove la regola locale dipende da quella specifica.
4. **Verifica l'assenza di rotture.** Dopo la bonifica: `kb-review` (audit
   strutturale, niente link rotti) e una ricerca globale che non trovi più
   inventari duplicati né path orfani.

## Touchpoint per-repo (indizi da verificare in loco, non ordini)

Il modello che `method` ha di ciascun repo è una fotografia dell'osservatorio e
può derivare (`cognitive-fidelity`): l'**ultimo miglio** — quali link tenere,
riscrivere o rimuovere — lo fa il `method-review` dell'adottante contro lo stato
reale del proprio repo.

- **`nixos`** — accidentale sospetto: in `CLAUDE.md` la serie ripetuta
  «Approfondimento: `method/skill.md`» sotto i comandi e la coda «principi guida:
  `method/design-principles.md`» / «cognitive artifact design e fedeltà: …».
  Intenzionali plausibili da **tenere**: `kb/home-manager.md` e
  `kb/unfree-packages.md` che àncorano un principio locale a `design-principles`;
  `kb/development-workflow.md` e `verdict.md` che rimandano a `verdict` come forma
  canonica. Da valutare i link `kb-tools`/`design-principles` nel README.
- **`bi`** — accidentale netto: in `CLAUDE.md` la riga-inventario «Riferimenti
  metodo: `method/cognitive-artifact-design.md`, `method/node.md`,
  `method/connection.md`, `method/kb-tools.md`» e la serie «approfondimento:
  `method/skill.md`». Intenzionali plausibili da **tenere**: `map.md` →
  `output.md`/`input.md` (semantico, i tre livelli o1/o2/o3 del dominio),
  `method-review.md` → `world.md` (operativo). Da valutare l'entry `design-principles`
  in `kb.md` (catalogo) e i link nel README.
- **`economia`** — verifica in loco: la sezione metodo dovrebbe già dichiarare il
  repo trans-repo invece di indicizzare i singoli nodi (cfr. `readme` § Applicazione);
  porta quella dichiarazione alla forma canonica `## Metodo`/`### Goal`/`### World`
  e classifica i link residui.
- **`salute`** — verifica in loco: README lungo e narrativo con pointer espliciti;
  conserva i pointer **intenzionali** ai nodi-ponte locali, isola la dipendenza
  generale nella sezione canonica.

## Chiusura

La prescrizione resta attiva finché tutti e quattro gli adottanti non l'hanno
recepita via il proprio `method-review`. Recepita, si rimuove dalla collezione e
si aggiorna `verdict.md`; la storia resta in Git. Solo allora il task #1 chiude e
il rename `deck→view` del task #2 può propagare senza una nuova bonifica generale.
