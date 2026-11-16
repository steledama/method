---
sintesi: "Ingresso dell'abbinatore (ottavo adottante) nell'osservatorio secondo o3/ingresso-adottante.md. Attende l'adozione locale in ~/abbinatore su svezia, condotta da una sessione lì dallo specimen ad42082; si sblocca quando il marker locale segna aligned. Qui vivono specimen, baseline pre-adozione, candidati classificati, accento e punti da rileggere."
ciclo: runtime
---

# Ingresso dell'abbinatore nell'osservatorio

Task in attesa (`w1`). L'abbinatore è l'app Django delle compatibilità fra
consumabili e modelli di stampante, con le equivalenze rebrand: produce gli
XML che leggono il sito e `bi`. Alessio l'ha passato al custode il
2026-10-26, il materiale è arrivato il 2026-11-16. Il custode ha deciso lo
stesso giorno l'adozione integrale, ristrutturazione della root compresa,
finché il progetto è in sviluppo. La conduce una sessione in `~/abbinatore`
su `svezia`; il lavoro in quel repository resta suo. L'ingresso dal lato
`method` segue [`o3/ingresso-adottante.md`](../o3/ingresso-adottante.md) e
parte solo quando l'adozione locale è verificabile. Fonte: messaggio della
sessione `nixos` di `svezia`, inoltrato su richiesta del custode il
2026-11-16.

È l'adottante che `world.md` attendeva come `abbinamenti` dalla dismissione
di `crm`: il nome è quello del repository.

## Il progetto in tre tempi

- **1, trasloco**: da AWS a `svezia`, dietro VPN, a comportamento invariato;
  il lato host vive in `nixos-lavoro`, task `o2/abbinatore-host.md`;
- **2, semplificazione del flusso** con `bi`;
- **3, lavoro agentico**; i tempi 2 e 3 vivono nel task
  `o2/ridisegno-flusso-abbinamenti.md` di `bi`.

## Specimen pre-adozione

- repository `tt-sviluppo/abbinatore` (privato), copia con tutta la storia
  di `toscanatrading/abbinatore`, che resta nel checkout come remote
  `alessio`;
- specimen `ad42082a05fa68a688c617f97ddacc58df8c7201`, «docs(passaggio):
  solo la parte locale, il server attuale resta ad Alessio», 54 commit,
  allineato a `origin/main` al 2026-11-16;
- canone di riferimento al 2026-11-16: `method` a `59f97f2`; se `method`
  avanza durante l'adozione, il marker dichiara quale commit ha recepito.

## Baseline fondativa

Conteggio manuale sullo specimen, il 2026-11-16, con `find` e `git log`:
non si somma alle serie di `o3/adottanti.py audit`.

- nessuna superficie del metodo: niente symlink `method/`, `goal.md`,
  `world.md`, collezioni `i1/`–`o3/`, `kb/`, marker, skill locali;
- conoscenza già scritta, da ricollocare: `CLAUDE.md` di progetto (regole,
  contratti con altri sistemi), `README.md`, `deploy.md`, sette file in
  `docs/` (`analisi-app`, `changelog`, `decisions` con gli ADR,
  `passaggio`, `produzione`, `todo`) più `docs/conoscenze/`;
- codice: app `abbinatore/` (56 file), `config/`, `templates/`, `locale/`;
  `legacy/` (25 file) è il vecchio ASP.NET, riferimento storico non
  modificabile;
- runtime: in produzione su AWS, gestito da Alessio; il checkout ha solo la
  copia del database, nessuna credenziale.

Non c'è storia comparabile: la baseline sostituisce il delta, e il primo
`/adottanti` verifica la tenuta nell'uso.

## Accento delle viste

`#475569`, grigio ardesia, scelto dal custode il 2026-11-16. Accenti in uso
(`world.md`): `#4338ca` (`method`), `#c2410c`, `#a16207`, `#0f766e`,
`#15803d`, `#be123c`, `#7e22ce`, `#0369a1`. L'ardesia è l'unica tinta
libera lontana da tutte: fucsia e lime, le alternative, stavano a ridosso
di viola e verde. Va in `o3/view/project.py` dell'adottante e accanto alla
sua voce in `world.md`.

## Condizione di sblocco

In `~/abbinatore` esistono il symlink `method/`, `goal.md`, `world.md`, la
sezione README canonica e `i3/allineamento-metodo.md` con `status: aligned`.

## Candidati classificati

Ricerca del 2026-11-16, da ripetere all'atto perché il repo nel frattempo
cambia:

- **inventario corrente da aggiornare**: `world.md` (elenco con accento e
  vista, conteggio «sette»), `README.md` («otto repo» della sezione canonica,
  «sette adottanti» due volte), `CLAUDE.md` (`/adottanti` «dei sette»),
  `goal.md` (obiettivo 2), `o2/coordinatore-di-gruppi.md` (`abbinamenti` fra
  i repo del gruppo lavoro, nome da correggere già ora);
- **baseline da aggiungere**: `i3/audit-adottanti.md`, senza anticipare il
  cursore mensile;
- **fotografie da preservare**: `i3/audit-adottanti.md` del 2026-11-02
  («`abbinamenti`, atteso al suo posto, non è ancora entrato»),
  `i2/bootstrap-adottanti.md`, `i2/baricentro-kb-adottanti.md` e i fili
  che contano gli adottanti a una data.

## Da verificare all'ingresso

- marker: adattamenti intenzionali, limiti di verifica, commit recepito;
- quartetto README, CLAUDE, Goal e World contro i nodi e
  `i2/bootstrap-adottanti.md`: che fine fanno le regole del `CLAUDE.md`
  attuale (credenziali, dati reali, migrazioni, contratti XML) e la
  documentazione viva di `docs/`;
- perimetro di `view/`: niente credenziali, dati di articoli o copie del
  database;
- vista pubblicata: porta registrata in `o3/presentations.nix` di
  `nixos-lavoro`, dove su `svezia` la prima libera al 2026-11-16 è 8004;
- primo `/adottanti` utile (2026-12-01): il segnale è lo stato del tempo 1,
  il trasloco, letto dal plan locale e dal task host di `nixos-lavoro`.
