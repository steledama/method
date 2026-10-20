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

- **nixos**: ha la copia integrale (sezione con sei passi e clausola
  «altri repo, host, sudo o rebuild»); va ridotta al rimando tenendo la
  clausola.
- **bi**: recepita nella sessione della decisione, con la clausola su
  produzione e rilasci, scritture di dominio, invii e ordini.
- **baserow**: la clausola deve nominare l'infrastruttura Docker e il
  checkout servito su `svezia`.
- **crm**: verso la dismissione; recepisce se resta in uso con sessioni
  aperte in Herdr.
- **economia**, **salute**, **danea-auto**: nessun protocollo oggi; sezione
  nuova.

## Verifica

`grep -n "session-messaging" CLAUDE.md` trova il rimando in ogni adottante e
nessun `CLAUDE.md` contiene più `herdr agent prompt`: il protocollo vive solo
nel nodo. All'audit `/adottanti` la prescrizione esce dall'indice quando i
sette l'hanno recepita.
