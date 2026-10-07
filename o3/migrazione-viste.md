---
data: 2026-10-04
stato: attiva
ciclo: runtime
target: nixos, danea-auto
---

# Le viste escono in `view/`, il deck curato in `presentation/`

## Cosa e perché

Il canone separa le **viste**, derivate e rigenerate, dal **deck**, il
racconto curato dell'artefatto (`kb/view.md`, `kb/presentation.md`): `view/`
è tutta generata dall'unico entrypoint `python3 o3/view/build.py`,
`presentation/` tiene la sola sorgente del deck, `o3/view/` i builder. La
ricetta completa di recepimento è nella storia di questo file (`216ec6f`,
`f21594b`).

## Stato

Recepita da tutti e sei i destinatari originari, verificato nei file su
`origin` il 2026-10-05: `o3/view/` presente, `o3/presentation/` assente,
nessun deck in `i2/`. Marker: `nixos`, `bi`, `economia`, `salute` e `crm` a
`f21594b`, `danea-auto` a `a344f64`. `baserow` è nato nella forma nuova. La
prescrizione resta attiva per la forma vecchia dei servizi. Il seguito sul
deck di `nixos` è trasferito a [presidio-ipotesi](presidio-ipotesi.md).

## Residui

1. **Togliere la forma vecchia del servizio** — `nixos`, `danea-auto`.
   Prima della migrazione il servizio permanente accettava entrambe le
   forme: `view/index.html` servito da `o3/view/serve.py` oppure
   `presentation/index.html` servito da `o3/presentation/serve.py`. Ora
   tutti i repo serviti sono migrati, quindi il ramo vecchio non ha più
   funzione:
   - in `nixos`, `o3/modules/home/presentations.nix`: il ramo
     `o3/presentation/serve.py`, il controllo sul processo che lo esegue
     ancora e la path unit che riavvia il servizio alla comparsa di
     `view/index.html` (deck e coppia server);
   - in `danea-auto`, `o3/scheduler/serve_presentazione.pyw`: la coppia
     `o3/presentation/serve.py` / `presentation/index.html` (`danea2`).

   Il passaggio alla pubblicazione da commit pulito
   ([viste-fuori-da-git](viste-fuori-da-git.md)) riscrive comunque questi
   servizi: il residuo può chiudersi nello stesso giro.

   Prima di togliere, il `method` locale verifica che ogni repo servito
   dall'host abbia `view/index.html` sul checkout dell'host, non solo su
   `origin`. Dopo il deploy, ogni porta risponde ancora coi titoli giusti.

## Verifica

Il battito `/adottanti` legge nei file su `origin` che i due servizi non
nominano più `o3/presentation/` e che le porte rispondono; per `danea2` resta
il collaudo riportato dall'istanza locale. Chiusa la
rimozione della forma vecchia dei servizi, questa prescrizione si pota.
