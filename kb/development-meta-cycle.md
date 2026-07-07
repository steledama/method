---
stato: bozza
---

# Development meta-cycle

Il ciclo che conta in prima vista è il **runtime cycle**: l'artefatto sostiene un
agente umano+LLM che agisce su un dominio reale, ne percepisce la risposta e
riporta il segnale verso il Goal. È il ciclo di Norman reso versionabile dal
metodo: piani, compiti, prescrizioni; percezioni, interpretazioni, confronti.

Il ciclo di sviluppo non è un secondo ciclo alla pari accanto al runtime. È il
**development meta-cycle**: usa la stessa geometria a sei atti e due poli, ma ha
per Mondo la macchina che rende possibile il runtime, cioè l'artefatto stesso.
Un commit, una modifica di KB, una vista rigenerata o uno script aggiornato sono
atti del meta-ciclo; lint, audit, test, errori e drift sono le sue percezioni.
Il suo output non è il dominio: è una macchina runtime più adatta.

La relazione resta quella che prima chiamavamo annidamento, ma il fuoco si
ribalta. Non diciamo più «due cicli annidati» come immagine primaria, perché
graficamente e retoricamente quella formula tende a far apparire il dev come
contenitore più importante. Diciamo: **un ciclo runtime, osservato e coltivato da
un meta-ciclo di sviluppo**. Il runtime rimane centrale; il dev sta sopra e
attorno, come forma riflessiva che progetta la macchina senza sostituirsi al suo
scopo di dominio.

L'antenato resta Engelbart, 1962: il **bootstrap** — «Tools Developed vs Tools
Used» (§IV-E di _Augmenting Human Intellect_) — il sistema di augmentation che
applica i propri means a migliorare sé stesso e si solleva «by its own
bootstraps» (cfr. `augmentation-system`). La distinzione tra ciò che il sistema
_sviluppa_ e ciò che _usa_ è la stessa: il meta-ciclo sviluppa la macchina, il
runtime la usa nel dominio.

## La cucitura, non l'affiancamento

I due movimenti non sono paralleli. La giunzione è precisa: **il Mondo del
development meta-cycle è la macchina che esegue il runtime cycle**. Il commit
non _è_ la macchina: è l'atto o3-dev che modifica l'artefatto; la macchina è
l'artefatto risultante, cioè il Mondo-dev su cui il meta-ciclo agisce e che poi
opera nel runtime.

Questa è la sutura reale: il fondo del meta-ciclo è il motore del ciclo. Per
questo una rappresentazione fedele non deve mettere dev e runtime in due colonne
alla pari, né deve miniaturizzare il runtime dentro un grande contenitore dev.
Deve mostrare il runtime come ciclo principale e il dev come meta-ciclo che lo
abbraccia dall'alto: una forma, non un dominio sostitutivo.

## Un ciclo e un meta-ciclo

Il **runtime cycle** ha per Mondo la realtà del dominio: una email inviata, una
transazione, una configurazione applicata, un gesto corporeo. o3 prepara o
prescrive l'atto; l'atto accade nella membrana `world`; i1 cattura il segnale
quando serve; i2 e i3 lo interpretano e lo confrontano con il Goal.

Il **development meta-cycle** ha per Mondo l'artefatto: repository, KB,
struttura, viste, automazioni, convenzioni. o3-dev prescrive la modifica; il
commit o la rigenerazione agisce sull'artefatto; i1-dev cattura risposta
tecnica e semantica. Il suo Goal non è lo scopo di dominio, ma la forma
desiderata della macchina runtime: attrito, autonomia, temporalità, portabilità
(`development-goal`).

Il meta-ciclo quindi non rende meno importante il runtime: lo rende progettato,
ispezionabile e correggibile. Il runtime dice _a che cosa serve_ l'artefatto; il
meta-ciclo dice _come deve essere fatta la macchina_ perché quel servizio regga.

## Quattro poli e un gradiente di portabilità

