---
data: 2026-06-04
stato: in corso
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

## Questione aperta che il task fa emergere: dove vivono le fonti grezze? — RISOLTA (2026-06-05)

Il repo `metodo` non aveva una cartella per le fonti grezze (cfr. `pattern-karpathy`: le
fonti stanno separate dai nodi atomici). L'ingest di un EPUB ha costretto a decidere dove
vive i1, e la posa stessa ha sciolto la decisione (dogfooding, non scrivania):

- **`sources/`** (inglese, allineato a i1/i2/i3 e alla traduzione del repo).
- **Binari non versionati** (copyright + repo pubblico): `.gitignore` ha `sources/*` +
  `!sources/README.md`.
- **`sources/README.md` versionato** = manifest di provenienza (edizione, formato, ISBN),
  base dei `## Riferimenti` dell'i3.
- **Copia scelta per DOET**: solo l'**EPUB 2013 Revised and Expanded** (è l'ed. che aggiunge
  affordance/signifier; testo nativo migliore per i1→i2). Scartate 2002, scansione 23 MB
  senza testo, PDF 2013 ridondante. *Emotional Design* (2004) copia unica.

Resta sospeso solo l'esito sull'altra metà della stessa domanda in `rifondazione`: dove
vivono i2 (note distillate) e come si dichiara lo strato input nei progetti adottanti.

## Sequenza

1. ~~Decidere collocazione delle fonti grezze~~ — fatto (vedi sopra).
2. ~~i1 — collocare gli epub/estratti come fonte~~ — fatto: `sources/` con EPUB DOET 2013 +
   *Emotional Design* 2004; manifest in `sources/README.md`.
3. **i2 — note distillate per concetto** — *in corso*. Deciso col dogfooding (2026-06-05):
   **l'i2 non ha casa separata, è un nodo `kb/` in `stato: bozza`**; il passaggio i2→i3 è la
   maturazione `bozza→maturo`. Scartate co-locazione in `sources/` e cartella `i2/` dedicata.
   - ✅ **affordance/signifier** → `kb/affordance-signifier.md` (bozza), distillato dal testo
     reale dell'EPUB (Cap. 1, DOET 2013), collegato a `ciclo-azione`. Aggancio chiave: l'agente
     «person, animal, or machine» fonda testualmente il ciclo a due agenti.
   - ✅ **system image / conceptual+mental model** → `kb/system-image.md` (bozza), Cap. 1 DOET
     2013. Aggancio chiave: «the entire burden of communication is on the system image» fonda
     *la KB è il system image dei due agenti*; «valid only as long as the assumptions hold»
     aggancia il check decisioni/assunzioni e il caso `bi`/1018022.
   - ✅ **visceral/behavioral/reflective** → `kb/visceral-behavioral-reflective.md` (bozza),
     *Emotional Design* 2004 (Prologo + Cap. 1). Aggancio chiave: la KB è lo strato reflective;
     l'esempio della staccionata è il filing back; «no direct access to the control of behavior»
     è il gulf of execution e la ragione dello strato output. Aggiunge la dimensione affettiva.
   - ✅ fonti disponibili esaurite. (Le estrazioni `.txt` di lavoro stanno in `sources/`,
     ignorate: sono i1 in forma testuale, non i2 — vedi `sources/README.md`.)
   - ⛔ artefatto cognitivo, cognizione distribuita → richiedono *Things That Make Us Smart*
     (non reperito, vedi gap sotto).
4. i3 — i concetti distillati maturano/creano i nodi (`artefatto-cognitivo`,
   `sistema-cognitivo`, `ciclo-azione`, `goal`); aggiornare i `## Riferimenti` con la fonte
   corretta per ogni concetto (fedeltà alle fonti: quale libro per quale idea). Primo
   `## Riferimenti` con provenienza esatta già posato in `affordance-signifier`.

## Gap di fonte ancora aperto

*Things That Make Us Smart* (1993) — fonte dei concetti nuovi (artefatto cognitivo,
cognizione distribuita) — **non ancora reperito**. Registrato in `sources/README.md`. I3 sui
nodi `artefatto-cognitivo`/`sistema-cognitivo` resta zoppo finché manca questa fonte.

## Connessioni

- [rifondazione-input-output](rifondazione-input-output.md)
- [ciclo-azione](../kb/ciclo-azione.md)
