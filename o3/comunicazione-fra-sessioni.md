---
data: 2026-10-20
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, baserow, danea-auto
---

# Le sessioni si parlano con Herdr, protocollo nel canone

## Cosa e perché

Il custode ha deciso il 2026-10-20, nella sessione `bi`, che la
comunicazione fra sessioni d'agente passi da Herdr e non dagli strumenti di
messaggistica interni all'harness: il canale resta agnostico rispetto a
harness e modello, quindi copre Codex e qualsiasi altro agente in un
terminale, senza legare il metodo a un fornitore. Il protocollo esisteva già
come sezione quasi identica nei `CLAUDE.md` di `method` (`f379aee`) e
`nixos`; gli altri adottanti non lo avevano, e un agente senza la regola
ricadeva sugli strumenti nativi.

Il canone ora tiene il protocollo nel nodo
[session-messaging](../kb/session-messaging.md): verifica di `HERDR_ENV`,
destinatario ricavato da `herdr agent list` e confermato leggendo il
pannello, nessun pane ID fisso, `blocked` riportato al custode, invio con
conferma del turno e niente reinvii alla cieca. Gli adottanti non lo copiano:
lo richiamano.

## Ricetta per il /method locale

1. **`CLAUDE.md`**: una sezione «Comunicazione fra sessioni con Herdr» di
   due paragrafi brevi:
   - la regola: su richiesta del custode di passare un messaggio a un'altra
     sessione aperta si usa Herdr, non gli strumenti interni all'harness;
     protocollo nel nodo `session-messaging` di method, citato nella forma
     che il repo usa per i nodi del canone (symlink `method/` o path del
     clone `~/method/kb/`);
   - la clausola locale: il messaggio si dichiara inoltrato dalla sessione
     del repo, conserva regole e autorizzazioni del destinatario e non
     estende la delega del repo. Elencare i riservati del dominio che il
     collegamento non sblocca (produzione, rilasci, invii, ordini, host,
     altri repository: quelli che il repo ha davvero).
2. Se il repo ha già una copia integrale del protocollo, sostituirla con la
   sezione breve: le differenze locali sopravvivono solo nella clausola.
3. `AGENTS.md` resta un wrapper e non duplica la regola.
4. Registrare il recepimento nel marker `i3/allineamento-metodo.md`.

## Indizi da verificare sul posto

- **nixos**: recepita (`228e8b2`), copia integrale ridotta al rimando con
  la clausola su altri repo, host, sudo e rebuild.
- **bi**: recepita (`601acd48`) nella sessione della decisione, con la
  clausola su produzione e rilasci, scritture di dominio, invii e ordini.
- **baserow**: recepita (`2eda4d5`), clausola su infrastruttura Docker,
  checkout servito su `svezia`, standby `norvegia`, host e altri repository.
- **danea-auto**: Herdr gira anche su `danea2`. Il custode l'ha collaudato il
  2026-10-20 dal pacchetto Chocolatey `herdr`: comunitario, ma scarica lo zip
  ufficiale delle release `herdrdev/herdr` con checksum. Il canale collega
  le sessioni dello stesso host, per esempio `danea-auto` e il clone di
  `method` su `danea2`, e attenua la differenza fra Windows e Linux. La
  clausola nomina i riservati del repo (scheduler, export Danea, `controlp`).
  Dove il repo documenta i pacchetti Chocolatey dell'host, aggiungere
  `herdr`. Su Windows il riconoscimento degli agenti è meno preciso che su
  Linux e la directory corrente in PowerShell può non aggiornarsi: il
  destinatario si conferma sempre leggendo il pannello.
- **economia**, **salute**: nessun protocollo oggi; sezione nuova.
- **crm**: in sospeso. È verso la dismissione e il custode attende la
  conferma di un collega per toglierlo dai target.

## Verifica

`grep -n "session-messaging" CLAUDE.md` trova il rimando in ogni adottante e
nessun `CLAUDE.md` contiene più `herdr agent prompt`: il protocollo vive solo
nel nodo. All'audit `/adottanti` la prescrizione esce dall'indice quando i
sette l'hanno recepita.
