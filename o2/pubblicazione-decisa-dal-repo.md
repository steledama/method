---
sintesi: "Chi serve cosa lo decide oggi nixos (o3/presentations.nix), fuori dai repo serviti. Adottato dal custode il 2026-11-08: il repo dichiara dove si pubblica con un valore solo, una porta per host con uno smistatore davanti a un servitore per repo, un elenco dei checkout ammessi sull'host. Il lanciatore da cui dipendeva è in esercizio: da implementare."
ciclo: dev
---

# Pubblicazione decisa dal repo

## Origine

Proposta della sessione `nixos` su `deck`, inoltrata via Herdr su richiesta
del custode il 2026-10-31, discussa col custode in quella sessione. Il
messaggio non porta autorizzazioni nuove.

## Oggi

`kb/view.md` («Servizio sulle reti private») lascia all'host porte,
configurazione e innesco, e chiede un solo host privilegiato per progetto.
In esercizio è `nixos` a dirlo, in `o3/presentations.nix`: repo → host →
porta. Il repo servito non sa di esserlo.

## La proposta

Tre livelli:

1. **Repo**: in `o3/view/project.py`, accanto a `ESCLUSE`, `SERVITA_SU` dice
   se e dove il repo si pubblica, per nome di host o ruolo; vuoto è spento.
2. **Metodo**: `build.py --publish` e il servitore, il vincolo delle sole
   reti private, il contratto dell'host che ospita: rispettare
   `SERVITA_SU`, servire la cartella pubblicata, aprire il firewall solo
   alle reti private.
3. **Host**: una porta per host (scelta del custode), un servitore unico
   che serve sotto `/<repo>/` ogni checkout che lo nomina, trovato per
   convenzione (i repo nella home) senza elenco. L'host dichiara chi è,
   nome e ruoli; il suo veto resta clonare, eseguire, la porta.

Accendere e spegnere diventa un commit nel repo, senza rebuild.

## Decisioni del custode (2026-11-08)

Adottata la direzione, da eseguire dopo il lanciatore (`o3/lanciatore.py`,
in esercizio dal 2026-11-09), con queste scelte sui punti
sotto:

- **Un solo host privilegiato:** `SERVITA_SU` è un valore solo, host o ruolo,
  controllato dalla build.
- **Forma del servitore:** una porta per host, con uno smistatore canonico
  davanti a un servitore per repo, ciascuno col codice del suo checkout.
- **Ammissione:** un elenco sull'host dice quali checkout può eseguire, distinto
  da `SERVITA_SU`: sono due consensi diversi. È anche ciò che dice allo
  smistatore quali servitori avviare.

Restano da fissare nell'implementazione chi risolve i ruoli e il
sotto-percorso delle pagine del ciclo.

## Valutazione del 2026-10-31

La direzione è quella che il custode ha già chiesto per il ciclo autonomo
(il lanciatore, `o3/lanciatore.py`): il repo decide cosa, il
metodo fissa un contratto indipendente dal sistema operativo, l'host è un
adattatore minimo. Le due proposte condividono il confine a tre e la
domanda sul codice eseguito da un checkout; conviene deciderle con lo
stesso criterio. Punti da decidere:

- **Un solo host privilegiato.** Una lista `["deck"]` permette due host e
  quindi due rese a versioni diverse, che il canone vieta. Proposta: un
  valore solo, `SERVITA_SU: str | None`, host o ruolo, controllato dalla
  build.
- **L'interruttore è un atto sull'esposizione.** Oggi accendere un servizio
  chiede un atto su `nixos`; con la proposta basta un commit nel repo, e con
  la porta già aperta l'host non ha un secondo atto. È voluto, ma sposta
  il presidio: `project.py` deve restare fuori dalla scrittura del giro
  autonomo. Oggi lo è (`Edit(./o3/**)` e `Write(./o3/**)` nei deny di
  `o3/ciclo/permessi.json`, verificato), e la rete in chiusura proposta
  per il lanciatore lo coprirebbe anche da `origin`. Le condizioni
  «consumatori reali» ed «esposizione dichiarata» di `kb/view.md` restano
  del repo: lo stesso commit che accende dichiara chi legge e cosa vede,
  in `world.md`. Va evitata la doppia rappresentazione: `world.md` cita
  l'interruttore invece di ripeterlo.
