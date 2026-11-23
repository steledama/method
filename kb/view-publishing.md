---
stato: bozza
---

# View publishing

Come le viste derivate raggiungono un lettore: la build che le produce, il
servizio che le espone sulle reti private, la pubblicazione da un commit pulito
e lo stato operativo che si legge a richiesta. La disciplina a cui una vista
risponde — derivata, verificata, non più vecchia delle sue fonti — vive in
`view`; qui sta il contratto operativo che la realizza, portabile fra host e
sistemi diversi.

## HTML apribile direttamente e build minima

Il formato operativo minimo è un HTML con path relativi, generato dalla build e
apribile con doppio click o `xdg-open view/index.html`. Dopo la build non
richiede deploy, servizi permanenti o `fetch` di file locali, che i browser
bloccano sotto `file://`. Chi non ha il toolchain consulta la vista pubblicata.

La build è versionata in `o3/view/`, con lo **stesso path in ogni repo**:
chi passa da un progetto all'altro, umano o agente, non deve scoprire dove
stanno i builder, e le skill citano un solo comando. I builder sono canone
e stanno in `method`: l'adottante li lancia dal checkout del canone sul
proprio repo, `python3 method/../o3/view/build.py --root .`, e in `o3/view/`
tiene solo ciò che è suo, cioè `project.py`, i moduli di dominio e i test.
Una copia dei builder nell'adottante deriva dal canone senza che nessuno lo
veda; finché esiste si lancia quella, e la build dal canone rifiuta di
mescolarsi con lei. L'entrypoint è unico,
`python3 o3/view/build.py`: verifica i contratti fra le fonti, rigenera
pagine, deck, home e asset, e chiude col presidio del compartimento stagno.
Scrive sempre in una cartella temporanea e copia in `view/` solo a esito
riuscito, così un errore tardivo non lascia una vista a metà; `--check`
verifica senza scrivere, `--publish` pubblica («Pubblicazione»). È Python e non shell perché deve girare anche sugli host Windows; non ha
dipendenze oltre a Pandoc e Prettier. I CSS canonici (`page.css` per le
pagine, `system-image.css` per la home, `deck.css` per il deck) vivono accanto
ai builder e la build li copia in `view/assets/`. Due generazioni consecutive
producono lo stesso output: il determinismo rende la rigenerazione un gesto
meccanico invece di una decisione.

Le viste sono uniformi fra i progetti: a distinguerle sono la **sigla** e un
**colore d'accento** unico per progetto. Sigla, lingua, accento, descrizioni degli stadi sulla home, deck ed
esclusioni si dichiarano in un solo file, `o3/view/project.py`; la build
scrive l'accento in `view/assets/theme.css`. La home resta minimale, pura
affordance di navigazione: i register in sintesi, i sei stadi verso i loro
indici, il deck come voce a sé.

## Servizio sulle reti private

Per aprire l'anteprima da un altro PC delle reti private, lo stesso comando in
ogni repo e su ogni sistema (su Windows `py o3\view\serve.py`):

```bash
python3 o3/view/serve.py
```

Il server usa solo la libreria standard e serve la sola cartella servita,
chiusa su se stessa: niente dotfile, niente elenchi di cartella. Ascolta per
default sulla porta 8000 (`--port`, `--bind`) e si chiude con Ctrl-C. Non tocca
il firewall: da un altro dispositivo la porta deve essere ammessa per le sole
reti private, mai per la rete pubblica.

Un servizio permanente è legittimo alle condizioni che conservano il vincolo
dell'artefatto autonomo:

- **consumatori reali**: persone nelle reti private che consultano lo stato del
  progetto senza il checkout. Senza di loro il servizio non nasce;
- **un solo host privilegiato per progetto**, così non circolano rese di
  checkout a versioni diverse. Se l'host è un ruolo (la produzione di una
  coppia di server), il servizio segue il ruolo;
- **servizio utente**, gestibile da un agente senza privilegi, disponibile dopo
  il riavvio e senza sessione interattiva;
- **solo reti private**: le porte le ammette il firewall dell'host, il server
  non le apre;
- **pubblicazione da commit pulito**, col contratto della sezione seguente, e
  nessuna copia mantenuta a mano: i builder e `serve.py` sono quelli del
  checkout, del repo o del canone;
- **esposizione dichiarata**: un server sempre acceso e senza autenticazione
  espone le viste in modo continuo. L'adottante lo registra dove tiene i propri
  vincoli sui dati — cosa entra nel perimetro e chi lo vede.

Host, porte, configurazione del servizio e innesco della pubblicazione (dopo un
pull manuale o un aggiornamento automatico) sono materia dell'host, non del
canone.

## Pubblicazione

`python3 o3/view/build.py --publish DIR` pubblica in una cartella dell'host,
fuori dal checkout, e `python3 o3/view/serve.py --publish-root DIR` la serve.
Il contratto è portabile, indipendente dal sistema dell'host:

- **ultima vista buona**: si costruisce in una cartella a parte e si pubblica
  solo l'esito riuscito, con uno scambio atomico anche su Windows. Un errore,
  anche tardivo, lascia servita la versione precedente; una richiesta già
  iniziata finisce sulla versione con cui è partita;
- **fonti pulite**: la vista pubblicata deriva da un commit, esportato senza
  modifiche locali né file non tracciati e costruito coi builder di quel
  commit. Se il commit non li porta, i builder si esportano allo stesso modo
  dal commit corrente del checkout del canone, mai dal suo working tree. Un
  pull o un edit durante la build non mescolano le revisioni;
