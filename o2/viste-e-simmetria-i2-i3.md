---
sintesi: "Separare le viste (resa HTML 1:1 dei .md, derivata) dalla presentazione (l'unico deck Reveal, scritto a mano, linkato dalla home) e ridare a i2 vita propria per simmetria con o2: i3 diventa una tabella di verdetti come il plan, ogni riga col suo file i2 che porta la lettura a valenza sospesa. Quattro fasi: canone, ristrutturazione di metodo, builder, prescrizione ai sei con rivalutazione delle potature recenti dei fili."
ciclo: dev
---

# Viste, presentazione e simmetria i2/i3

Decisione del custode (2026-10-04), nata dalla revisione della presentazione:
in `presentation/` convivono due cose diverse, e la confusione si è
propagata fino allo stadio i2.

- **Viste**: la traduzione 1:1 di un `.md` in una pagina HTML, con la
  navigazione. Derivate, rigenerate, mai scritte a mano (`kb/view.md`).
- **Presentazione**: l'unico deck Reveal, il racconto curato
  dell'artefatto. Scritta, non derivata. Non è uno stadio: la home la
  linka come voce a sé.

Il deck oggi occupa i2 (`i2/metodo-in-sintesi.md` e le tavole), ma non è
un'interpretazione: i2 deve tornare a essere il ponte fra percezioni e
confronti.

## Il modello deciso

Simmetria con il braccio di esecuzione, secondo gli specchi del ciclo
(o1↔i3, o2↔i2):

- **i3 è una tabella**, come `o1/plan.md`: una riga per filo, col verdetto
  contro l'obiettivo e il prossimo controllo. Seconda eccezione alla regola
  delle tabelle di `CLAUDE.md`.
- **i2 tiene un file per filo**: evidenze, fonti, tensioni, a valenza
  sospesa (`kb/interpret.md`). Oggi un filo di `i3/` mescola lettura e
  verdetto; la divisione li separa.
- **Corrispondenza biunivoca**: nessuna riga di i3 senza il suo file i2,
  nessun file i2 aperto senza la sua riga (al limite col verdetto «da
  confrontare»). Il generatore la verifica come verifica plan×`o2/`, e
  `/eval` ne fa il controllo speculare a quello di `/exec plan`.
- **Chiusura**: il filo chiuso esce da entrambi; ciò che ha capito sale in
  un nodo `kb/`, la storia resta in git.

Decisione aperta: lato esecuzione una riga del plan può vivere senza file
`o2/`. Lato valutazione la corrispondenza è stretta per scelta: va detto
nel canone se l'asimmetria è voluta o se anche il plan si stringe.

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

Ricalcare i path rende meccanica la riscrittura dei link: un `.md` reso
diventa il suo `.html`, un file non reso resta etichetta.

## Fasi

1. **Canone.** Nodi `view` (resa 1:1, build, servizio sulle reti private),
   `presentation` (il solo deck: è l'unica superficie non derivata, e
   dichiara come resta fedele al canone), `verdict`, `interpret`,
   `compare`, `project-structure`, `plan` (eccezione tabelle). Skill
   `eval` (`interpret` e `compare` col controllo i2↔i3) e `adottanti`
   (scrive nel filo dell'audit). `CLAUDE.md` e `README.md`. Un solo
   commit: i nodi si citano a vicenda.
2. **Ristrutturazione di `metodo`.** Deck e tavole in `presentation/`;
   i cinque fili divisi in riga i3 e corpo i2; triage degli altri file di
   `i2/` (`potatura-kb` conclusa, `baricentro-kb-adottanti` materiale di
   nodo, `bootstrap-adottanti` e `ingresso-adottante` da rileggere).
   **Rivalutazione della potatura** `5ea8204` (sedici fili ridotti a
   cinque): il criterio era «un filo misura un obiettivo», e senza una
   casa per la lettura a valenza sospesa alcune interpretazioni vive
   possono essere state cacciate insieme ai verdetti morti. Per ogni filo
   rimosso: chiuso a ragione, salito in un nodo, oppure lettura da
   ripristinare in i2 con la sua riga.
3. **Builder.** Pagine 1:1 con Pandoc e riscrittura dei link; barra di
   navigazione comune (home, indice della collezione, pallini sul filo
   d'accento per le collezioni a sequenza, orizzontale su schermo stretto);
   `goal.html` con un'ancora per obiettivo, destinazione della chiave
   `Ob.`; `plan.html` con dipendenze e scadenze, tabella a scorrimento
   proprio; home col link «Presentazione». Etichetta «Confronti» al posto
   di «Verdetti»; sigle degli stadi nel colore neutro, non `--warm`.
4. **Prescrizione ai sei** in `o3/`: migrazione di cartelle e fili, la
   rivalutazione delle proprie potature recenti dei fili (da 38 a 19
   nell'aggregato) con lo stesso criterio della fase 2, e il nuovo path
   nei servizi permanenti degli host (`nixos`, `danea-auto` su `danea2`)
   che oggi controllano `presentation/index.html`. Il deck di `nixos` si
   riscrive qui, con lo scopo finalmente chiaro.

## Feedback

- La build passa col contratto i2↔i3 attivo e il presidio del compartimento
  stagno su `view/`.
- Ogni pagina si apre via `file://` e via `serve.py`; la navigazione regge a
  larghezza mobile.
- La rivalutazione delle potature dichiara per ogni filo rimosso l'esito,
  anche quando è «chiuso a ragione».
- Il battito `/adottanti` successivo alla prescrizione legge la migrazione
  nei file, non nei marker.

## Vincoli

- Nessuna vista scritta a mano: ciò che non deriva da un `.md` è il deck,
  e il deck è uno solo.
- La rinomina della cartella servita non si fa senza aggiornare nello stesso
  giro i servizi permanenti degli host: un servizio fermo in silenzio è
  l'«assenza leggibile» mancata.
- Le fasi 1–3 si chiudono in `metodo` prima di prescrivere ai sei.