- **Multi-root e codice per repo.** `serve.py` importa `ciclo`, `project`
  e `sources` del proprio checkout, e le rotte vive (`/_ciclo/`, `/_stato`)
  leggono stato e parametri di quel repo. Un processo unico caricherebbe
  una sola versione di quei moduli per tutti i repo, mentre ogni adottante
  ha la propria copia, a volte indietro. Alternativa da pesare: uno
  smistatore canonico sulla porta unica davanti a un servitore per repo,
  ciascuno col codice del suo checkout (porta locale o socket non esposti).
  Riduce anche il punto di guasto unico: cade un repo, non tutte le
  presentazioni dell'host.
- **Sotto-percorso.** Le pagine statiche sono relative e reggono sotto
  `/<repo>/`. Le pagine del ciclo no: `ciclo.py` emette `/assets/…`, `/` e
  `/_ciclo/…` assoluti (righe 414-435 e 575). Vanno resi relativi, o
  lo smistatore toglie il prefisso.
- **Scoperta per convenzione.** Cercare i checkout nella home senza elenco
  evita il doppio interruttore, ma l'host esegue il servitore di ogni
  checkout che lo nomina: è la domanda «Codice privilegiato da un checkout»
  del lanciatore. Su Windows la convenzione della home va dichiarata
  (`danea-auto`). Commento di `nixos` del 2026-10-31: con la sola
  convenzione, qualunque clone sull'host, anche fatto per tutt'altro, gli
  fa eseguire `build.py --publish` e il servitore. Un elenco sull'host
  torna utile con un'altra funzione: non dice dove un repo si pubblica, che
  resta a `SERVITA_SU`, ma quale checkout l'host ammette all'esecuzione. Non
  porta né porte né host, quindi non duplica l'interruttore: sono due
  consensi distinti, il repo che vuole esporsi e l'host che accetta di
  eseguirne il codice. Si decide col punto del servitore: con lo smistatore,
  l'elenco è anche ciò che gli dice quali servitori avviare.

## Evidenza: la vista di `nixos-lavoro` sullo standby

Il 2026-11-05, con nixos d88e297, la vista di `nixos-lavoro` passa dalla
production allo standby, l'host del suo giro autonomo, perché `/_ciclo/` legge
lo stato del giro sull'host locale. È il ponte deciso nel regime di oggi
(`kb/view.md`: il servizio segue il ruolo, host e porte sono materia
dell'host). Va trattato come evidenza e vincolo di compatibilità, non come
decisione sui punti sopra:

- **primo ruolo diverso da production**: `privileged.standby` accanto a
  `privileged.production` in `o3/presentations.nix`, chiave della stessa
  specie e nessun elenco nuovo. Il valore unico di `SERVITA_SU` regge anche
  con questo secondo ruolo;
- **un predicato per ruolo**: `roleCondition` risolve ogni ruolo in una
  condizione di avvio, condivisa da presentazioni e cicli, e un'asserzione
  limita le chiavi di ruolo agli host della coppia. Resta da decidere **chi
  risolve i ruoli**. Con l'host che dichiara nome e ruoli (livello 3), la
  risoluzione è dell'host e il ponte resta valido. Se invece il metodo li
  risolvesse da sé, il ponte andrebbe smontato;
- **la porta è un consenso separato**: il firewall della coppia ammette
  l'unione delle porte di production e standby, ricavata dal registro e
  distinta dall'interruttore. Spostare la vista non ha cambiato il sistema
  (drvPath identico a revisione fissata);
- **la sovrapposizione transitoria**: fra lo switch dello standby e
  l'allineamento della production i due host hanno servito lo stesso
  commit. Il vincolo dell'host unico, che esiste contro le rese a versioni
  diverse, regge se la sovrapposizione si chiude nella stessa sessione.

## Effetti sul canone

Se il custode adotta: `kb/view.md` cambia la frase «Host, porte,
configurazione del servizio … sono materia dell'host» nel confine a tre;
`project.py` canonico riceve il campo; `serve.py` o lo smistatore crescono
nel metodo; una prescrizione porta campo e codice agli adottanti. Poi
`nixos` adegua il modulo home e toglie le porte per repo da
`o3/presentations.nix`, nella propria sessione.

## Criterio di chiusura

Il contratto è in `kb/view.md`, il campo e
il servitore girano in `method` e in un adottante su un altro sistema
operativo, la prescrizione è aperta. Riga del plan, voce in `o2/tasks.md` e
questo file si rimuovono nello stesso commit.

Connessioni:

- [view](../kb/view.md)
