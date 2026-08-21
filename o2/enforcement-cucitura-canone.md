---
sintesi: "Il secondo write-through, nato revisionando il bootstrap di salute, è arrivato ai nodi canonici senza previo passaggio i1: la condizione di risveglio è avverata. Scegliere e costruire il presidio minimo che segnali l'edit trans-repo prima della ratifica."
ciclo: dev
---

# Enforcement della cucitura «agisci attraverso, ratifica in `method`»

## Problema

La disciplina è **dichiarata, non enforced** (cfr. `i3/membrana-afforda-scrittura.md`, filo «La membrana
`method/` afforda scrittura»; recepita in `kb/world.md`). Oggi regge su un solo
presidio: l'agente adottante che, scrivendo un nodo di canone via symlink, **si
accorge** che l'edit non è suo e **si ferma** — come ha fatto `bi`. È un controllo
umano-nel-loop affidato all'attenzione del singolo agente, non una macchina.

Il punto cieco: se un write-through **passasse inosservato**, l'edit di canone
finirebbe committato senza passare per l'i2/i3 di `method` — il canone muterebbe
senza ratifica, e potrebbe rompere silenziosamente gli altri adottanti. Nessun
controllo lo intercetta oggi.

Il 2026-08-21 il segnale di risveglio si è verificato: una sessione in `salute`
ha modificato tre nodi canonici mentre revisionava il componente locale
corrispondente, e il custode ha ricostruito solo a posteriori il mancato
passaggio i1. Il task è quindi attivo.

## Le forme candidate (non ancora scelte)

- **Skill di inizio sessione, speculare a `/commit`** — un gate d'apertura che
  controlla la pulizia/verginità dell'albero prima di iniziare e **segnala
  all'utente** edit di canone non ratificati (orfani nel working tree di `method`,
  o modifiche al symlink `method/` lato adottante). Come `/commit` presidia
  l'uscita, questa presidia l'**ingresso**.
- **Agente che recepisce, dentro il loop agentico** — quando il loop è in campo, un
  agente che intercetta l'edit non ratificato e apre da sé l'arco i1→i2/i3 invece di
  lasciarlo orfano.
- **Check strutturale in `kb_tools.py`** — un controllo che rilevi nodi di canone
  modificati ma non ratificati (eco del `coverage --check` da cui tutto è partito:
  un gate riusabile). Forma più leggera, attivabile da `/commit` o da un pre-commit
  hook.

Le tre non si escludono: la skill d'ingresso e il check sono complementari (segnale
all'utente + gate meccanico); l'agente è l'evoluzione quando il loop matura.

## La lama: repo adottanti multiutente

Oggi l'utente è **uno solo**, e il presidio dell'attenzione basta. La posta sale con
i **repo adottanti multiutente**: lì un write-through di un utente sul canone
condiviso può sfuggire all'attenzione di tutti gli altri, e la coerenza del Mondo-dev
non può più contare sul fatto che «chi scrive è anche chi ratifica». Questo è il
contesto in cui l'enforcement smette di essere secondario e diventa fondante — la
ragione per cui il task esiste ora come pietra miliare anche se non si esegue.

## Scelta da compiere

Il primo presidio deve essere proporzionato ai due episodi osservati e coprire
il momento in cui il contesto è ancora recuperabile. La prescrizione
`o3/revisione-bootstrap-adottante.md` rende esplicito il percorso corretto per
questa classe di revisione, ma non rileva da sola gli altri write-through. Va
quindi confrontata con un check meccanico leggero sul working tree di `method`
all'ingresso e all'uscita della sessione adottante; skill o agente devono
orchestrare quel check, non sostituirlo con un richiamo narrativo.

## Criterio di chiusura

Esiste un presidio dichiarato e funzionante, verificato riproducendo almeno il
caso adottante→symlink→working tree canonico, che intercetta un edit di canone
non ratificato prima che diventi canone-di-record; la cucitura «agisci
attraverso, ratifica in `method`» smette di contare solo sull'attenzione del
singolo agente.
