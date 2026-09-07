---
ciclo: runtime
---

# Ingresso di un adottante nell'osservatorio

Prescrizione per ammettere un progetto nel territorio osservato da `metodo`.
L'ingresso verifica l'adozione locale, fissa una baseline confrontabile e
predispone il primo giro di `/adottanti`; non autorizza a governare la coda del
nuovo repository.

## Verifica l'adozione locale

- identifica il commit esatto dell'adottante e conserva l'eventuale specimen
  pre-adozione;
- verifica il symlink `method/`, i register `goal.md` e `world.md`, la sezione
  README canonica e il marker `i3/allineamento-metodo.md`;
- leggi dal marker adattamenti intenzionali, limiti di verifica e commit di
  `method` recepito: `aligned` certifica l'allineamento documentale dichiarato,
  non il runtime esterno;
- applica `revisione-bootstrap-adottante.md` al quartetto README, CLAUDE, Goal
  e World;
- non correggere la coda locale: task, gradualità e priorità restano
  giurisdizione dell'adottante.

## Fissa una baseline con provenienza

- conta soltanto ciò che la superficie permette di misurare e dichiara il
  metodo: audit, query o conteggio manuale;
- registra almeno nodi KB, sintesi i2, fili i3, task e skill locali quando
  esistono; una quantità manuale non si somma retroattivamente a serie prodotte
  da un audit diverso;
- separa i limiti del checkout dai limiti del sistema vivo: assenza di accesso
  a host, scheduler, servizi o backup resta esplicita e non diventa una
  certificazione negativa;
- se manca storia comparabile, usa la baseline fondativa al posto del delta e
  demanda al primo `/adottanti` la verifica della tenuta nell'uso reale.

## Aggiorna solo le rappresentazioni correnti

- registra nome, profilo e superficie nel register `world.md`;
- cerca nel repository enumerazioni e conteggi correnti degli adottanti: `rg`
  propone candidati, non decide;
- classifica ogni occorrenza come inventario corrente da aggiornare, baseline
  locale da aggiungere con provenienza o fotografia storica da preservare;
- non riscrivere una fotografia vera perché il territorio è cresciuto: annota
  invece che il nuovo ingresso è fuori dal suo perimetro originario.

## Predisponi il primo giro

- aggiungi l'adottante alla prossima finestra `/adottanti` e dichiara quale
  segnale costituirà la sua prima verifica;
- aggiorna `i3/audit-adottanti.md` senza anticipare il cursore mensile:
  l'ingresso è un evento fuori giro, non un audit aggiuntivo;
- rigenera le viste con `o3/build-presentation.sh` e
  `o3/build-system-image.sh`;
- chiudi con `o3/kb_tools.py audit`, `git diff --check` e una ricerca finale dei
  candidati classificati, dichiarando quelli storici lasciati invariati.
