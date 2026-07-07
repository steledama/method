---
ciclo: runtime
---

# Segnale: una modifica di canone nata in un adottante, scritta via symlink

Data: 2026-06-23 · Fonte: `bi` (origine del segnale), risolvendo un problema
concreto di filing back

## Il segnale

Operando in `bi` su un problema concreto — rendere la copertura documentale degli
script un **gate bloccante** per `/commit` (il flag `coverage --check`, exit
non-zero se uno script non ha nodo `kb/<nome>.md`) — è emersa una generalizzazione
portabile: il `--check` non è specifico di `bi`, appartiene allo strato portabile
di `kb_tools.py` e riusabile da `/commit` e da un git pre-commit hook in qualunque
adottante. Documentandola, l'agente in `bi` ha aggiornato il nodo
[`kb-tools`](../kb/kb-tools.md) — che vive in `method` e che `bi` vede **via
symlink** `method/`.

Sopra al contenuto, l'episodio porta un secondo segnale, di natura propriamente
metodologica, ed è il più interessante: **l'agente si è accorto che la modifica
non compariva nel diff del proprio commit**, ha indagato e ha chiesto come
comportarsi. Quel «non compare nel mio diff» è la firma esatta del fatto che il
file modificato non è di `bi`: è il nodo canonico in `method`, raggiunto in
scrittura attraverso il symlink.

## L'attrito osservato

Il canone descrive il canale `world`/`method/` come **lettura**: gli adottanti
«leggono i nodi» (cfr. `README`, `project-structure`). L'episodio mostra che lo
stesso symlink è anche una **superficie di scrittura**: un agente che risolve un
problema in un adottante può modificare il canone direttamente, senza passare per
i tempi del dal-basso canonico (stabilizzazione locale → segnale i1 →
valutazione i2/i3 **qui**, dove si decide se generalizza e se rompe gli altri tre
adottanti).

Conseguenze osservate, valenza-neutre:

- la modifica è atterrata sul nodo **prima** della sua cattura i1 e della
  valutazione: al momento è un cambiamento orfano nel working tree di `method`
  (`M kb/kb-tools.md`), non sorzato e non committato;
- il diff porta già una **generalizzazione implicita**: `--check` è stato scritto
  nello strato portabile (lo possono usare tutti), mentre la riga `bi`-specifica
  registra che solo `bi` l'ha cablato come gate bloccante;
- l'agente in `bi` ha **fermato e chiesto** invece di committare oltre: il
  riconoscimento dell'anomalia è arrivato dall'agente stesso, non da un controllo
  del metodo.

## Da valutare (i2→i3, non ancora verdetto)

Aperto, da sciogliere in `method`:

1. la modifica al nodo `kb-tools` generalizza? (apparentemente sì: il `--check`
   portabile è già scritto come tale) — e per gli altri tre adottanti l'esito è
   adozione o «non applicabile» (come si chiuse la prescrizione _baricentro_)?
2. il segnale metodologico più largo: il canale `world` è **bidirezionale**. Va
   dichiarato come tale e dotato di una disciplina nominata — una modifica di
   canone nata in un adottante back-filla una perception e passa per i2/i3 in
   `method` prima di essere committata qui? È il protocollo che l'agente di `bi`
   ha eseguito a mano.
3. è il primo arco runtime→dev **bottom-up** che attraversa il symlink (finora
   l'unico scoccato era top-down: il _baricentro_ su `salute`): evidenza nuova per
   il filo `development-meta-cycle`/`runtime-o1` e per l'osservatorio nascente.

## Esito

Valutato e formalizzato. Cfr. `verdict.md`, filo «La membrana `method/` afforda
scrittura: agisci attraverso, ratifica in `method`». L'i2 ha riformulato il segnale
come gap **affordance↔signifier** (il symlink afforda scrittura, il canone significava
lettura) e ha localizzato la perdita sui nodi-strumento con sezioni per-adottante. L'i3
ha inciso la disciplina «agisci attraverso la membrana, ratifica in `method`» (il
write-through è atto runtime legittimo; il gate trattiene solo il commit del nodo di
canone), recepita in `world.md`. La riga `kb-tools` è ratificata come generalizzata e
diventa committabile; il nodo nuovo è tenuto in riserva (un solo episodio). Aggiornato il
rilievo di collocazione: è la gamba **bottom-up** del ciclo runtime, non evidenza per
`runtime-o1` (top-down).
