---
sintesi: "Proposta del 2026-10-06: view/ esce da git in tutti i repo. Le viste si generano sull'host privilegiato che le serve, con una unit dichiarata in nixos che ricostruisce dopo il pull, e in locale su richiesta. Il task porta i fatti verificati, il giro in quattro tempi, la build che resta come verifica nel gate di /commit e i punti da rivalutare; resta pause fino alla revisione del custode."
ciclo: dev
---

# Viste fuori da git

Task `pause`. La proposta nasce il **2026-10-06** dal custode, che
riconsidera la decisione di versionare `view/` presa con la migrazione delle
viste (`216ec6f`). Si attende la sua revisione prima di toccare il canone.

## La proposta

`view/` è interamente derivata dalle fonti `.md` e da `presentation/`:
versionarla è un debito (`kb/view.md`, «Freschezza»). Ogni repo ha già un
**host privilegiato** che serve le viste sulle reti private; basta che sia
lui a generarle. Il flusso diventa: commit → push su richiesta → pull
sull'host privilegiato → ricostruzione automatica. Chi lavora su un altro
checkout genera le viste in locale quando vuole aprirle.

## Fatti verificati il 2026-10-06

- `view/` in `metodo`: 41 file, tutti prodotti da `python3 o3/view/build.py`
  (Pandoc e Prettier). La rigenerazione sul checkout pulito non cambia nulla:
  la build è deterministica e le viste erano fresche.
- I 17 MB di `view/` sono quasi tutti i sette PNG copiati da
  `presentation/`: blob identici, git li conserva una volta. Il peso non è un
  argomento.
- 24 dei 75 commit dell'ultimo mese toccano `view/`: un terzo della storia
  porta HTML rigenerato.
- L'output dipende dalla versione di Pandoc dell'host: il 2026-10-05 il deck
  di `danea-auto` differiva solo per quella (`goal.md`, obiettivo 2).
- Le ragioni del versionamento in `kb/view.md` sono due: aprire le viste dal
  checkout senza build, e il servizio permanente che «lancia lo stesso
  `serve.py` del checkout; un pull aggiorna le viste senza riavvii». L'hook
  di rigenerazione era scartato perché installazione host-locale non
  versionata.
- In `nixos` (`o3/modules/home/presentations.nix`, `o3/presentations.nix`)
  il pull sugli host privilegiati è **manuale**: oggi le viste servite
  cambiano solo dopo push e pull. Host privilegiati: `deck` per `method`,
  `nixos`, `salute`, `economia`; il ruolo `production` della coppia server
  per `bi`, `crm`, `baserow`; `danea2` per `danea-auto`.

## Perché l'obiezione all'hook non regge più

Una path unit systemd **dichiarata in `nixos`** è versionata, non stato
host-locale: è lo stesso schema della path unit `-vista` già in uso per la
migrazione. La ricostruzione dopo il pull diventa automatica, push e pull
restano gesti del custode. Con Pandoc e Prettier forniti da nix sugli host
privilegiati, la build ha versioni fisse: sparisce anche il rumore fra host.

## Il giro in quattro tempi

1. **`metodo`, il canone**:
   - `kb/view.md`: viste non versionate; build sull'host privilegiato dopo
     il pull e in locale su richiesta. Si riscrivono «Freschezza»
     (l'obbligo passa dal commit al servizio), «Perimetro» (`view/` non si
     versiona ma si serve: resta decisione sui dati), «HTML apribile
     direttamente e build minima», «Servizio sulle reti private» (la
     condizione «nessuna copia separata» si aggiorna: il servizio ricostruisce
     e serve dal checkout);
   - `goal.md`, Goal di sviluppo: «viste che si aprono dal checkout» diventa
     «viste servite dall'host privilegiato, generabili in locale»;
   - gate di `/commit`: la build **resta**, ma come verifica e non come
     rigenerazione da committare. `build.py` controlla anche i contratti
     fra le fonti («Derivata implica verificata»): toglierla dal gate
     sposterebbe l'errore sul server, dopo il push, dove la vista servita
     resta ferma senza che nessuno lo veda. Il gate esegue la build, rompe
     sul contratto violato, e il suo output non entra nel commit. Resta il
     giudizio sugli artefatti di sintesi `i2/`;
   - `/adottanti`: la freschezza non si legge più su `origin` ma sulla porta
     servita. Proposta: la build scrive l'hash del commit sorgente nel piè
     di pagina della home, così il controllo è un confronto fra hash. Una
     porta che dal PC dell'audit non si raggiunge si dichiara non
     verificata, non si presume fresca;
   - `.gitignore` con `view/` e `git rm -r --cached view`;
   - riferimenti a `view/` versionata nelle skill e nei nodi
     (`project-structure`, `presentation`, `karpathy-pattern`, `zettelkasten`
     da rileggere).
2. **Prescrizione `o3/`** per i sette adottanti: `.gitignore`, rimozione di
   `view/` dall'indice, verifica che la home servita mostri l'hash di
   `origin`. Collegata a `migrazione-viste`, che si può chiudere nello stesso
   giro.
3. **`nixos`**: Pandoc e Prettier sugli host privilegiati; per ogni repo una
   path unit su `.git/logs/HEAD` che lancia `o3/view/build.py` e, se la home
   prima mancava, avvia il servizio. La `ConditionPathExists` su
   `view/index.html` resta la diagnosi dell'assenza. Si toglie insieme il
   ramo della forma vecchia (`o3/presentation/serve.py`, path unit `-vista`),
   residuo di `migrazione-viste`.
4. **`danea-auto`**: si sviluppa solo su `danea2`, che lo serve: lì non c'è
   un pull da intercettare, la build del gate di `/commit` produce già le
   viste sul posto. Nessun meccanismo di ricostruzione su Windows; lo
   scheduler `o3/scheduler/serve_presentazione.pyw` perde solo la forma
   vecchia. Il custode valuta di togliere i cloni dagli altri
   host per non modificarlo altrove; `/adottanti` legge su `origin` e non ne
   dipende.

## Da rivalutare in revisione

- **Raggiungibilità delle porte**: il controllo di `/adottanti` per hash
  presuppone che ogni porta servita si raggiunga dal PC dell'audit. Da
  verificare in particolare `danea2` da casa e la coppia server dal lavoro.
- **Pull ancora manuale**: le viste servite restano indietro finché non si
  fa il pull, come oggi. Un pull automatico sull'host privilegiato è una
  decisione separata, fuori da questo task.
- **Errore di build sul server**: il contratto fra fonti fa fallire la build;
  serve che il servizio continui a servire l'ultima vista buona e che
  l'errore sia leggibile (journal), non un'assenza silenziosa.
- **Deck in `presentation/`**: resta versionato come sorgente; solo la sua
  resa in `view/presentation.html` esce da git.

## Bilancio e momento

Il guadagno è modesto — diff puliti, nessuna vista stale nella storia — e il
costo è un giro su sette repo più `nixos`. Conviene farlo insieme alla
chiusura di `migrazione-viste`, che tocca gli stessi servizi, non come lavoro
a sé.

La pulizia della storia è scartata: nessun commit tocca solo `view/` (0 su
25), lo spazio non cala perché i PNG sono gli stessi blob di
`presentation/`, e la riscrittura degli hash romperebbe i marker degli
adottanti e i riferimenti nei `.md`. Basta `git rm --cached` da qui in
avanti.

## Criterio di chiusura

Il custode approva, corregge o ritira la proposta. Se approvata, il task si
consuma col canone rivisto e la prescrizione pubblicata; il seguito negli
adottanti vive nella prescrizione, quello in `nixos` nel suo plan.
