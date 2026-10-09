---
data: 2026-10-09
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, danea-auto, baserow
---

# Delegare il ciclo avviato dal custode

## Decisione e confine

Il custode ha ratificato il governo operativo delegato del ciclo richiesto:
l'agente raccoglie e interpreta segnali, aggiorna verdetti, piano e specifiche,
compie gli interventi già autorizzati e chiude con controlli, commit e push
ove autorizzato, senza conferme intermedie ordinarie. Scopi, territorio,
criteri della delega, atti non autorizzati e incertezze decisive non risolvibili
dalle fonti tornano al custode. Il lavoro indipendente prosegue.

L'agente assume la conduzione operativa del repository; il custode conserva
scopi, territorio e delega. Goal dice che cosa perseguiamo e perché, World
quale territorio consideriamo rilevante, Autonomy quali decisioni e atti
sono delegati. L'autonomia ordinaria vale entro quel perimetro: non è una
whitelist universale di atti sul Mondo.

Il canone è in `kb/consent.md`; `autonomy.md` di `method` ne è la prima
istanza, con criteri `ciclo-delegato` e `confine-delega`. L'avvio umano e la
schedulazione sono due deleghe distinte: questa ricetta non attiva un battito
né concede permessi nuovi su produzione, invii o altri atti di dominio.

## Recepimento tramite /method locale

1. Leggere Goal, World, CLAUDE e i fork delle tre skill. Materializzare
   `autonomy.md` con il perimetro locale della delega: criteri nominati,
   atti, evidenza, impatto minimo, decisioni riservate e arresto parziale.
   Riconoscere l'autorizzazione già data dal custode; chiedere solo se manca
   una decisione sul confine di dominio, senza interpretare `aligned`
   come autorizzazione. Per il ciclo ordinario l'istanza canonica parte da
   impatto medio; il giudizio può alzarlo, non creare autorità.
2. Sostituire in `eval` ed `exec` il gate universale proponi-poi-applica e
   i richiami equivalenti nei singoli passi. Conservare stadi, provenienza,
   presidio delle ipotesi, scope richiesti, ordine `eval → exec` ed esiti
   contabili. Una richiesta solo diagnostica resta tale; il ciclo congiunto
   chiude con `/commit` senza un nuovo assenso per ogni arco.
3. In `/commit` eseguire i controlli necessari e gli aggiornamenti dei fili
   già delegati senza domande rituali. Conservare formatter, verifiche,
   vincoli sui segreti, push e pubblicazione del dominio. `Autonomia:`
   registra chi ha deciso la modifica concreta: `agente` anche in chat con
   il custode, `concordato` per una modifica decisa o ratificata da lui.
   L'agente dichiara impatto e motivo riferito al criterio locale.
4. Rendere raggiungibile il register dal bootstrap. Adeguare il Goal di
   sviluppo alla delega ratificata senza uniformare il motivo di dominio.
   Le proposte riservate vivono nei task pertinenti, indicizzati e nel plan,
   con alternative, motivo e decisione richiesta. Il resoconto le collega;
   il commit della proposta non applica l'atto.
5. Verificare i casi: riscontro che corregge un verdetto (applicare entro
   delega); cambio del nord (proporre); dato decisivo ambiguo (sospendere il
   punto, proseguire il resto); atto sul Mondo (verificare autorità specifica).
   Eseguire i controlli locali e registrare nel marker esito, adattamenti,
   limiti e commit canonico. Il primo giro reale verifica la tenuta nell'uso.
6. Integrare nei fork locali il seguito descritto sotto: `eval perceive`
   raccoglie i casi metodologici emersi nell'uso e `exec` rende riconoscibili
   decisioni autonome, conferme richieste e punti sospesi. Il marker indica
   dove vive questo presidio, perché sopravviva al consumo della prescrizione.
   Nessun caso o report vuoto va prodotto solo per completare il giro.

## Raccogliere casi per affinare la delega

Si parte dai casi concreti raccolti dagli adottanti mentre lavorano, dove
contesto e alternative sono ancora disponibili. Non si avvia ora una
classificazione generale degli ultimi commit: la storia si consulta quando
serve a verificare un caso, senza attribuire retroattivamente motivi che
non documenta.

