---
data: 2026-06-03
stato: bozza
---

# Confronto progetti adottanti

Questo nodo sintetizza la fotografia periodica dei quattro progetti che adottano il metodo KB: `nixos`, `bi`, `economia` e `salute`. Il dettaglio per componente vive nei nodi dedicati (`readme`, `claude`, `agents`, `map`, `plan`, `tasks`, `why`, `strumenti-kb`, `skill`, `fonte-di-verita`, `fedelta-cognitiva`); qui vengono tirate le somme.

Aggiornamento 2026-06-03 (seconda fotografia, prima era 2026-05-23). Le variazioni dallo snapshot iniziale: `economia` è cresciuta (51→55 nodi, 184→198 link) e ha risolto i segnali strutturali che erano segnalati "da correggere", arrivando ad audit pulito; `bi` ha chiuso due task (task 9→7) mantenendo la KB strutturalmente stabile; `nixos` e `salute` sono invariati nei numeri. Sul piano del metodo, la novità maggiore è la formalizzazione del principio bottom-up (2026-06-01): lo sviluppo del metodo parte da un'esigenza concreta in un repo adottante e risale a `metodo` solo come generalizzazione portabile. Tutti e quattro i repo hanno audit strutturale pulito alla data.

Il confronto usa due assi. Il primo confronta i progetti tra loro, per capire quali differenze siano legittime variazioni di dominio e quali siano segnali di drift. Il secondo confronta la teoria del metodo con l'applicazione pratica, per capire dove il metodo deve chiarirsi o dove un progetto deve riallinearsi.

## Stato dei quattro progetti

| Progetto   | Profilo attuale                                                             | Segnale principale                                                                                                         |
| ---------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `nixos`    | implementazione più ordinata della ricetta su un codebase dichiarativo      | README e mappa forti; strumenti anti-drift più completi                                                                    |
| `bi`       | implementazione ricca e operativa su codebase applicativo complesso         | KB e mappa mature; revisione di `CLAUDE.md` completata dopo la fotografia iniziale                                         |
| `economia` | variante domain-specific con stato, scadenze, dati e documenti autoritativi | buon adattamento a fonti legali/finanziarie; audit ora pulito; coda `tasks/` molto attiva (21 file di lavoro reale)          |
| `salute`   | KB ampia e riflessiva, nata prima della separazione metodologica piena      | rete dei nodi molto forte; mappa, principi locali e verifica nel vivere ora rendono più esplicito l'adattamento del metodo |

## Dati strutturali

| Progetto   | Nodi KB | Link KB | Cluster index | File tasks | Skill locali                                                    | Stato audit                                    |
| ---------- | ------- | ------- | -------------- | --------- | --------------------------------------------------------------- | ---------------------------------------------- |
| `nixos`    | 37      | 177     | 7              | 4         | `audit-kb`, `tasks-review`, `commit`                         | nessun link rotto, orfano o cluster isolato    |
| `bi`       | 84      | 329     | 11             | 7         | `audit-kb`, `tasks-review`, `commit`, `graphify`             | nessun link rotto, orfano o cluster isolato    |
| `economia` | 55      | 198     | 3              | 21        | `audit-kb`, `tasks-review`, `commit`                         | nessun errore, avviso o nota                   |
| `salute`   | 197     | 2210    | 8              | 7         | `audit-kb`, `tasks-review`, `commit`, `elabora-trascrizione` | rete integra; audit pulito                     |

Questi numeri non sono graduatorie. `salute` ha molti più nodi perché il suo dominio è concettuale e riflessivo; `nixos` ha meno nodi perché il codice dichiarativo è una fonte di verità molto compatta; `bi` ha molti nodi perché ogni flusso applicativo richiede runbook e reference; `economia` ha una KB media ma dipende molto da file esterni, JSON e stato corrente.

## Convergenze

