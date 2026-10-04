---
sintesi: "Separare le viste derivate dall'unico deck curato: il deck esce da i2 e trova casa in presentation/, le pagine generate in view/, servita e chiusa su se stessa. Canone, builder, servizi degli host e prescrizione ai sei, senza perdere funzioni interpretative dei deck generati né servizi permanenti."
ciclo: dev
---

# Viste e presentazione

Decisione del custode (2026-10-04), nata dalla revisione della presentazione:
in `presentation/` convivono due cose diverse, e la confusione si è
propagata fino allo stadio i2.

- **Viste**: la traduzione 1:1 di un `.md` in una pagina HTML, con la
  navigazione. Derivate, rigenerate, mai scritte a mano (`kb/view.md`).
- **Presentazione**: l'unico deck Reveal, il racconto curato
  dell'artefatto. Scritta, non derivata. Non è uno stadio: la home la
  linka come voce a sé.

Il deck di `metodo` oggi occupa i2 (`i2/metodo-in-sintesi.md` e le tavole),
mescolando il racconto curato dell'artefatto con l'interpretazione dei segnali.
Questo task lo sposta e chiude la motivazione originaria. Che cosa i2 diventi
una volta liberato è materia del task
[ipotesi-e-confronti-i2-i3](ipotesi-e-confronti-i2-i3.md), da cui questo è
stato separato il 2026-10-04 perché il lavoro meccanico non attendesse l'esito
di una prova di modello. Il solo punto di contatto è l'etichetta della
collezione i3 («Verdetti» o «Confronti»): decisione di canone che appartiene
all'altro task; qui il builder legge il titolo dall'indice, senza cablarlo.

## Cartelle

Una sola cartella generata e servita, chiusa su se stessa: `serve.py` serve
una cartella e la home deve linkare il deck senza uscirne.

```
presentation/   sorgente del deck: presentation.md e tavole
view/           generata: index.html, presentation.html, pagine che
                ricalcano i path del repo (goal.html, o1/plan.html,
                o2/*.html, i2/*.html, i3/*.html, …), assets/
o3/view/        i builder (oggi o3/presentation/)
```

Ricalcare i path facilita la riscrittura dei link: un `.md` reso diventa il suo
`.html`, un file non reso resta etichetta. «1:1» significa fedeltà al contenuto
e alla struttura della pagina sorgente; non restringe la nozione generale di
vista derivata, che può essere una sintesi o un grafico.

Decisioni aperte, da prendere prima del builder:

- **perimetro delle fonti rese e degli asset**, anche per symlink, dati
  personali e prodotti runtime: non si pubblica automaticamente ogni `.md` del
  checkout;
- **versionamento di `view/`**: oggi `presentation/` generata è versionata e
  rigenerata nel commit (gate `commit`, check i2). Tenere la stessa regola o
  ignorare la cartella cambia la freschezza verificabile dal checkout e il
  modo in cui l'audit `/adottanti` legge le viste.

## Fasi

1. **Canone.** Nodi `view` (resa delle pagine, build, servizio sulle reti
   private), `presentation` (il racconto curato dell'artefatto e la sua
   fedeltà alle fonti, distinto dalle viste derivate) e `project-structure`;
   skill `commit` (nuova build); `CLAUDE.md` e `README.md`. Transizione
   dichiarata per gli adottanti che leggono i nodi via symlink ma non hanno
   ancora migrato.
2. **Ristrutturazione di `metodo`.** Deck e tavole da `i2/` a
   `presentation/`; `i2/interpretations.md` perde la nota di build del deck.
3. **Builder.** Pagine fedeli alle fonti con Pandoc e riscrittura dei link;
   barra di navigazione comune (home, indice della collezione, pallini sul
   filo d'accento per le collezioni a sequenza, orizzontale su schermo
   stretto); `goal.html` con un'ancora per obiettivo, destinazione della
   chiave `Ob.`; `plan.html` con dipendenze e scadenze, tabella a
   scorrimento proprio; home col link «Presentazione». Sigle degli stadi nel
   colore neutro, non `--warm`. Coordinare il cambio della cartella servita
   col servizio di `metodo` quando avviene, prima della propagazione.
4. **Prescrizione ai sei** in `o3/`: migrazione delle cartelle e nuovo path
   nei servizi permanenti degli host (`nixos`, `danea-auto` su `danea2`) che
   oggi controllano `presentation/index.html`. Ogni adottante decide e
   applica la migrazione nel proprio dominio.

## Feedback

- La build passa col contratto di riferimenti e il presidio del
  compartimento stagno su `view/`.
- Ogni pagina si apre via `file://` e via `serve.py`; la navigazione regge a
  larghezza mobile.
- Il deck di `metodo` non vive più in `i2/`.
- Il battito `/adottanti` successivo alla prescrizione legge la migrazione
  nei file, non nei marker.

## Vincoli

- Nessuna vista derivata mantenuta a mano. Il racconto curato dell'artefatto è
  distinto dalle interpretazioni e dalle loro rese grafiche.
- Negli adottanti alcuni deck sono sintesi di dominio generate dai dati (in
  `bi` anche prodotti runtime i2 e i3): la loro funzione interpretativa non
  scompare cambiando formato o cartella, e i contratti runtime dei JSON si
  conservano. Il deck di `nixos`, che mescola racconto dell'artefatto e
  lettura del boot, si riscrive solo dopo l'esito dell'altro task.
- La rinomina della cartella servita non si fa senza aggiornare nello stesso
  giro i servizi permanenti degli host: un servizio fermo in silenzio è
  l'«assenza leggibile» mancata.
- Le fasi 1–3 si chiudono in `metodo` prima di prescrivere ai sei; la finestra
  di transizione fra canone e adottanti è esplicita.
