# Autonomia

Il custode conserva scopi, territorio e condizioni della delega. L'agente
conduce il ciclo operativo nel perimetro concesso e ne rende leggibili gli
esiti. Questo register raccoglie i criteri concordati, modificabili dal
custode; non concede permessi sugli adottanti o sulle superfici esterne.

## Ciclo delegato dal custode

Criterio `ciclo-delegato`, ratificato il 2026-10-09 da Stefano.

Quando il custode avvia `eval`, `exec` o il ciclo congiunto, l'agente compie
gli scope richiesti e applica gli esiti ordinari senza conferme intermedie.
Una richiesta esplicitamente diagnostica o «solo proposte» restringe il mandato.
Nel ciclo congiunto conserva l'ordine `eval → exec → commit`; l'invocazione
di un solo arco non estende automaticamente lo scope all'altro.

La delega comprende catture pertinenti, sintesi e correzioni delle letture,
verdetti sui goal vigenti, priorità, dipendenze, specifiche dei task e igiene
delle collezioni. Include gli interventi già autorizzati, i controlli
necessari e la chiusura con commit e push nei limiti di `CLAUDE.md`.
Una voce nel plan non autorizza da sola qualsiasi atto di dominio.

L'agente verifica le fonti, esplicita provenienza e incertezza e conserva il
presidio delle ipotesi. Una tesi nuova può essere registrata come ipotesi;
non diventa un fatto certo per rendere eseguibile una decisione.

Impatto minimo **medio** per le decisioni autonome del ciclo: il motivo del
commit cita `ciclo-delegato` e i fatti che lo rendono applicabile. Il giudizio
può alzarlo. Nel resoconto finale compaiono decisioni, motivazioni, verifiche,
incertezze e questioni lasciate al custode. La presenza umana in chat non
trasforma una decisione dell'agente in una decisione concordata.

## Decisioni riservate e arresto parziale

Criterio `confine-delega`: restano in proposta cambi di scopi, territorio o
criteri di autonomia, atti oltre le autorizzazioni vigenti e decisioni con
incertezza decisiva non risolvibile dalle fonti disponibili. L'agente chiede
la decisione sul punto e prosegue il lavoro indipendente. Impatto alto per
una proposta che cambia i confini costitutivi; l'incertezza da sola non è
un'autorizzazione e non richiede di rendere alta ogni altra modifica.

Una proposta persistente vive nel task `o2/` pertinente, indicizzato e
collegato al plan, con stato «da decidere», alternative, motivo e decisione
richiesta. Il resoconto la collega. Se serve un task nuovo si applica la forma
ordinaria di `o2/`; non si aggiunge una collezione. Il commit della proposta
non applica l'atto. Accettata, entra nel lavoro autorizzato; respinta, si
consuma conservando il razionale durevole dove pertinente e la storia in Git.

## Casi che delimitano il criterio

- Un riscontro verificato smentisce un filo: correggere filo, letture
  dipendenti e priorità, verificare e committare; `ciclo-delegato`, medio.
- Un dato ambiguo non permette di decidere se chiudere un'ipotesi: registrare
  il limite e chiedere sul punto, continuando il resto del ciclo.
- Una nuova direzione richiede di cambiare Goal o territorio: predisporre
  la proposta, `confine-delega`, alto; il custode decide.
- Un task propone un invio, un rilascio o un intervento in un adottante:
  verificare l'autorità specifica. La delega del ciclo non la sostituisce.

## Supervisione e sviluppo successivo

Il primo controllo è il resoconto del ciclo con diff e commit consultabili;
la concordanza frequente dichiarata dal custode motiva la riduzione
dell'attrito, non certifica la qualità. I riesami a campione confrontano le
ricostruzioni con le fonti, secondo il filo
[ricostruzione delegabile](i3/verdetto-piu-sicuro-del-materiale.md).

Questa delega riguarda cicli avviati dal custode. Non copre `/method`: il
recepimento del canone negli adottanti conserva il proprio gate di conferma.
Il battito schedulato,
la sua visibilità anche senza commit e l'estensione dei criteri attendono
il [percorso del pilota](o2/pilota-battito.md). Il custode può restringere o
revocare la delega; il register e Git ne conservano lo stato e la storia.
