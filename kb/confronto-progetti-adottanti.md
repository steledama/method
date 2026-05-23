---
data: 2026-05-23
stato: bozza
---

# Confronto progetti adottanti

Questo nodo sintetizza la fotografia del 2026-05-23 dei quattro progetti che adottano il metodo KB: `nixos`, `bi`, `economia` e `salute`. Il dettaglio per componente vive nei nodi dedicati (`readme`, `claude`, `agents`, `mappa`, `task-aperti`, `todo`, `log`, `strumenti-kb`, `skill`, `fonte-di-verita`, `fedelta-cognitiva`); qui vengono tirate le somme.

Il confronto usa due assi. Il primo confronta i progetti tra loro, per capire quali differenze siano legittime variazioni di dominio e quali siano segnali di drift. Il secondo confronta la teoria del metodo con l'applicazione pratica, per capire dove il metodo deve chiarirsi o dove un progetto deve riallinearsi.

## Stato dei quattro progetti

| Progetto   | Profilo attuale | Segnale principale |
| ---------- | --------------- | ------------------ |
| `nixos`   | implementazione più ordinata della ricetta su un codebase dichiarativo | README e mappa forti; strumenti anti-drift più completi |
| `bi`      | implementazione ricca e operativa su codebase applicativo complesso | KB e mappa mature; `CLAUDE.md` contiene ancora molta documentazione di dominio |
| `economia` | variante domain-specific con stato, scadenze, dati e documenti autoritativi | buon adattamento a fonti legali/finanziarie; alcuni segnali strutturali da correggere |
| `salute`  | KB ampia e riflessiva, nata prima della separazione metodologica piena | rete dei nodi molto forte; README e CLAUDE restano più narrativi del metodo ideale |

## Dati strutturali

| Progetto | Nodi KB | Link KB | Cluster README | File todo | Skill locali | Stato audit |
| -------- | ------- | ------- | -------------- | --------- | ------------ | ----------- |
| `nixos` | 37 | 177 | 7 | 4 | `audit-kb`, `commit` | nessun link rotto, orfano o cluster isolato |
| `bi` | 78 | 293 | 11 | 11 | `audit-kb`, `commit`, `graphify` | nessun link rotto, orfano o cluster isolato |
| `economia` | 44 | 145 | 4 | 16 | `audit-kb`, `commit`, `revisione-tasks` | 3 link rotti, 2 orfani, 1 cluster isolato |
| `salute` | 193 | 2175 | 8 | 4 | `audit-kb`, `commit`, `elabora-trascrizione` | rete integra; 10 nomi file accentati segnalati |

Questi numeri non sono graduatorie. `salute` ha molti più nodi perché il suo dominio è concettuale e riflessivo; `nixos` ha meno nodi perché il codice dichiarativo è una fonte di verità molto compatta; `bi` ha molti nodi perché ogni flusso applicativo richiede runbook e reference; `economia` ha una KB media ma dipende molto da file esterni, JSON e stato corrente.

## Convergenze

Tutti i progetti adottano il nucleo della ricetta: README come bootstrap, `CLAUDE.md` come ingresso operativo, `AGENTS.md` come wrapper, `log.md` come memoria interpretativa, `todo/` come spazio temporaneo, nodi atomici con footer `Connessioni:`, skill `audit-kb` e `commit`, script `scripts/kb_tools.py`.

La separazione `metodo/ -> ../metodo/kb` è ormai il punto comune: i nodi metodologici sono consumati come dipendenza e non duplicati localmente. Questo rende più facile aggiornare il metodo, ma limita l'accesso dei progetti a eventuali futuri strumenti o skill centralizzati che vivessero fuori da `kb/`.

Le mappe canoniche sono il componente che più chiaramente migliora l'adozione nei progetti applicativi. `nixos`, `bi` ed `economia` hanno una mappa che collega sistema reale, fonti di verità e nodi KB. `salute` non ha ancora un nodo mappa autonomo: il README svolge parzialmente quel ruolo, ma con costo cognitivo più alto.

## Divergenze

La divergenza più importante riguarda `CLAUDE.md`. `nixos` ed `economia` sono vicini alla teoria: file brevi, operativi, con riferimenti rapidi. `salute` conserva ancora molta spiegazione metodologica e struttura interna. `bi` è il caso più distante: 824 righe, con standard tecnici, pattern applicativi, comandi, policy e documentazione che in parte dovrebbero vivere nei nodi.

La seconda divergenza riguarda la fedeltà cognitiva. `nixos` ha il modello più avanzato, con `inventory`, `facts`, `coverage` e `fidelity`. `bi` ha un audit strutturale buono e un controllo locale di copertura script, ma la fedeltà al dominio deve ancora essere progettata su fonti primarie BI. `economia` ha `facts` adattato alla mappa, ma mostra errori strutturali da correggere. `salute` resta soprattutto semantica: la rete è sana, ma il dominio richiede verifiche qualitative e fonti testuali più che fact check tecnici.

La terza divergenza riguarda i componenti locali aggiuntivi. `economia` ha `stato.md`, `scadenze.md` e `diario.md`; `salute` ha `diario.md`, `scadenze.md` e `fonti/`; `bi` ha presentazione, client Windows e Graphify; `nixos` ha script tecnici e moduli Nix. Il metodo deve ammettere questi componenti senza trasformarli in nucleo universale.

## Implicazioni per il metodo

Il metodo deve chiarire che ogni componente ha una parte universale e una soglia di adattamento locale. La ricetta non è "tutti i progetti hanno gli stessi file", ma "tutti i progetti esplicitano quali file svolgono le funzioni cognitive della ricetta".

I nodi dei componenti devono quindi contenere esempi reali dei progetti adottanti. Questo evita una teoria astratta che non vede i casi limite: `bi` mostra il rischio di CLAUDE come manuale operativo; `economia` mostra che stato e scadenze possono essere componenti locali legittimi; `salute` mostra che una KB riflessiva può essere formalmente sana ma richiedere una mappa meno tecnica; `nixos` mostra il valore dei fact check quando la fonte di verità è dichiarativa.

Gli strumenti vanno trattati come backend del metodo, non come metodo stesso. `kb_tools.py` può avere una superficie portabile comune, ma `facts` e `fidelity` devono restare adattati al dominio finché le fonti primarie non sono comparabili.

## Azioni suggerite

| Target | Azione | Tipo |
| ------ | ------ | ---- |
| metodo | mantenere questo nodo come sintesi periodica e aggiornare i nodi componente con esempi reali | metodo |
| `bi` | aprire una revisione di `CLAUDE.md` per spostare documentazione di dominio nei nodi pertinenti | task locale |
| `salute` | valutare un nodo mappa autonomo e principi specifici di dominio | task locale |
| `economia` | correggere link rotti e orfani emersi dall'audit | task locale |
| metodo / strumenti | aggiungere un report cross-repo ricostruibile a `scripts/kb_tools.py` o a un futuro wrapper osservatorio | strumento |
| metodo / skill | confrontare `audit-kb` e `commit` per capire se serva una base portabile con wrapper locali | strumento |
| metodo / frontmatter | policy chiarita: `kb/` e `todo/` hanno frontmatter minimale; i file root ne restano privi | completato |

Connessioni:

- [osservatorio-metodo](osservatorio-metodo.md)
- [metodo-kb](metodo-kb.md)
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
