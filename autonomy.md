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
delle collezioni. Include gli interventi già autorizzati e i controlli
necessari. Un arco chiude col proprio esito e la proposta di commit; commit e
push, nei limiti di `CLAUDE.md`, li compie `/commit` quando li chiede il
custode o la composta.
Una voce nel plan non autorizza da sola qualsiasi atto di dominio.

Criterio `momento-del-commit`, deciso il 2026-10-11 da Stefano. Nella
sessione interattiva il momento del commit si concorda: le decisioni in
discussione restano aperte ad aggiustamenti e ripensamenti. L'agente
propone il commit quando un punto si è fermato; lo fa di propria
iniziativa, dichiarandolo, solo se un lettore fuori dalla sessione ne ha
bisogno, come un adottante che recepisce o un'altra sessione. Il ciclo
chiesto esplicitamente fino al commit lo include. Il push segue ogni
commit senza conferma.

L'agente verifica le fonti, esplicita provenienza e incertezza e conserva il
presidio delle ipotesi. Una tesi nuova può essere registrata come ipotesi;
non diventa un fatto certo per rendere eseguibile una decisione.

Impatto minimo **medio** per le decisioni autonome del ciclo: il motivo del
commit cita `ciclo-delegato` e i fatti che lo rendono applicabile. Il giudizio
può alzarlo. Nel resoconto finale compaiono decisioni, motivazioni, verifiche,
incertezze e questioni lasciate al custode. La presenza umana in chat non
trasforma una decisione dell'agente in una decisione concordata.

## Ciclo autonomo senza custode

Criterio `ciclo-autonomo`, deciso il 2026-10-16 da Stefano, gradino 0;
gradino 1 deciso il 2026-10-17: il timer lancia un giro ogni giorno alle 15:00.

Il ciclo autonomo è il ciclo congiunto senza custode, la skill `/cycle
autonomo`: lo avvia su `deck` l'unità `ciclo-method` del modulo `cicli` di
`nixos`, con `o3/ciclo/prompt.md` e i permessi di `o3/ciclo/permessi.json`.
Nessuno risponde durante il giro, e ciò che in sessione si chiederebbe
diventa proposta nel task `o2/` pertinente. Resta fuori da
`momento-del-commit`: un commit per giro, con `Esiti`, `Autonomia: agente`,
impatto almeno **medio** e `Impatto-motivo:` col criterio e il gradino
dichiarati dal prompt. Al gradino 1 il timer di `nixos` avvia il giro; un
avvio a mano dell'unità resta coperto da questo criterio. Tetto per
giro, 45 minuti e 5 USD, nell'unità.

Il giro tiene vivi catture, letture, fili, plan, task e i nodi di `kb/`. Un
nodo arriva subito agli adottanti via symlink: si corregge solo su una fonte
verificata e il resoconto dichiara ogni nodo toccato. Una prescrizione che
tutti i marker danno recepita il giro la chiude da sé con
`o3/prescrizioni.py chiudi` e corregge i rimandi (deciso dal custode il
2026-10-26: è l'esecuzione di una regola del canone, non una scelta). Restano
proposte le altre modifiche alle prescrizioni, gli strumenti in `o3/`, le skill canoniche, `presentation/`,
`CLAUDE.md`, `AGENTS.md`, questo register e `goal.md`; `/adottanti` e
`/method` non girano nel giro. Gli adottanti si leggono dai marker nei
checkout locali di `deck`, o da `origin` via `fetch` per quelli di `svezia`,
senza `ssh`; lo stato dei giri da `i1/giri/` o da `~/.local/state/ciclo/`, trascritti degli adottanti esclusi. Il divieto sta nei deny del solo
`o3/ciclo/permessi.json`; nelle sessioni col custode restano le regole di sopra.

Sospensione: si torna al manuale dopo un rosso per atto fuori delega, per un
nodo `kb/` che altera il senso del canone senza fonte o per una ricostruzione
sbagliata che altera una decisione. Lo stop per sessione aperta, il push
rifiutato e il lock occupato sono il sistema che funziona.

## Decisioni riservate e arresto parziale

Criterio `confine-delega`: restano in proposta cambi di scopi, territorio o
criteri di autonomia, atti oltre le autorizzazioni vigenti e decisioni con
incertezza decisiva non risolvibile dalle fonti disponibili. L'agente chiede
la decisione sul punto e prosegue il lavoro indipendente. Impatto alto per
una proposta che cambia i confini costitutivi; l'incertezza da sola non è
un'autorizzazione e non richiede di rendere alta ogni altra modifica.

Una proposta persistente vive nel task `o2/` pertinente, indicizzato e
collegato al plan: il campo `decidere:` del frontmatter ne dice la questione
in una frase, il corpo alternative, motivo e decisione richiesta. La home la
elenca finché il campo c'è (forma decisa il 2026-10-25 da Stefano). Il
resoconto la collega. Se serve un task nuovo si applica la forma
ordinaria di `o2/`; non si aggiunge una collezione. Il commit della proposta
non applica l'atto. Accettata, entra nel lavoro autorizzato; respinta, si
consuma conservando il razionale durevole dove pertinente e la storia in Git.
In entrambi i casi il campo `decidere:` si toglie e il corpo registra la
decisione con la data.

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

`ciclo-delegato` riguarda i cicli avviati dal custode, `ciclo-autonomo` il
giro senza custode nei limiti sopra. Nessuno dei due copre `/method`: il
recepimento del canone negli adottanti conserva il proprio gate di conferma.
I gradini successivi seguono il
[percorso del pilota](o2/pilota-ciclo-autonomo.md). Il custode può restringere o
revocare la delega; il register e Git ne conservano lo stato e la storia.
