---
stato: bozza
---

# Consent

Principio che governa la cadenza con cui l'agente passa dalla proposta
all'azione: riconoscere l'autorità già concessa, chiedere consenso esplicito
quando manca, e non scambiare un assenso parziale per un assenso totale.
L'autorizzazione può essere dichiarata dal custode nella richiesta corrente o
nelle regole operative del repository; entro quel perimetro l'agente agisce
senza una seconda cerimonia. Quando l'atto esce da quel perimetro, è difficile
da annullare o incontra il Mondo, formula prima la proposta e attende il via. Un
sì su una parte non autorizza il tutto.

Non è cautela burocratica ma la disciplina della cerniera tra esecuzione e
valutazione nel ciclo dell'azione. Il custode chiude il cappio — fissa il
Goal e giudica l'esito; l'agente propone il piano e lo specifica, ma il
passaggio all'azione nel mondo è il punto in cui l'autorità si trasferisce e va
riconosciuta esplicitamente. Saltare il consenso significa attraversare il gulf
of execution senza che il custode abbia attraversato quello di valutazione sulla
proposta: l'agente agisce su un'intenzione presunta, non confermata. È
l'asimmetria di autorità tra i due agenti del sistema, resa procedura.

Il principio è tanto più stringente quanto più l'atto è irreversibile o rivolto
all'esterno — una mail spedita, una transazione, un commit pubblicato: lì il
consenso esplicito è un vincolo, non una cortesia. Ha un gemello sul lato
valutazione, la guardia contro il sostituire la memoria alla verifica: prima di
affermare o comunicare un fatto, controllarlo alla fonte invece di fidarsi del
ricordo. Entrambe difendono lo stesso confine — l'agente non deve trasformare
una presunzione in un atto compiuto.

Quando l'agente lavora senza il custode, il consenso non può più accadere nel
momento e si sposta nel registro. Ogni commit dichiara se è `concordato` o
dell'`agente`, e un commit dell'agente dichiara l'**impatto** — basso, medio,
alto — e il **motivo** che l'ha determinato. Basso e medio si applicano, e il
medio chiede uno sguardo dopo; l'alto resta proposta committata e non
applicata, perché è proprio l'atto in cui l'autorità dovrebbe trasferirsi e
nessuno era lì a trasferirla. La forma dei trailer vive nella skill di commit.

Il livello dipende dalla natura della modifica, non dal tipo di file: un fix
che ripara un difetto evidente nel codice di produzione pesa poco, una
funzionalità nuova sullo stesso file è un'iniziativa da valutare insieme. Per
questo il criterio verificabile fissa il livello minimo e il giudizio
dell'agente può solo alzarlo. I criteri partono severi e si allentano coi
casi.

Un errore di stima è atteso, ed è materia per affinare i criteri. Ciò che non
si tollera è un livello di cui non si può ricostruire la ragione: il motivo
nomina il criterio e ciò che l'ha fatto scattare, o il giudizio che ha alzato
il livello. Lo stato dei criteri in quel momento è il register a quel commit,
e la storia di git lo conserva. Impatto è una proprietà del commit; il
semaforo che lo veste nelle viste è presentazione, riusabile per altre
proprietà a tre gradi.

Caratteristiche:

- riconoscere l'autorità già dichiarata nella richiesta e nelle regole operative
- proporre e attendere un assenso esplicito quando l'atto non è già autorizzato
- ambito limitato: un consenso parziale non si estende al tutto
- soglia proporzionata: massima per atti irreversibili o verso il mondo, minima
  per esplorazioni reversibili e interne
- gemello sul lato input: verificare i fatti alla fonte prima di affermarli,
  specie prima di comunicazioni esterne
- senza custode, consenso differito: impatto e motivo ricostruibile in ogni
  commit dell'agente, l'alto resta proposta

Esempi:

- in `economia`, mostrare la bozza di ogni mail e attendere conferma esplicita
  prima di inviarla; e verificare pagamenti, importi e intestazioni sui
  movimenti del repo prima di asserirli, soprattutto verso commercialista o
  avvocato
- in una sessione metodologica, modificare file e storia quando `CLAUDE.md` o la
  richiesta lo autorizzano; chiedere il via prima di ampliare lo scope o agire
  verso il Mondo

Connessioni:

- [action-cycle](action-cycle.md)
- [agent](agent.md)
- [design-principles](design-principles.md)
- [method-development](method-development.md)
- [cognitive-fidelity](cognitive-fidelity.md)
