---
sintesi: "Chi serve cosa lo decide oggi nixos (o3/presentations.nix), fuori dai repo serviti. Proposta da nixos il 2026-10-31: il repo dichiara dove si pubblica, il metodo fissa il contratto agnostico, l'host una porta sola con un servitore per tutti i checkout che lo nominano. Valutata: direzione coerente col lanciatore, cinque punti da decidere."
ciclo: dev
decidere: "Adottare SERVITA_SU nel repo e una porta sola per host, e con quale forma del servitore (multi-root o smistatore davanti ai servitori per repo)?"
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

## Valutazione del 2026-10-31

La direzione è quella che il custode ha già chiesto per il ciclo autonomo
([lanciatore](lanciatore-ciclo-nel-metodo.md)): il repo decide cosa, il
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
  (`danea-auto`).

## Effetti sul canone

Se il custode adotta: `kb/view.md` cambia la frase «Host, porte,
configurazione del servizio … sono materia dell'host» nel confine a tre;
`project.py` canonico riceve il campo; `serve.py` o lo smistatore crescono
nel metodo; una prescrizione porta campo e codice agli adottanti. Poi
`nixos` adegua il modulo home e toglie le porte per repo da
`o3/presentations.nix`, nella propria sessione.

## Criterio di chiusura

Il custode decide i punti sopra. Il contratto è in `kb/view.md`, il campo e
il servitore girano in `method` e in un adottante su un altro sistema
operativo, la prescrizione è aperta. Riga del plan, voce in `o2/tasks.md` e
questo file si rimuovono nello stesso commit.

Connessioni:

- [view](../kb/view.md)
- [lanciatore-ciclo-nel-metodo](lanciatore-ciclo-nel-metodo.md)
- [uscita-dal-deck](uscita-dal-deck.md)
