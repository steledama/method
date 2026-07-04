---
stato: bozza
sintesi: "La cucitura «agisci attraverso la membrana, ratifica in method» è dichiarata (verdict + world.md) ma non enforced: conta sull'agente adottante che si accorge e si ferma, come ha fatto bi. Task trattenuto (|): si costruisce l'enforcement solo quando un write-through passa inosservato — quel mancato accorgersi è il segnale. Critico in ottica repo adottanti multiutente."
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

## Perché `|` (trattenuto), non `—`

Costruire l'enforcement adesso, con un solo episodio e un solo utente, inventerebbe
struttura prima dell'evidenza — l'opposto di come il metodo si sviluppa
(`method-development`). Il muro lo alziamo **noi**, deliberatamente, non il mondo.

**Segnale di risveglio (autoimposto)**: il primo write-through che passa
**inosservato** — un edit di canone committato senza ratifica, scoperto a posteriori.
Quel mancato accorgersi è l'evidenza che la disciplina manuale non scala, e il task
passa da `|` ad attivo. In subordine, lo anticipa l'arrivo di un secondo utente su un
repo adottante (la condizione multiutente sopra).

## Criterio di chiusura

Esiste un presidio dichiarato e funzionante — almeno il segnale all'utente
all'ingresso di sessione, idealmente un check meccanico — che intercetta un edit di
canone non ratificato prima che diventi canone-di-record; la cucitura «agisci
attraverso, ratifica in `method`» smette di contare solo sull'attenzione del singolo
agente.
