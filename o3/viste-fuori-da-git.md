---
data: 2026-10-07
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, danea-auto, baserow
---

# Le viste escono da git e l'host le pubblica da commit pulito

## Cosa e perché

`view/` è derivata dalle fonti, dai builder e dagli asset versionati.
Versionarla raddoppiava la storia con HTML rigenerato e portava nel commit il
toolchain dell'host che l'aveva costruita. Il canone ora la tiene fuori da
git (`kb/view.md`, «Freschezza» e «Pubblicazione»):

- in locale `python3 o3/view/build.py` rende il working tree come
  **anteprima**, dichiarata nella home;
- nel gate di `/commit` la build è una **verifica**
  (`build.py --check`), e il suo output non entra nel commit;
- l'host privilegiato **pubblica da commit pulito** con
  `build.py --publish DIR` e serve con `serve.py --publish-root DIR`:
  ultima vista buona, provenienza nella home, stato in `/_stato`.

`metodo` l'ha fatto per primo (`9b9597f`), col servizio di `deck` preparato
in `nixos` e collaudato prima di togliere `view/` da git. La ricetta è stata
provata in un clone di `nixos` e uno di `salute`, i due fork con un builder di
deck di dominio: pubblicazione e anteprima coincidono, salvo il piè di pagina.

## Ordine: builder, host, poi git

Per ogni repo, in quest'ordine, senza saltare il collaudo:

1. **Builder** (il `method` locale). Nessun cambio di servizio, `view/` resta
   versionata finché il passo 3 non arriva.
2. **Host** (chi ne governa i servizi: `nixos` per `deck` e la coppia server,
   `danea-auto` per `danea2`). Il servizio passa alla forma pubblicata solo
   dopo che il checkout dell'host ha i builder nuovi **in un commit**: la
   pubblicazione costruisce `HEAD`, quindi builder solo nel working tree
   fanno fallire la prima pubblicazione. Se l'host non è quello dove si
   sviluppa, serve anche il push e l'aggiornamento del suo checkout.
3. **Git** (il `method` locale). `view/` esce dall'indice solo con l'host
   pronto e la porta collaudata.

La preparazione dei servizi in `nixos` è una dipendenza esplicita per i repo
che serve, non un passo successivo alla rimozione dell'output. Una pausa fra
i passi è legittima: un repo al passo 1 continua a funzionare con la forma
attuale del servizio. In quella finestra la home versionata si dichiara
anteprima.

## Ricetta per il /method locale

1. **Copiare i builder canonici** dal checkout di `metodo` a cui punta il
   symlink `method/` (la sua `o3/view/`): `build.py`,
   `publish.py`, `serve.py`, `build_pages.py`, `sources.py` e
   `assets/system-image.css`. `build_system_image.py` ha la sezione CONFIG
   del repo: portare solo le funzioni nuove (`provenance_html` e il
   parametro `provenance` di `render`). Un fork con adattamenti dichiarati
   (cfr. `salute`) porta le modifiche del canone sopra i propri, non il
   contrario.
2. **Builder di deck di dominio**: se `project.py` dichiara `DECK_BUILDER`,
   `render` accetta ora la cartella di uscita,
   `render(root, reveal_url, folder)`, e chiude i link contro `folder`, mai
   contro `root / "view"`, che durante una build non è l'output. Con la firma
   vecchia la build si ferma e lo dice.
3. **Provare**: `python3 o3/view/build.py --check` passa;
   `python3 o3/view/build.py` dà la stessa `view/` di prima, salvo la home
   che si dichiara anteprima e il CSS del piè di pagina. In una cartella
   temporanea, `build.py --publish DIR` su un commit dà una vista identica
   all'anteprima, salvo `index.html` e `provenance.json`.
4. **Aggiornare le skill del repo**: il gate i2 del fork di `/commit` esegue
   `build.py --check` (con la regola di transizione finché `view/` è
   versionata); `exec plan` usa `--check` per il contratto plan × `o2/`.
5. **Passo 1 chiuso**: commit e push su richiesta del custode, marker al
   commit di `metodo` recepito. Segnalare all'host che il checkout è pronto.
6. **Dopo il collaudo dell'host**: `/view/` in `.gitignore`,
   `git rm -r --cached view`, la regola `view/**` tolta da `.gitattributes`
   se presente. Bussole e istruzioni (README, CLAUDE, AGENTS, commenti di
   `project.py`) non dicono più che le viste si aprono dal checkout senza
   build; un link a `view/index.html` in una bussola si rompe su un clone
   pulito. Verifica su una copia dei soli file tracciati: audit senza link
   rotti, `--check` e build riusciti. Il symlink `method` è relativo
   (`../method/kb`): la copia va messa accanto al repo, per esempio
   `git worktree add --detach ../<repo>-verifica` dopo il commit (poi
   `git worktree remove --force`, perché la build vi lascia la `view/`
   ignorata), altrimenti il symlink non si risolve e l'audit
   va ripuntato a mano.
7. Registrare nel marker il recepimento o l'adattamento motivato.

## Stato

- **nixos**: recepita fino all'ultimo passo, riportato dall'istanza di
  `nixos` e verificato su `deck` il 2026-10-07: `b5867fc` con `view/` fuori
  dall'indice, marker a `341b622` `aligned`, porta 8002 nella forma
  pubblicata (`served_commit` `b5867fc`, `ok: true`). Non ancora su
  `origin`. Le due note pratiche della ricetta (builder in un commit prima
  di attivare, copia di verifica accanto al repo) vengono da questo giro.
