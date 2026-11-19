---
sintesi: "Decidere se il canone ammette, oltre al deck unico di kb/presentation.md, sotto-deck annidati e pagine di dominio come voci della home, e con quale contratto: due segnali da salute, uno riscontrato anche in economia."
ciclo: dev
decidere: "Il canone ammette sotto-deck annidati e pagine di dominio in home, e con quale contratto, o restano scostamenti locali?"
---

# Presentazione oltre il deck

## Origine

Giro autonomo del 2026-11-19. Due catture del custode del 18/11, da inoltri
della sessione `salute` via Herdr, non sono ancora valutate da nessun filo:

- [pagina di dominio in home](../i1/pagina-dominio-home-salute-2026-11-18.md):
  la home canonica linka come voce a sé solo il deck; il cruscotto di
  `salute` finisce nella descrizione della card i2. Un caso solo;
- [presentazioni annidate](../i1/presentazioni-annidate-salute-economia-2026-11-18.md):
  `salute` ed `economia` arrivano a un deck principale con sotto-deck, in
  due forme diverse. Due casi.

Il marker `i3/allineamento-metodo.md` di `salute` (letto su `deck` il
2026-11-19) dichiara le due cose come scostamento dal «solo deck» del canone
e le dice «in attesa di verdetto» qui. Finché `method` non decide, lo
scostamento resta dichiarato e il canale col basso aspetta.

## Alternative

- **Restano locali**: `kb/presentation.md` resta «un solo deck»; i due
  adottanti tengono lo scostamento dichiarato nel marker.
- **Contratto nel canone, navigazione locale**: il nodo ammette un deck
  principale con sotto-deck e fissa solo il contratto (sintassi del
  collegamento, nomi delle pagine, link chiusi in `view/`, rottura della
  build sugli orfani); script e briciola restano negli adottanti.
- **Contratto e navigazione canonici**: in più una delle due forme entra in
  `o3/view/`. Le due divergono su pagina unica o una per sotto-deck,
  sintassi (`Approfondimento:` nel Markdown o `data-sub` nell'HTML) e stato
  della navigazione (hash o briciola).
- **Pagina di dominio in home**, indipendente dalle tre: un campo facoltativo
  in `project.py` (la proposta di `salute` è `PAGINE_HOME`) che la home rende
  accanto a «Presentazione», oppure nessun aggancio finché resta un caso solo.

## Decisione richiesta

Quale alternativa per i sotto-deck, e se aprire subito l'aggancio in home o
aspettare un secondo caso. Il nodo `kb/presentation.md` e gli strumenti in
`o3/view/` si toccano solo dopo la scelta, in sessione: gli strumenti restano
proposta per il giro, e una forma fra due non si sceglie su una fonte.