- **provenienza**: la home pubblicata espone l'hash del commit costruito e il
  toolchain che l'ha resa, registrati anche in un file accanto all'output.
  Quando i builder vengono dal canone la versione è la coppia dei due
  commit: la home li espone entrambi, e un canone avanzato fa ricostruire
  lo stesso commit;
- **recupero**: all'avvio si pubblica se l'output manca o è arretrato.
  L'innesco a evento dopo un aggiornamento delle fonti può perdere un
  cambio che arriva mentre una pubblicazione si chiude: lo affianca un
  controllo periodico, idempotente e quasi gratuito quando il commit è già
  servito, che recupera anche un errore transitorio. Più
  richieste concorrenti si serializzano, e l'ultimo commit richiesto viene
  infine pubblicato, anche dopo una build fallita. Senza alcuna versione valida
  il server non parte, dice perché ed esce con un codice proprio; se una
  versione c'è, continua a servirla e rende consultabile l'errore (`/_stato`);
- **lo scambio ricarica le viste, non il server**: il processo che serve tiene
  il codice caricato all'avvio. Un commit che cambia `serve.py` o i moduli
  locali che importa (oggi `ciclo`, `project`, `sources`) arriva in
  esercizio solo dopo un riavvio, e l'innesco dell'host deve prevederlo: per
  esempio un riavvio quando cambia l'impronta del codice di `o3/view/`
  rispetto a quella caricata, compresa quella di `o3/view/` del canone se il
  servitore viene da lì. Senza, una rotta nuova risponde 404 finché un
  riavvio a mano non la porta in esercizio. Il riavvio che il servitore chiede
  uscendo da sé non va affidato al solo riavvio-su-errore del supervisore
  dell'host, che può non scattare: lo affianca un innesco periodico che
  rilancia il servizio se non gira, come il controllo periodico affianca
  l'innesco a evento. Su `danea2` un'uscita per builder cambiati ha lasciato
  le viste ferme dal 13 al 16/11/2026 (`danea-auto`,
  `i2/servizio-viste-fermo-2026-11-13.md`);
- **verifica distinta dalla freschezza**: un audit controlla separatamente
  build e contratti sulle fonti, revisione servita rispetto al riferimento
  remoto aggiornato, raggiungibilità della porta. Hash uguali non provano un
  rendering corretto; una porta irraggiungibile è «non verificata», non fresca
  per presunzione.

## Sito di gruppo

Un gruppo è un'istanza del metodo più i repo che coordina: si consulta da un
solo sito, non da una porta per repo. L'istanza dichiara i membri nel
proprio `world.md`, in una sezione `## Membri` con una voce per repo e il
nome del checkout in grassetto. La build dell'istanza la rende in
`view/gruppo.json`, così anche l'elenco servito viene da un commit pulito;
un `world.md` senza la sezione non è un'istanza di gruppo.
L'istanza non è un repo apposito: è uno dei repo del gruppo, eletto a
coordinarlo, perché un repo che tiene solo l'elenco dei membri costa più di
quanto rende. Se scrive sui membri, la sua visibilità non deve essere più
aperta della loro.

Il sito non ricostruisce nulla. Ogni membro, istanza compresa, pubblica la
propria vista col contratto della sezione precedente, in una cartella per
repo sotto una base comune; `serve.py --gruppo BASE --istanza NOME` instrada:

- `/` è la home del gruppo, composta a ogni richiesta dall'elenco pubblicato
  dell'istanza e dalle viste pubblicate dei membri (titolo, accento,
  presentazione). Un membro senza versione valida resta in elenco, dichiarato
  non pubblicato;
- `/<repo>/` è la versione pubblicata di quel repo, `/<repo>/_stato` il suo
  stato di pubblicazione. Il compartimento stagno di ogni vista ne permette
  la resa sotto un prefisso senza ricostruirla;
- un'istanza senza membri serve sé sola: è il caso minimo da cui il gruppo
  cresce.

Il servizio di gruppo sostituisce quelli dei repo membri: un repo del
gruppo non tiene anche una porta propria. La porta è una sola e la dichiara
l'host, nel registro del gruppo, al posto di una porta per repo.

Il server di gruppo dipende solo dalla pubblicazione dell'istanza, che porta
l'elenco dei membri; i membri pubblicano per conto proprio. Portare al gruppo
lo schema per repo, un server che aspetta il proprio publisher e un publisher
che a fine corsa riavvia il server, dà un server che aspetta tutti i
publisher: ogni fine pubblicazione lo riavvia mentre si sta ancora
attivando, lui tira di nuovo i publisher già conclusi, e il gestore dei
servizi lo ferma per troppi avvii (riscontro di `nixos-lavoro` su `svezia`,
2026-11-23). Il canone non è membro dei
gruppi: le istanze lo adottano, e la sua vista resta a sé.

La home elenca le proposte da decidere: i task `o2/`
col campo `decidere:`, letti dalla release perché versionati, raggiungibili
finché restano aperti. Da lì si apre `autonomy.md`, il
register della delega, reso come pagina accanto a `goal.md` e `world.md` ma
senza un polo: non è uno stadio del ciclo. Una proposta che aspetta il custode resta raggiungibile dalla sezione fissa.

È visibilità e feedback nel senso del ciclo d'azione (`action-cycle`): un
ambito di autonomia senza uno strumento che lo renda valutabile apre il
golfo di valutazione che l'artefatto dovrebbe chiudere.

Connessioni:

- [view](view.md)
- [presentation](presentation.md)
- [action-cycle](action-cycle.md)
- [constraint](constraint.md)
- [project-structure](project-structure.md)
- [method-development](method-development.md)
