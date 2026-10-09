---
sintesi: "La home della vista apre con due sezioni: «fatto», gli ultimi commit con autonomia, impatto e motivo, e «da fare», lavoro pronto e attese; proposte pendenti e tentativi restano visibili."
ciclo: dev
---

# Home con fatto e da fare

Più autonomia all'agente chiede un controllo che il custode legge in un
colpo d'occhio. La vista web è il luogo: le due sezioni stanno in cima alla
home, prima dei poli Goal e World.

## Le due sezioni

- **Fatto**: gli ultimi 5 commit, con data e ora, titolo, autonomia e
  impatto vestito col semaforo, e il motivo leggibile accanto. La fonte è `git log` con i trailer, letto dall'host che pubblica
  dal commit.
- **Da fare**: la prossima mossa pronta nell'ordine del plan, le scadenze
  ordinate per data e le dipendenze `w`/`p` di `o1/plan.md`, anche senza
  data. Oggi si leggono solo aprendo il plan.

## Vincoli

- È un cambio del canone delle viste (`kb/view.md`, builder in `o3/view/`):
  si prescrive agli adottanti come gli altri.
- «Da fare» non dipende da nulla e può partire subito. «Fatto» mostra
  `Esiti:` e i trailer `Autonomia:`/`Impatto:` dove ci sono, già in `/commit`.
- La pubblicazione costruisce da `git archive`: verificare come il builder
  legge la storia senza rompere il contratto del commit pulito.

## Contratto di supervisione e riuscita

La home deve rendere distinguibili l'ultimo commit riuscito e l'ultimo
tentativo del battito: un giro interrotto prima del commit, un push rifiutato
o una partenza mancata non diventano un successo per assenza di nuovi commit.
Il task [Dove gira il battito](dove-gira-il-battito.md) definisce fonte,
freschezza e stati dei tentativi; qui si definisce come leggerli. Finché la
fonte non esiste, la vista dichiara il dato non disponibile.

- «Fatto» conserva gli ultimi cinque commit; le proposte ancora da decidere
  restano raggiungibili anche quando escono da quel campione. La loro fonte
  e il loro consumo sono definiti in [Criteri di autonomia](criteri-autonomia.md).
- «Da fare» rende anche la prossima mossa pronta senza data, rispettando
  l'ordine del plan. Le attese senza data restano tali, senza date inventate.
- La storia estratta per la pubblicazione termina al commit esportato con
  `git archive`; una pubblicazione dello stesso commit non incorpora commit
  successivi. Lo stato operativo corrente dichiara separatamente provenienza
  e momento della lettura.

Il task si chiude quando il custode trova una mossa pronta, ricostruisce
motivo e impatto di un commit e raggiunge una proposta ancora pendente oltre
i cinque commit. Prima dell'avvio del pilota deve essere verificata anche
la resa di un tentativo fallito o non partito, usando la fonte concordata
con l'esecutore. La pubblicazione continua a rispettare i contratti delle viste.

## Register della delega

`autonomy.md` contiene la prima delega operativa del ciclo richiesto dal
custode. Il resoconto con diff e commit è già il controllo di quel giro;
la home deve renderne raggiungibili i criteri e le proposte pendenti prima
del pilota schedulato. Il register è per ora leggibile dal repository:
aggiungerlo al perimetro delle pagine e concordarne la resa nella home con
il residuo di `criteri-autonomia`, senza introdurre un nuovo stadio.
