---
data: 2026-05-23
stato: bozza
---

# Confronto progetti adottanti

Questo nodo sintetizza la fotografia del 2026-05-23 dei quattro progetti che adottano il metodo KB: `nixos`, `bi`, `economia` e `salute`. Il dettaglio per componente vive nei nodi dedicati (`readme`, `claude`, `agents`, `mappa`, `task-aperti`, `todo`, `log`, `strumenti-kb`, `skill`, `fonte-di-verita`, `fedelta-cognitiva`); qui vengono tirate le somme.

Il confronto usa due assi. Il primo confronta i progetti tra loro, per capire quali differenze siano legittime variazioni di dominio e quali siano segnali di drift. Il secondo confronta la teoria del metodo con l'applicazione pratica, per capire dove il metodo deve chiarirsi o dove un progetto deve riallinearsi.

## Stato dei quattro progetti

| Progetto   | Profilo attuale                                                             | Segnale principale                                                                                                         |
| ---------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `nixos`    | implementazione più ordinata della ricetta su un codebase dichiarativo      | README e mappa forti; strumenti anti-drift più completi                                                                    |
| `bi`       | implementazione ricca e operativa su codebase applicativo complesso         | KB e mappa mature; revisione di `CLAUDE.md` completata dopo la fotografia iniziale                                         |
| `economia` | variante domain-specific con stato, scadenze, dati e documenti autoritativi | buon adattamento a fonti legali/finanziarie; alcuni segnali strutturali da correggere                                      |
| `salute`   | KB ampia e riflessiva, nata prima della separazione metodologica piena      | rete dei nodi molto forte; mappa, principi locali e verifica nel vivere ora rendono più esplicito l'adattamento del metodo |

## Dati strutturali

| Progetto   | Nodi KB | Link KB | Cluster README | File todo | Skill locali                                                    | Stato audit                                    |
| ---------- | ------- | ------- | -------------- | --------- | --------------------------------------------------------------- | ---------------------------------------------- |
| `nixos`    | 37      | 177     | 7              | 4         | `audit-kb`, `revisione-tasks`, `commit`                         | nessun link rotto, orfano o cluster isolato    |
| `bi`       | 84      | 329     | 11             | 9         | `audit-kb`, `revisione-tasks`, `commit`, `graphify`             | nessun link rotto, orfano o cluster isolato    |
| `economia` | 51      | 184     | 3              | 19        | `audit-kb`, `revisione-tasks`, `commit`                         | nessun errore, avviso o nota                   |
| `salute`   | 197     | 2210    | 8              | 7         | `audit-kb`, `revisione-tasks`, `commit`, `elabora-trascrizione` | rete integra; 10 nomi file accentati segnalati |

Questi numeri non sono graduatorie. `salute` ha molti più nodi perché il suo dominio è concettuale e riflessivo; `nixos` ha meno nodi perché il codice dichiarativo è una fonte di verità molto compatta; `bi` ha molti nodi perché ogni flusso applicativo richiede runbook e reference; `economia` ha una KB media ma dipende molto da file esterni, JSON e stato corrente.

## Convergenze

Tutti i progetti adottano il nucleo della ricetta: README come bootstrap, `CLAUDE.md` come ingresso operativo, `AGENTS.md` come wrapper, `log.md` come memoria interpretativa, `todo/` come spazio temporaneo, nodi atomici con footer `Connessioni:`, triade di skill `audit-kb` / `revisione-tasks` / `commit`, script `scripts/kb_tools.py`.

La separazione `metodo/ -> ../metodo/kb` è ormai il punto comune: i nodi metodologici sono consumati come dipendenza e non duplicati localmente. Questo rende più facile aggiornare il metodo, ma limita l'accesso dei progetti a eventuali futuri strumenti o skill centralizzati che vivessero fuori da `kb/`.

Le mappe canoniche sono il componente che più chiaramente migliora l'adozione nei progetti applicativi. `nixos`, `bi` ed `economia` hanno una mappa che collega sistema reale, fonti di verità e nodi KB. `salute` ha aggiunto una mappa autonoma più semantica, centrata su assi concettuali, fonti, pratica, diario e percorsi di accesso.

## Divergenze

La divergenza più importante riguarda `CLAUDE.md`. Nella fotografia iniziale `nixos` ed `economia` erano vicini alla teoria: file brevi, operativi, con riferimenti rapidi; `salute` conservava ancora molta spiegazione metodologica e struttura interna; `bi` era il caso più distante, con standard tecnici, pattern applicativi, comandi, policy e documentazione che in parte dovevano vivere nei nodi. La revisione di `bi/CLAUDE.md` e stata completata dopo questa fotografia e va considerata un riallineamento gia effettuato.