Far risalire gli eventi significativi: un confine ambiguo, un arresto,
un errore di ricostruzione o una decisione per cui il criterio non bastava.
Includere anche qualche caso di autonomia riuscita con riscontro e qualche
conferma rivelatasi inutile. La sola raccolta dei problemi selezionerebbe
l'evidenza verso criteri sempre più restrittivi. Un assenso umano frequente
è un segnale di attrito, non una verifica indipendente della correttezza.

Ogni caso porta cinque elementi, in prosa breve:

- **Situazione**: decisione concreta, repository e contesto necessario.
- **Confine**: autorizzazione o criterio applicabile, assente o ambiguo,
  con riferimento alla versione valida al momento.
- **Comportamento**: cosa l'agente ha applicato, sospeso o sottoposto al
  custode, alternative considerate e motivo della scelta.
- **Riscontro**: esito osservato e fonte o commit; se manca, dichiararlo
  con orizzonte e fonte del riesame. Distinguere fatto, dichiarazione e
  interpretazione; un commit riuscito non prova da solo un buon risultato.
- **Questione per il metodo**: quale distinzione potrebbe servire anche
  altrove e quale parte resta specifica del dominio. Un criterio suggerito
  è un'ipotesi da valutare, non una regola già applicabile.

### Dal caso locale al canone

Il caso resta verificabile nella fonte locale; si raccoglie il minimo
contesto metodologico necessario, senza duplicare i dossier di dominio.
La cattura destinata a `method` è un segnale i1, non una modifica del canone.
Se serve una nota locale in attesa di consegna, deve essere raggiungibile
dall'indice i1 e distinguere «da inoltrare» da «acquisita da method».

Il canale segue `kb/method-development.md`: nei repo del custode la
consegna avviene tramite una sessione autorizzata sul canone, con cattura
in `method/i1/` e voce nell'indice; per adottanti mantenuti da terzi, la
pull request e il suo razionale sono già il segnale persistente. Senza
accesso o autorità, lasciare il caso locale raggiungibile e dichiarare
l'handoff pendente nel resoconto. Non dichiarare una consegna mai avvenuta;
il solo marker di allineamento non sostituisce il caso.

In `method`, `eval` acquisisce i casi, li interpreta e confronta con gli
altri prima di proporre una generalizzazione. Al battito `/adottanti`
si riesaminano i casi arrivati e un piccolo campione di decisioni ordinarie
con fonti disponibili, includendo successi e conferme inutili per limitare
la selezione dei soli problemi. Dichiarare perimetro e limiti del campione;
assenza di segnalazioni non dimostra assenza di attrito o errori.

I criteri si precisano gradualmente dal basso: un episodio può motivare
una correzione locale o una domanda, senza diventare obbligo per tutti.
Ogni modifica delle condizioni della delega torna al custode; la cattura
non amplia né restringe da sola l'autorità dell'agente. Il verdetto di
`method` deve rendere riconoscibile il seguito del segnale: criterio comune,
adattamento locale, ulteriore osservazione o nessuna modifica motivata.
Il seguito torna agli adottanti attraverso il normale canale del canone.

## Indizi e vincoli locali

- `bi`: conservare la riserva sul push dei commit che toccano codice eseguito
  dal ciclo; la delega della revisione non è autorizzazione al rilascio.
- `nixos`: la delega del ciclo non estende permessi su rebuild, sudo o host.
- `economia` e `salute`: distinguere la manutenzione dell'artefatto dalle
  decisioni patrimoniali, personali e sanitarie e dagli invii.
- `crm` e `baserow`: conservare i confini locali su deploy e produzione.
- `danea-auto`: il recepimento che modifica `eval` attende la chiusura
  dell'osservazione già presidiata in `i2/presidio-ipotesi-adottanti.md` di
  `method`. Il marker può registrare il rinvio neutro senza ricordare alle
  sessioni l'ipotesi osservata. La propagazione non deve contaminare la prova.

## Stato e chiusura

Applicata in `method`; recepimento nei sette non ancora verificato. Il filo
`i3/audit-adottanti.md` segue gli esiti, compreso il rinvio intenzionale.
La prescrizione si consuma dopo il recepimento o adattamento motivato dei
sette, compreso il presidio locale di raccolta e consegna dei casi;
la qualità nell'uso resta osservata nei fili del battito e della
ricostruzione delegabile. La nuova home e il pilota schedulato restano lavoro
separato: il resoconto con diff e commit è già il controllo del giro richiesto.