Tutti i progetti adottano il nucleo della ricetta: README come bootstrap, `CLAUDE.md` come ingresso operativo, `AGENTS.md` come wrapper, `why.md` come memoria interpretativa, `tasks/` come spazio temporaneo, nodi atomici con footer `Connessioni:`, triade di skill `audit-kb` / `tasks-review` / `commit`, script `tools/kb_tools.py`.

La separazione `metodo/ -> ../metodo/kb` è ormai il punto comune: i nodi metodologici sono consumati come dipendenza e non duplicati localmente. Questo rende più facile aggiornare il metodo, ma limita l'accesso dei progetti a eventuali futuri strumenti o skill centralizzati che vivessero fuori da `kb/`.

Le mappe canoniche sono il componente che più chiaramente migliora l'adozione nei progetti applicativi. `nixos`, `bi` ed `economia` hanno una mappa che collega sistema reale, fonti di verità e nodi KB. `salute` ha aggiunto una mappa autonoma più semantica, centrata su assi concettuali, fonti, pratica, diario e percorsi di accesso.

## Divergenze

La divergenza più importante riguarda `CLAUDE.md`. Nella fotografia iniziale `nixos` ed `economia` erano vicini alla teoria: file brevi, operativi, con riferimenti rapidi; `salute` conservava ancora molta spiegazione metodologica e struttura interna; `bi` era il caso più distante, con standard tecnici, pattern applicativi, comandi, policy e documentazione che in parte dovevano vivere nei nodi. La revisione di `bi/CLAUDE.md` e stata completata dopo questa fotografia e va considerata un riallineamento gia effettuato.

La seconda divergenza riguarda la fedeltà cognitiva. `nixos` ha il modello più avanzato, con `inventory`, `facts`, `coverage` e `fidelity`. `bi` ha un audit strutturale buono e un controllo locale di copertura script, ma la fedeltà al dominio deve ancora essere progettata su fonti primarie BI. `economia` ha `facts` adattato alla mappa e audit ora pulito. `salute` resta soprattutto semantica: la rete è sana, ma il dominio richiede verifiche qualitative e fonti testuali più che fact check tecnici. Una nota di tooling ora risolta: l'audit di `salute` segnalava nomi file con caratteri accentati (`realtà`, `qualità`, `gesù-cristo-figlio-di-dio`, …), concetti legittimi di una KB riflessiva in italiano. La convenzione "niente accenti nei nomi file" e la possibilità di derogarvi per dominio erano in tensione; `salute` ha scelto di normalizzare i nomi e l'audit è ora pienamente pulito. Il caso resta utile come promemoria: un warning strumentale va interpretato — default tecnico o specificità di dominio — non soppresso meccanicamente.

La terza divergenza riguarda i componenti locali aggiuntivi. `economia` ha `stato.md`, `scadenze.md` e `diario.md`; `salute` ha `diario.md`, `scadenze.md` e `fonti/`; `bi` ha presentation, client Windows e Graphify; `nixos` ha script tecnici e moduli Nix. Il metodo deve ammettere questi componenti senza trasformarli in nucleo universale.

## Implicazioni per il metodo

Il metodo deve chiarire che ogni componente ha una parte universale e una soglia di adattamento locale. La ricetta non è "tutti i progetti hanno gli stessi file", ma "tutti i progetti esplicitano quali file svolgono le funzioni cognitive della ricetta".

I nodi dei componenti devono quindi contenere esempi reali dei progetti adottanti. Questo evita una teoria astratta che non vede i casi limite: `bi` mostra il rischio di CLAUDE come manuale operativo; `economia` mostra che stato e scadenze possono essere componenti locali legittimi; `salute` mostra che una KB riflessiva può essere formalmente sana ma richiedere una mappa meno tecnica; `nixos` mostra il valore dei fact check quando la fonte di verità è dichiarativa.

