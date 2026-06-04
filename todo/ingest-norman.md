---
data: 2026-06-04
stato: aperto
---

# Ingest dei libri di Norman come fonte

Task meccanico e dipendente dalla rifondazione (`rifondazione-input-output`): portare il
contributo di Norman nel repo come **fonte grezza** versionata, non solo come citazione di
seconda mano nei nodi. Candidato a essere il **primo pilota reale dello strato input**
(i1 → i2 → i3) — dogfooding che dà fondamento empirico alla formalizzazione dell'input.

## Quali libri

Il contributo di Norman è più ampio di DOET, e i concetti emersi nella rifondazione vengono
da libri diversi:

- *The Design of Everyday Things* (1988/2013) — ciclo d'azione a sette stadi, due gulf,
  system image / mental model, visibilità · feedback · mapping · constraint, affordance e
  signifier (questi ultimi aggiunti nell'ed. 2013). È la fonte già citata in `ciclo-azione`.
- *Things That Make Us Smart* (1993) — **cognitive artifact**, cognizione distribuita,
  experiential vs reflective cognition. È la fonte dei concetti nuovi (artefatto cognitivo,
  sistema cognitivo) e oggi **non è citata** in nessun nodo.

Verificare se servono anche *Emotional Design* (2004) e *Living with Complexity* (2010),
già menzionati in `ciclo-azione`.

## Questione aperta che il task fa emergere: dove vivono le fonti grezze?

Il repo `metodo` non ha una `fonti/` (cfr. `pattern-karpathy`: le fonti grezze stanno
separate dai nodi atomici). L'ingest di un epub costringe a decidere dove vive i1 nel repo,
e questa decisione è parte della formalizzazione dello strato input. Per questo il task è
*dipendente* dalla rifondazione, non indipendente: non ingerire prima di aver deciso la
struttura dell'input.

## Sequenza (quando si attiva)

1. Decidere collocazione delle fonti grezze (dipende da `rifondazione-input-output`)
2. i1 — collocare gli epub/estratti come fonte
3. i2 — note distillate per concetto (artefatto cognitivo, cognizione distribuita, ciclo
   a due agenti, gerarchia del Goal)
4. i3 — i concetti distillati aggiornano/creano i nodi (`artefatto-cognitivo`,
   `sistema-cognitivo`, `ciclo-azione`, `goal`); aggiornare i `## Riferimenti` con la fonte
   corretta per ogni concetto (fedeltà alle fonti: quale libro per quale idea)

## Connessioni

- [rifondazione-input-output](rifondazione-input-output.md)
- [ciclo-azione](../kb/ciclo-azione.md)