La seconda divergenza riguarda la fedeltà cognitiva. `nixos` ha il modello più avanzato, con `inventory`, `facts`, `coverage` e `fidelity`. `bi` ha un audit strutturale buono e un controllo locale di copertura script, ma la fedeltà al dominio deve ancora essere progettata su fonti primarie BI. `economia` ha `facts` adattato alla mappa, ma mostra errori strutturali da correggere. `salute` resta soprattutto semantica: la rete è sana, ma il dominio richiede verifiche qualitative e fonti testuali più che fact check tecnici.

La terza divergenza riguarda i componenti locali aggiuntivi. `economia` ha `stato.md`, `scadenze.md` e `diario.md`; `salute` ha `diario.md`, `scadenze.md` e `fonti/`; `bi` ha presentazione, client Windows e Graphify; `nixos` ha script tecnici e moduli Nix. Il metodo deve ammettere questi componenti senza trasformarli in nucleo universale.

## Implicazioni per il metodo

Il metodo deve chiarire che ogni componente ha una parte universale e una soglia di adattamento locale. La ricetta non è "tutti i progetti hanno gli stessi file", ma "tutti i progetti esplicitano quali file svolgono le funzioni cognitive della ricetta".

I nodi dei componenti devono quindi contenere esempi reali dei progetti adottanti. Questo evita una teoria astratta che non vede i casi limite: `bi` mostra il rischio di CLAUDE come manuale operativo; `economia` mostra che stato e scadenze possono essere componenti locali legittimi; `salute` mostra che una KB riflessiva può essere formalmente sana ma richiedere una mappa meno tecnica; `nixos` mostra il valore dei fact check quando la fonte di verità è dichiarativa.

Gli strumenti vanno trattati come backend del metodo, non come metodo stesso. `kb_tools.py` può avere una superficie portabile comune, ma `facts` e `fidelity` devono restare adattati al dominio finché le fonti primarie non sono comparabili.

## Strato output come componente universale

Sessione del 2026-05-24: lo strato di output, finora trattato come "componente locale aggiuntivo" di alcuni progetti, è stato riconosciuto come funzione cognitiva universale del metodo. Tutti e quattro i progetti adottanti lo implementavano già in forme proprie:

- `nixos`: l'output è la configurazione stessa, in `home/`, `hosts/`, `modules/`
- `bi`: `presentazione/` Reveal.js per la vista human-readable, scripts notturni per l'automazione
- `economia`: `output/json/` (macchina) e `output/report*.md` (umano, ancora solo tabellare)
- `salute`: ora `quadro/` con vista clinica per area di sorveglianza (pilota in bozza)

La formalizzazione vive nei nodi ponte (i tre livelli L1 macchina, L2 decisione umana, L3 azione nel mondo) e ciclo-azione (fondamento teorico via Norman). Donald Norman entra come terzo gigante del metodo accanto a Luhmann (atomicità) e Karpathy (manutenzione LLM), portando il design dell'interfaccia di azione.

La promozione non rimuove la variazione locale: il nome dello strato resta scelta di dominio. Quello che si stabilizza è la funzione (tradurre conoscenza in azione possibile) e i criteri di qualità (visibilità, feedback, mapping, constraint).

## Azioni suggerite

| Target               | Azione                                                                                                                                  | Tipo                      |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| metodo               | mantenere questo nodo come sintesi periodica e aggiornare i nodi componente con esempi reali                                            | metodo                    |
| `bi`                 | revisione di `CLAUDE.md` completata; verificare nel prossimo confronto se il file resta costituzione operativa e non manuale di dominio | completato / monitoraggio |
| `salute`             | mappa autonoma, principi specifici e loop teoria-pratica-verifica creati nel repo locale                                                | completato                |
| `economia`           | correggere link rotti e orfani emersi dall'audit                                                                                        | task locale               |
| metodo / task        | mantenere `metodo/todo/` solo per manutenzione propria del metodo; le verifiche operative restano nei repo adottanti                    | regola stabile            |
| metodo / strumenti   | aggiungere un report cross-repo ricostruibile a `scripts/kb_tools.py` o a un futuro wrapper osservatorio                                | strumento                 |
| metodo / skill       | mantenere la triade `audit-kb` / `revisione-tasks` / `commit` come base ufficiale, lasciando locali le parametrizzazioni di dominio     | regola stabile            |
| metodo / frontmatter | policy chiarita: `kb/` e `todo/` hanno frontmatter minimale; i file root ne restano privi                                               | completato                |

Connessioni:

- [osservatorio-metodo](osservatorio-metodo.md)
- [metodo-kb](metodo-kb.md)
- [ponte](ponte.md)
- [ciclo-azione](ciclo-azione.md)
- [struttura-progetto](struttura-progetto.md)
- [readme](readme.md)
- [claude](claude.md)
- [agents](agents.md)
- [mappa](mappa.md)
- [task-aperti](task-aperti.md)
- [todo](todo.md)
- [log](log.md)
- [strumenti-kb](strumenti-kb.md)
- [skill](skill.md)
- [fonte-di-verita](fonte-di-verita.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