- **salute**: recepita per intero il 2026-10-07, verificato su `deck`:
  builder in `1829087` e `430e6ed`, servizio di `nixos` in `4a726d4` (porta
  8003 collaudata), `view/` fuori da git in `36fa7db`, ripubblicato da solo
  (`served_commit` `36fa7db`, `ok: true`). Non ancora su `origin`. La patch
  del canone si è applicata sopra gli adattamenti locali senza conflitti.
- **economia**: recepita per intero il 2026-10-07, verificato su `deck`:
  builder in `5f46e90`, servizio di `nixos` in `fe080cd` (porta 8004
  collaudata, fotografia mensile nel deck), `view/` fuori da git in
  `22462c9`, ripubblicato da solo (`served_commit` `22462c9`, `ok: true`).
  Non ancora su `origin`; dalla LAN casa la porta non è stata provata. Il
  giro ha trovato la `view/` versionata a `4f03c89` indietro rispetto alle
  fonti (un task già ritirato ancora reso). Le fonti derivate versionate del
  repo (`build_perceptions_index.py`, `fotografia_mensile.py`) restano in git
  e si rigenerano nel gate.
- **bi**: passi 1-5 fatti il 2026-10-07 in `5fc8008e` su `svezia`, marker
  a `4a1bd0c` `aligned` con l'adattamento in corso, secondo l'esito
  riportato dall'istanza di `bi`: non su `origin` e non verificato da
  `metodo`. La `view/` versionata a `85e40937` non era indietro. Il checkout
  servito è `~/bi` su `svezia`, lo stesso in cui `bi` lavora. Il passo 6
  attende il collaudo della porta 8001 sulla coppia server da parte di
  `nixos`.
- **crm, baserow, danea-auto**: da recepire. `nixos`
  aggiunge ai suoi servizi i repo di `deck` e della coppia server quando
  ognuno ha chiuso il passo dei builder.

## Indizi per repo, da verificare in loco

- **nixos** (recepita, cfr. Stato), a `7eb6811`: il servizio di `method` era già nella forma
  pubblicata (elenco `published` in `o3/presentations.nix`, tre unit per
  repo, `ExecCondition` con `serve.py --check`). Per sé: `nixos_deck.py`
  chiude i link su `root / "view"` (passo 2 della ricetta). Come host:
  estendere `published` ai repo serviti da `deck` (`nixos`, `salute`,
  `economia`) e dalla coppia server (`bi`, `crm`, `baserow`) man mano che
  ognuno chiude il passo 1. Sulla coppia la unit segue il ruolo
  `production`; l'innesco dopo l'aggiornamento del checkout è una scelta
  locale, e la scelta del pull manuale fatta per `deck` non vincola gli
  altri host. Il residuo di `migrazione-viste` (la forma vecchia e le unit
  `-vista`) può chiudersi nello stesso giro.
- **salute**: `build.py` ha due adattamenti dichiarati (`check_plan_details`
  e le tavole `PLATES` del builder di dominio); la patch del canone vi si
  applica sopra senza conflitti. `build_deck.py` cambia solo la firma di
  `render`.
- **economia**: `deck.py` cambia solo la firma di `render`. Il symlink
  tracciato `gdrive` arriva nelle fonti esportate come link pendente: la
  build non lo segue, ma un builder di dominio non deve leggerlo.
- **bi, crm, baserow**: nessun builder di dominio. Il servizio vive sulla
  coppia server: la pubblicazione su `svezia` (produzione) e la
  preparazione dello standby su `norvegia` passano da `nixos`. Su `svezia`
  il checkout si aggiorna con un pull manuale, come su `deck` (decisione del
  custode, 2026-10-07). Ricetta provata da `metodo` su un clone di `bi` a
  `85e40937`: patch senza conflitti, pubblicazione identica all'anteprima.
- **danea-auto**: sviluppo e servizio sullo stesso host, `danea2`, Windows.
  La verifica precede il commit, la pubblicazione lo segue su fonti pulite:
  definire il comando o meccanismo locale che la esegue dopo il commit e al
  riavvio del task (`o3/scheduler/serve_presentazione.pyw` passa a
  `--publish-root`). Il symlink tracciato `method` punta a un path assoluto
  Windows: verificare che l'estrazione di `git archive` con `tarfile` lo
  accetti sull'host, dove i symlink possono chiedere privilegi. Collaudare
  lo scambio fra versioni col server Windows in funzione prima di togliere
  `view/` da git. Il residuo di `migrazione-viste` (la forma vecchia nel
  lanciatore) può chiudersi nello stesso giro.

## Verifica e chiusura

Il `/method` locale verifica sui file i passi 1, 3 e 6 e dichiara il
collaudo dell'host, con ciò che non ha potuto verificare. Il battito
`/adottanti` applica i tre controlli distinti di `kb/view.md`: build e
contratti sulle fonti di `origin`, revisione servita rispetto al riferimento
remoto, porta raggiungibile dal luogo dell'audit. La prescrizione resta
finché i sette non hanno `view/` fuori da git e un servizio che pubblica da
commit pulito, o una divergenza motivata nel marker.
