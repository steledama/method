# Segnale: le dipendenze dei task non sono solo task↔task

Data: 2026-06-21 · Fonte: `economia` (origine del segnale), con riscontri in
`nixos`, `salute` e `bi`

## Il segnale

La colonna `Dip.` di `plan.md` nasce per esprimere _cosa impedisce di agire_, ma
il modello implicito — una dipendenza è un puntatore a un altro task (`#n`) —
è troppo povero per la pianificazione reale. Operando su `economia` è emerso che
un task aperto può trovarsi in **condizioni di eseguibilità diverse fra loro**,
non riducibili al «dipende dal task X»: ci sono task fermi su un evento del mondo
e task che _si potrebbero_ fare ma che teniamo deliberatamente sospesi.

Il segnale è arrivato qui perché chi opera su `economia` lo ha giudicato
**generalizzabile** — non un'inezia di dominio — e quindi degno di percorrere in
`method` il ciclo completo i1→i2→i3.

Riscontri trasversali dello stesso attrito, prima di questa cattura:

- `nixos` — il task _Monitor server boot after LTS kernel switch_ era marcato
  `[a] = rebuild e reboot controllato di norvegia e svezia` (commit di chiusura
  `c36c141`): un task di **monitoraggio** la cui «dipendenza» non era un altro
  task ma una condizione da sorvegliare nel tempo. Tenuto aperto per vigilanza,
  non per blocco da un task gemello.
- `salute` e `bi` — stesso pattern atteso: task che restano aperti perché vanno
  tenuti presenti, ma con condizioni di svolgimento eterogenee (attesa di un
  referto/dato esterno vs. attesa deliberata).

## L'attrito osservato

Comprimere tutte queste situazioni in «dipende / non dipende da un task»
appiattisce la pianificazione: due task entrambi «non `—`» possono richiedere
risposte opposte (sollecitare un attore esterno vs. lasciar sedimentare una
decisione). Il fatto che un task sia ancora aperto significa che chiede
**monitoraggio attivo**, ma non tutti gli aperti hanno le stesse condizioni di
svolgimento, e la `Dip.` attuale non lo distingue.

In particolare resta non separato il caso del task **azionabile ma trattenuto**:
la mossa è nostra, nessun attore esterno ci blocca, eppure scegliamo di non
agire — per attendere la maturazione di una negoziazione a più attori, o per
darci tempo (ripensamento, valutazione a freddo, attesa di più dati).

## La proposta da valutare (i2→i3, non ancora verdetto)

Da `economia` è stata avanzata una classificazione a quattro significanti per la
colonna `Dip.`, da vagliare in `method`:

1. `—` — nessuna dipendenza: il task è eseguibile ora.
2. `n` — dipendenza interna: il task attende lo svolgimento del task n.
3. `world` — il task attende dal mondo una conferma, un evento, un messaggio, un
   preventivo, un'azione di un attore esterno (il prossimo passo non è nostro).
4. `|` — **pausa tattica**: il task sarebbe eseguibile, ma si sceglie
   deliberatamente di non agire — per attendere il muoversi degli altri attori di
   una negoziazione, o per «pensarci su» (approfondimento, ripensamento,
   valutazione a freddo o su più dati).

La distinzione chiave rispetto allo stato attuale del canone è tra `world` (non
tocca a noi) e `|` (tocca a noi, ma scegliamo di attendere).

## Esito

Valutato e formalizzato. Il quarto significante `|` è stato adottato e distinto da
`world`: cfr. `verdict.md`, filo «I quattro significanti di `Dip.`», con
recepimento in `kb/plan.md`. La regola sulle date segue _chi possiede l'orologio_
(esogena → `## Scadenze`; autoimposta → legenda del `|`), correggendo il primo
passo grezzo `f929f7e` che lasciava `—` un task deliberatamente sospeso. La
notazione è a tre livelli: significante in tabella, chiosa facoltativa in legenda
(`world [a]`, `| [b]`), dettaglio nel file `tasks/`.