Gli strumenti vanno trattati come backend del metodo, non come metodo stesso. `kb_tools.py` può avere una superficie portabile comune, ma `facts` e `fidelity` devono restare adattati al dominio finché le fonti primarie non sono comparabili.

## Strato output come componente universale

Sessione del 2026-05-24: lo strato di output, finora trattato come "componente locale aggiuntivo" di alcuni progetti, è stato riconosciuto come funzione cognitiva universale del metodo. Tutti e quattro i progetti adottanti lo implementavano già in forme proprie:

- `nixos`: l'output è la configurazione stessa, in `home/`, `hosts/`, `modules/`
- `bi`: `presentation/` Reveal.js per la vista human-readable, scripts notturni per l'automazione
- `economia`: `output/json/` (macchina) e `output/report*.md` (umano, ancora solo tabellare)
- `salute`: ora `quadro/` con vista clinica per area di sorveglianza (pilota in bozza)

La formalizzazione vive nei nodi output (o1 macchina, o2 decisione umana, o3 azione nel mondo; + strato input i1/i2/i3) e ciclo-azione (fondamento teorico via Norman). Donald Norman entra come terzo gigante del metodo accanto a Luhmann (atomicità) e Karpathy (manutenzione LLM), portando il design dell'interfaccia di azione.

La promozione non rimuove la variazione locale: il nome dello strato resta scelta di dominio. Quello che si stabilizza è la funzione (tradurre conoscenza in azione possibile) e i criteri di qualità (visibilità, feedback, mapping, constraint).

Stato al 2026-06-05: il nodo `ponte` è stato sostituito da `output` (rifondazione input/output), `ciclo-azione` aggiornato con la nomenclatura o/i e il cappio a due cerniere. Entrambi restano `stato: bozza` — la promozione a `maturo` è un filing back atteso dal pilota `salute/quadro/` quando produrrà 2-3 cicli completi documentati.

## Azioni suggerite

| Target               | Azione                                                                                                                                  | Tipo                      |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| metodo               | mantenere questo nodo come sintesi periodica e aggiornare i nodi componente con esempi reali                                            | metodo                    |
| `bi`                 | `CLAUDE.md` a 190 righe: tabella strumenti propagata, non manuale di dominio. Resta sotto monitoraggio qualitativo, non quantitativo    | monitoraggio              |
| `salute`             | mappa autonoma, principi specifici e loop teoria-pratica-verifica creati nel repo locale                                                | completato                |
| `economia`           | audit ora pulito (55 nodi, 198 link, 0 problemi): i segnali strutturali sono risolti                                                    | completato                |
| metodo / output      | promuovere `output` e `ciclo-azione` da bozza a maturo quando il pilota `salute/quadro/` produce cicli completi documentati            | filing back atteso        |
| metodo / task        | mantenere `metodo/tasks/` solo per manutenzione propria del metodo; le verifiche operative restano nei repo adottanti                    | regola stabile            |
| metodo / strumenti   | un report cross-repo automatico resta non necessario finché l'osservatorio si ricostruisce a mano in poche query; aprire solo se il costo cresce | bottom-up: in attesa      |
| metodo / skill       | mantenere la triade `audit-kb` / `tasks-review` / `commit` come base ufficiale, lasciando locali le parametrizzazioni di dominio     | regola stabile            |
| metodo / frontmatter | policy chiarita: `kb/` e `tasks/` hanno frontmatter minimale; i file root ne restano privi                                               | completato                |

Connessioni:

- [osservatorio-metodo](osservatorio-metodo.md)
- [metodo-kb](metodo-kb.md)
- [output](output.md)
- [ciclo-azione](ciclo-azione.md)
- [struttura-progetto](struttura-progetto.md)
- [readme](readme.md)
- [claude](claude.md)
- [agents](agents.md)
- [map](map.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [why](why.md)
- [strumenti-kb](strumenti-kb.md)
- [skill](skill.md)
- [fonte-di-verita](fonte-di-verita.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
