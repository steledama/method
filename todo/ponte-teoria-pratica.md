---
data: 2026-05-24
stato: aperto
---

# Ponte teoria-pratica (strato output universale)

Formalizzare lo strato di OUTPUT come funzione cognitiva universale del metodo, finora implicita ma presente in tutti i progetti adottanti. Aggiungere Donald Norman come terzo gigante del metodo accanto a Luhmann (Zettelkasten) e Karpathy (LLM KB).

## Contesto

La sessione del 24/5/2026 (vedi `log.md`) ha riconosciuto che ogni progetto adottante ha un suo strato di output (`nixos/{home,hosts,modules}/`, `bi/presentazione/`, `economia/output/`) ma il metodo non lo nomina. `salute` è il caso più chiaro: in assenza di uno strato dedicato, la pressione di sintesi sta deformando i nodi della KB (es. `storia-clinica.md`, diventato di fatto un dashboard improprio).

Tre formulazioni nuove emerse nella sessione, da stabilizzare in nodi metodologici:

1. La sintesi vive nello strato output, non nei nodi. **Lo strato output esiste perché il KB possa restare puro** — risolve il conflitto implicito Zettelkasten/Karpathy.
2. L'output ha tre livelli: L1 macchina, L2 decisione umana, L3 azione nel mondo. L3 ritorna come fonte chiudendo il ciclo.
3. Donald Norman fornisce il fondamento teorico per L2 via il ciclo di azione, i due gulf, le quattro proprietà cardine.

## Dipendenze

Pilota in `salute/quadro/` (vedi `salute/todo/quadro-corporeo.md`). La formalizzazione nasce dopo l'evidenza empirica. Astrarre prima dell'applicazione è la trappola classica della metodologia fine a se stessa.

## Nodi da creare

### `kb/ponte.md` — lo strato output

- Definizione: livello distinto dal KB, dedicato alla traduzione conoscenza → azione possibile
- Risoluzione del conflitto Zettelkasten/Karpathy: la sintesi vive nello strato output, non nei nodi
- I tre livelli L1/L2/L3 con definizione, audience, esempi dai quattro progetti adottanti
- Il ciclo chiuso: L3 ritorna come fonte (generalizzazione del "filing back" di Karpathy)
- Tabella di stato dei quattro progetti adottanti con forma locale e completezza dei tre livelli
- Raccomandazione: ogni progetto dichiara esplicitamente la sua forma per L1, L2, L3 (alcuni livelli possono essere assenti, ma vanno nominati)

### `kb/ciclo-azione.md` — fondamento teorico via Norman

- Non è biografia di Norman: è distillazione metodologica, come `pattern-karpathy.md` non è biografia di Karpathy
- Modello dei sette stadi: Goal → Plan → Specify → Perform → Perceive → Interpret → Compare
- I due gulf: execution (volere → fare) e evaluation (esito → comprendere)
- Le quattro proprietà cardine (visibilità, feedback, mapping, constraint) come criteri di qualità per L2
- "L'errore umano come errore di design": se l'utente non agisce, la KB è mal progettata
- Il gulf of execution come metrica della distanza tra "so cosa fare" e "lo faccio"

## Aggiornamenti collaterali

- `kb/confronto-progetti-adottanti.md`: promuovere l'output da "componente locale aggiuntivo" a "componente universale con forme locali"
- `kb/metodo-kb.md`: citare esplicitamente i tre giganti (Luhmann, Karpathy, Norman)
- `kb/mappa.md`: integrare lo strato output come dimensione della mappa
- `README.md`: aggiungere Norman nei riferimenti del metodo

## Nomi adottati

- `ponte` per il livello di output (riprende la framing teoria-pratica, coerente con Norman come interfaccia tra utente e sistema)
- `ciclo-azione` per il nodo Norman (preferito a `design-norman` per coerenza con `pattern-karpathy`)
- Nei progetti locali il nome può variare: `salute` usa `quadro/`, `bi` ha già `presentazione/`, `economia` ha già `output/`, `nixos` di fatto usa `home/`, `hosts/`, `modules/` (l'output è la configurazione stessa)

## Riferimenti

- Donald Norman, _The Design of Everyday Things_ (1988), capitolo sull'action cycle — epub disponibile su Drive personale, da leggere puntualmente quando si scriverà `ciclo-azione.md`
- Nodo `salute/kb/donald-norman.md` (già esistente, da citare dal nodo metodologico)
- Tabella di stato L1/L2/L3 dei quattro progetti elaborata nel `log.md` del 24/5/2026

## Filing back nel pilota

Quando i due nodi metodologici sono pronti, i file in `salute/quadro/` linkeranno entrambi (dal locale verso il meta), come fanno già con `metodo/zettelkasten.md` e `metodo/pattern-karpathy.md`. Il pattern di linking dal locale al meta diventa parte del metodo stesso.