La prospettiva un-ciclo/più-meta-ciclo conserva i quattro poli già emersi:
**Goal-runtime**, **World-runtime**, **Goal-dev**, **Artifact/World-dev**. Cambia
la messa a fuoco.

Al centro sta il runtime:

- **Goal-runtime** — lo scopo del dominio.
- **World-runtime** — la realtà su cui l'artefatto agisce.
- **Runtime machine** — l'artefatto in opera, che sostiene il ciclo.

Sopra il runtime sta il meta-ciclo:

- **Goal-dev** — la forma auspicata della macchina: comune nelle dimensioni,
  calibrata per dominio.
- **Artifact = World-dev** — il Mondo su cui il dev agisce e, insieme, la
  macchina che esegue il runtime.

Da qui nasce il **gradiente di portabilità**: il Goal-dev è la parte più comune
tra domini; scendendo verso il World-runtime si diventa progressivamente
domain-specifici. La portabilità non vive fuori dal runtime: è una qualità della
macchina runtime voluta dal meta-ciclo.

Per un artefatto come `method`, il cui dominio è il metodo stesso, la distinzione
si legge nell'atrio. Il runtime di `method` sono gli adottanti: segnali che
emergono da loro, confronto cross-repo, prescrizioni di canone che tornano a
loro. Il meta-ciclo di sviluppo di `method` agisce invece sui nodi, sulle viste,
sul piano e sugli strumenti di questo repo.

## L'agente è un asse ortogonale

Una tentazione ricorrente è leggere runtime e dev come «IA esegue, umano
sviluppa». È falso. **Entrambi** i movimenti sono percorsi da umano + LLM
insieme; cambia il mix, non la natura della coppia. Nel dev il peso umano tende
a essere più alto e più frequente; nel runtime l'artefatto può spostare il peso
verso l'autonomia dell'LLM, con l'umano più spesso _on-the-loop_ che
_in-the-loop_.

Quella posizione non è una proprietà del meta-ciclo: è una dimensione del
Goal-dev, cioè dell'autonomia desiderata della macchina (`development-goal`).
Agente e ciclo stanno dunque su assi ortogonali. Il diagramma può suggerire il
mix, ma non deve collassarlo nella distinzione runtime/dev.

## I sei stadi restano punti di controllo

Il runtime e il meta-ciclo condividono la stessa geometria di `action-cycle`.
Ogni stadio reso esplicito è due cose insieme: il punto in cui l'umano ispeziona
e interviene, e il punto in cui l'LLM rientra senza ricostruire il contesto da
zero. Un ciclo mostrato come un solo arco — prescrizione più ritorno — perde
questi punti di controllo; un meta-ciclo mostrato come pura cornice li nasconde.

Per questo la nuova rappresentazione deve fare due cose insieme: dare peso
visivo al runtime, e mantenere leggibile il fatto che anche il meta-ciclo ha i
suoi sei atti. Il dev può stare come arco superiore, corna, corona o struttura
riflessiva; non deve diventare un box dominante che ingoia il runtime.

## Perché non è solo di method

Ogni progetto adottante ha un ciclo runtime e un development meta-cycle: una
macchina locale — codice, configurazione, KB, viste — che agisce su un Mondo di
dominio, e un meta-ciclo che modifica quella macchina. La popolazione dei due
movimenti cambia da dominio a dominio, e proprio quella differenza è materiale
di confronto tra adottanti: dove il runtime è solido, dove manca, dove il
meta-ciclo è eccessivo, dove non dà abbastanza forma alla macchina.

La verifica sul campo di questa relazione, artefatto per artefatto, è il compito
di `action-cycle-matrix`.

Connessioni:

- [action-cycle](action-cycle.md)
- [action-cycle-matrix](action-cycle-matrix.md)
- [augmentation-system](augmentation-system.md)
- [world](world.md)
- [goal](goal.md)
- [development-goal](development-goal.md)
- [perform](perform.md)
- [perceive](perceive.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [adopter-comparison](adopter-comparison.md)
