---
ciclo: runtime
---

# Ingresso di un adottante

Procedura permanente per un progetto che adotta il metodo. Il lavoro sul
nuovo repo lo fa il coordinatore del suo gruppo, nel proprio repository e col
proprio custode; `method` registra soltanto la voce di territorio. L'ingresso
non autorizza nessuno a governare la coda del nuovo repository
(`kb/method-observatory.md`, «Ingresso di un adottante»).

## Nel coordinatore del gruppo

- verifica l'adozione locale: commit esatto, canone letto (symlink `method/`
  per i repo del custode, checkout a un tag per chi è mantenuto da altri),
  register `goal.md` e `world.md`, sezione README canonica e marker
  `i3/allineamento-metodo.md` con la versione o il commit recepito;
- leggi dal marker adattamenti intenzionali e limiti di verifica: `aligned`
  certifica l'allineamento documentale dichiarato, non il runtime esterno;
- rileggi insieme il quartetto README, CLAUDE, Goal e World contro i nodi
  `readme`, `claude`, `goal` e `world`;
- aggiungi il repo alla sezione `## Membri` del tuo `world.md`, col checkout e
  l'host (`kb/view-publishing.md`, «Sito di gruppo»), e verifica che si legga:
  `python3 <canone>/o3/adottanti.py --root . stato <nome>`;
- scegli con l'adottante un accento per le viste che non sia già in uso né
  confondibile a colpo d'occhio con quelli del `world.md` di `method` (stessa
  tinta in tonalità vicina non basta a distinguere);
- pubblica la vista del nuovo membro e verifica `/<repo>/_stato` nel sito del
  gruppo;
- se il gruppo confronta i propri membri, fissa una baseline con provenienza
  nel tuo `i2/`: conta solo ciò che la superficie permette di misurare e
  dichiara come; l'assenza di accesso a host, scheduler o servizi resta
  esplicita e non diventa una certificazione negativa;
- non correggere la coda locale: task, gradualità e priorità restano
  giurisdizione dell'adottante.

## In `method`

- registra nome, profilo, checkout con l'host, accento e vista nel register
  `world.md`, come voce di territorio: `method` non legge i membri dei gruppi
  che non coordina;
- cerca nel repository enumerazioni e conteggi correnti degli adottanti, come
  «otto adottanti» in README e `world.md`: `rg` propone candidati, non decide;
- classifica ogni occorrenza come inventario corrente da aggiornare o
  fotografia storica da preservare, e non riscrivere una fotografia vera
  perché il territorio è cresciuto;
- rigenera le viste con `python3 o3/view/build.py` e chiudi con
  `o3/kb_tools.py audit` e `git diff --check`.
