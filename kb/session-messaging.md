---
stato: bozza
---

# Session messaging

Canale con cui una sessione d'agente passa un messaggio a un'altra sessione
aperta, su richiesta del custode. Il metodo lo vuole agnostico rispetto a
harness e modello: la popolazione di agenti comprende Claude Code, Codex e
qualsiasi altro agente in un terminale, e un canale nativo di un solo harness
ne coprirebbe una parte sola, legando il metodo a un fornitore. Lo strumento
corrente è Herdr, il multiplexer di terminali che riconosce gli agenti nei
pannelli e li espone con la CLI `herdr`; gli strumenti di messaggistica
interni all'harness non si usano per questo scopo, anche quando sono
disponibili.

Il messaggio arriva come prompt nel pannello del destinatario: è testo, non
un oggetto strutturato, e la risposta non torna da sola, si legge dal
pannello. Il canale serve quindi a passare un'informazione o una richiesta
puntuale. Una coordinazione che deve durare oltre la conversazione vive nelle
collezioni versionate — un task `o2/`, un filo `i3/`, una cattura `i1/` — e il
messaggio si limita a segnalarla.

Il collegamento non sposta autorità. Il destinatario conserva regole,
autorizzazioni e delega del proprio repository; il mittente non ottiene
permessi nuovi su altri repository, host o atti sul Mondo per il fatto di
poter scrivere in un altro pannello, e non risponde mai al posto del
destinatario a un dialogo di approvazione.

## Protocollo

- l'invio richiede la richiesta esplicita del custode; il messaggio dichiara
  da quale sessione è inoltrato;
- la sessione verifica di essere dentro Herdr con
  `test "${HERDR_ENV:-}" = 1`; se fallisce si ferma e lo riferisce;
- legge `herdr --skill` una volta per sessione e l'help della CLI installata
  per la sintassi corrente;
- ricava il destinatario dal JSON di `herdr agent list`, verificando
  directory, agente e stato; nessun pane ID fisso nelle istruzioni, perché
  gli ID seguono i pannelli e non si riusano;
- legge `herdr agent read <pane-id> --source visible` per confermare che il
  destinatario sia quello richiesto e pronto a ricevere; gli ID di
  conversazione dell'harness e i pane ID di Herdr sono identificatori
  distinti, e un ID di conversazione fornito dal custode si confronta quando
  visibile;
- la lettura `visible` può non mostrare il campo di input del destinatario:
  in quel caso lo si verifica con `--source detection`, e un campo che non
  si riesce a vedere conta come non vuoto;
- se il campo di input del destinatario non è vuoto, il testo può essere un
  messaggio scritto e non ancora inviato, del custode o di un altro mittente:
  un invio lo unirebbe al messaggio o lo farebbe partire. In forma testuale non
  si distingue da un suggerimento dell'harness, che un invio sostituisce. Si
  rilegge il pannello con `--format ansi`. Dove la resa del suggerimento è
  verificata per l'harness e la versione del destinatario, un testo con quella
  resa è un suggerimento e si invia; ogni altro testo ferma l'invio e si torna
  al custode. La resa verificata oggi è quella di Claude Code 2.1.303,
  2.1.306, 2.1.308, 2.1.310, 2.1.311 e 2.1.312 (campo vuoto confermato dal
  custode il 2026-10-26 e, per 2.1.311 e 2.1.312, il 2026-10-28): il suggerimento è preceduto da `ESC[2m`, l'attributo dim. Per Codex CLI
  0.163.0, confermata dal custode il 2026-10-25, il campo vuoto mostra il
  suggerimento generico `Ask Codex to do anything` in dim dopo il prompt `›`,
  che un invio sovrascrive; le righe `›` più in alto nel pannello sono
  messaggi già inviati della cronologia, non il campo. Senza verifica vale
  la regola prudente: qualunque testo nel campo di input ferma l'invio;
- un agente `blocked` ha un dialogo aperto: lo si legge e si torna al
  custode, senza approvarlo;
- invia con `herdr agent prompt <pane-id> "<messaggio>"`; su un agente
  inattivo aggiunge `--wait --until working --timeout 10000`, perché la
  conferma d'invio non prova che il turno sia partito; dopo timeout o errore
  rilegge stato e pannello prima di ritentare, per non inviare due volte;
- se la sandbox blocca il socket di Herdr chiede l'escalation per il solo
  comando necessario.

## Nel repository adottante

`CLAUDE.md` tiene una sezione breve che rimanda a questo nodo e aggiunge la
clausola locale: quali deleghe del repository il collegamento non estende
(produzione, rilasci, invii, host, altri repository). Il protocollo non si
copia: vive qui e si aggiorna una volta sola.

Connessioni:

- [agent](agent.md)
- [consent](consent.md)
- [claude](claude.md)
- [cognitive-system](cognitive-system.md)
- [tasks](tasks.md)
- [verdict](verdict.md)
- [agent-as-user](agent-as-user.md)
