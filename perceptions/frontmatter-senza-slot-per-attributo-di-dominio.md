# Segnale: il frontmatter del nodo non ha slot per un attributo intrinseco di dominio

Data: 2026-06-27 · Fonte: `nixos` (Fase 4 della predisposizione separazione
lavoro/casa), stratificando la KB per mondo

## Il segnale

In `nixos` serviva marcare ogni nodo della KB con il mondo che documenta —
`lavoro`, `casa` o `trasversale` — per rendere meccanico un futuro split dei
repository (smistamento, non riscrittura). «A quale mondo appartiene questo nodo»
è un **attributo intrinseco del nodo**: non è una relazione verso un altro nodo,
non è storia, non è un task, non è priorità. È una proprietà del nodo, e la sede
naturale di una proprietà del nodo è il suo frontmatter.

Ma il frontmatter, per [node](../kb/node.md), ammette solo `data` e `stato`, e
vieta campi ulteriori «salvo decisione metodologica esplicita». Le sedi
alternative tentate si sono rivelate metodologicamente sbagliate: il catalogo
`kb.md` è il **solo indice**, `map.md` è il **register** dello stato corrente —
nessuno dei due è la casa di un attributo classificatorio del nodo. L'attributo
resta così senza sede canonica.

## L'attrito osservato

Il metodo ha uno slot per quasi ogni tipo di informazione — relazioni → link,
storia → git, lavoro → `tasks/`, priorità → `plan.md`, stato corrente → `map.md`,
verdetti → `verdict.md` — ma **non** per un attributo intrinseco e tassonomico del
nodo stesso. Senza uno slot sanzionato, l'adottante è spinto a contrabbandare la
tassonomia in un indice o register che non è la sua sede.

Il divieto esistente (`tags`, `owner`, `priority`, `updated`) è corretto: quelli
erano relazioni, storia o gestione-lavoro travestite da metadato. Ma il divieto
**sovra-estende**: in assenza di un criterio di demarcazione, blocca anche
l'attributo intrinseco legittimo. Manca la regola che separa l'attributo del nodo
dal metadato-che-vive-altrove.

Corollario emerso esaminando lo stesso frontmatter, valenza-neutro: anche `data`
è ricostruibile da git (il primo commit che tocca il file), quindi per la logica
stessa del metodo («la storia in git») è un campo debole — mentre `stato`, che è
giudizio non ricostruibile, resta solido. Una contro-giustificazione reale ma
**eccezionale** è affiorata proprio dalla separabilità di `nixos`: una riscrittura
di history (il repo pubblico fresco) distrugge la data del primo commit, e il
frontmatter `data` la sopravvive come àncora di provenienza. Net: nello stesso
esame `data` va ri-giustificato o degradato.

## Da valutare (i2→i3, non ancora verdetto)

Aperto, da sciogliere in `method`:

1. Il metodo deve sanzionare un **meccanismo di estensione del frontmatter** che
   permetta a un adottante di dichiarare proprietà di nodo oltre `{data, stato}`?
   Con quale criterio di demarcazione? Proposta grezza dall'adottante: la proprietà
   è ammessa solo se **intrinseca** (non relazione/storia/lavoro/priorità), a
   **valori chiusi e singola** (faceted classification, non tag aperto e
   multi-valore — quello è un link), **non derivabile** da una fonte di verità
   esistente (niente seconda storia), e **dichiarata e verificabile** da `kb_tools`.
2. Generalizza agli altri tre adottanti (`bi`, `economia`, `salute`) o è
   `nixos`-specifico? L'esito per gli altri è adozione o «non applicabile»?
3. Il riesame del campo `data`: ri-giustificarlo esplicitamente come àncora di
   provenienza robusta alle riscritture di history, oppure degradarlo a opzionale
   o rimuoverlo (propensione corrente dell'adottante: rimuoverlo).

L'applicazione attesa in `nixos`, una volta sbloccata: campo
`mondo: lavoro | casa | trasversale` sui ~40 nodi (oggi la ripartizione ~9/8/23
vive solo nella prosa di un task) più un check in `kb_tools`. Lì la Fase 4 è
sospesa in attesa di questo verdetto.

## Esito

Aperto.
