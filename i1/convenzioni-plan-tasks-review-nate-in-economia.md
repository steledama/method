---
ciclo: runtime
---

# Segnale: convenzioni di `plan.md` e `tasks-review` affinate in un adottante

Data: 2026-06-23 · Fonte: `economia` (origine del segnale), durante una sessione
di pianificazione operativa sulla coda reale

## Il segnale

In `economia`, lavorando sulla coda viva (situazioni condominiali e fiscali con
molti attori e pause tattiche), sono emerse quattro modifiche alla forma di
`plan.md` e alla skill base `tasks-review`, ciascuna nata da un attrito concreto e
già applicata in locale (registrate come divergenze-intenzionali nel
`method-review.md` di `economia`):

1. **`pause` al posto di `|`** come significante della pausa tattica. Il `|` è il
   delimitatore di colonna delle tabelle markdown: usato come valore di cella va
   escapato (`\|`) ed è visivamente ambiguo. Sostituito con la parola `pause`.
2. **Colonna `Dip.` senza numeri, riferimenti per nome.** Il `#` come puntatore
   d'ordine effimero veniva letto come ID stabile e confondeva. Tolta la colonna
   `#`; le righe sono ordinate per **imminenza della prossima mossa**; le
   dipendenze si esprimono per nome (`dopo: X`) e le cause sono elencate per nome
   in legenda.
3. **`## Scadenze` in forma canonica + ricorrenti assorbite.** Ogni voce è
   `data → una riga → un rimando` a task o nodo (protocolli, importi e cronache
   stanno nel nodo/task, non qui). Le ricorrenti non hanno sezione separata:
   stanno in `## Scadenze` con la cadenza tra parentesi (`(mensile)`,
   `(annuale)`, `(biennale)`) e la prossima occorrenza come data.
4. **Passo `3b — lettura strategica` in `tasks-review`.** Oltre all'igiene
   (coerenza, ordine, scadenze), la review interroga ogni mossa nostra:
   canale/delega (scavalca un agente con mandato?), sequenza/informazione (una
   conversazione imminente darebbe un _read_ prima di muoverci?), effetti di
   secondo ordine (indebolisce un canale neutrale? cambia gli incentivi di una
   controparte?). Una `pause` può **nascere** da qui. Il caso che l'ha prodotto:
   una richiesta diretta a un amministratore condominiale che avrebbe scavalcato
   il gestore delegato — la review formale non l'aveva intercettata.

## L'attrito osservato

Valenza-neutro, per ciascuna:

- Il `|` collide **letteralmente** con la sintassi di tabella: difetto di
  portabilità che tocca ogni adottante con tabelle markdown — lo stesso
  [`plan.md`](../plan.md) di `method` porta `\| [a]`.
- Il `#` effimero ha doppia funzione (ordine in tabella + riferimento in `Dip.` e
  in conversazione), mentre il canone già chiede di citare i task **per titolo**:
  la doppia vita del `#` è il punto che `economia` ha sciolto togliendolo. È però
  in tensione **diretta** con una scelta deliberata di [`plan.md`](../kb/plan.md)
  (§«La forma e gli identificatori a vite diverse»): va pesato se generalizza o è
  gusto locale.
- Il passo strategico non è igiene: è una lettura che la skill base oggi non
  sollecita, e il suo valore dipende da domini **multi-attore** (forte in
  `economia`, da verificare altrove).
- L'assorbimento delle ricorrenti è in parte pulizia locale: `economia` non
  riceveva una sezione `## Ricorrenti` dal canone, la teneva per conto suo.

## Da valutare (i2→i3, non ancora verdetto)

Aperto, da sciogliere in `method`:

1. Quali delle quattro **generalizzano** e quali sono gusto/dominio di `economia`?
   Ipotesi: `pause`-vs-`|` (difetto di portabilità) e `3b` (multi-attore) sono i
   candidati più forti; «niente numeri» contraddice una scelta deliberata del
   canone e va pesato; «ricorrenti assorbite» è più pulizia locale.
2. Per ciascuna generalizzabile, l'esito per gli altri tre adottanti (`nixos`,
   `bi`, `salute`) è **adozione** o **«non applicabile»**? `pause` cambierebbe il
   significante in [`plan.md`](../kb/plan.md) e in ogni coda; `3b` arricchirebbe
   la skill base `tasks-review` per tutti.
3. Compatibilità interna: «niente numeri» va riconciliato con §«La forma e gli
   identificatori a vite diverse» di [`plan.md`](../kb/plan.md) (il `#` effimero,
   il puntatore conversazionale): se si adotta, quel paragrafo va **riscritto**,
   non solo la tabella.
4. È un secondo arco runtime→dev **bottom-up** attraverso la membrana (dopo
   `kb-tools` da `bi`): evidenza per la cucitura «agisci attraverso, ratifica» e
   per il task [`enforcement-cucitura-canone`](../o2/enforcement-cucitura-canone.md).
