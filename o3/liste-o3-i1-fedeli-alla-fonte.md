---
data: 2026-09-09
stato: attiva
ciclo: dev
target: nixos, bi, economia, salute, crm, danea-auto
---

# Le viste a elenco derivano dall'intera struttura della fonte, non da un nome di intestazione

## Cosa e perché

`build_lists.py` (o l'equivalente locale, dove esiste una vista a elenco
generata da un indice di collezione `i1`/`o3`) assumeva un nome di
intestazione fisso (`## Contenuti`) come unico blocco da rendere, con parsing
che si fermava al primo blocco puntato trovato lì sotto. Due segnali
indipendenti — `bi` (lo stesso nome ha significati diversi fra collezioni) e
`nixos` (la card o3 promette «strumenti» che il generatore non rendeva mai) —
hanno mostrato che il contratto era sul lessico di `metodo`, non sulla
struttura markdown della fonte, e che questo produce viste incomplete non
quando la fonte è malformata ma quando è semplicemente organizzata altrimenti.
Il generatore rende l'intero corpo Markdown tramite Pandoc, già usato dalla
build Reveal: conserva sezioni, sottotitoli, liste annidate e numerate, codice e
link. Il titolo H1 iniziale è sostituito dal titolo di pagina configurato.
La normalizzazione dei target Markdown avviene sull'AST, anche per immagini e
link a riferimento, senza modificare testo letterale o codice. L'HTML grezzo
incorporato conserva i propri URL e resta responsabilità della fonte.
Il formato letto è `markdown-native_divs`, come nelle viste Reveal.
Dettaglio e razionale in `i3/liste-o3-i1-fedeli-alla-fonte.md`; principio
canonico in `kb/view.md`, «Il contratto è strutturale, non nominale».

## Ricetta di recepimento

1. Confronta `o3/build_lists.py` con il fork: il rendering usa Pandoc invece
   del parser di paragrafi e liste piatte, che perdeva gerarchie e sottotitoli.
   Preserva la parametrizzazione locale di `PAGES`
   (sorgente/prefisso-link/titolo per pagina). Verifica che Pandoc sia disponibile
   nella build locale, come già richiesto dalle viste Reveal del canone.
2. Porta anche il ribasamento dei target Markdown sull'AST (`rebase_links` e
   `rebase_target`): preserva query, frammenti, URL assoluti e testo letterale.
   Non dipende più da `presentation.py:inline_markdown`; quel renderer resta
   usato dalla home e non va rimosso. Porta le prove pertinenti di
   `tests/test_build_lists.py` o il loro equivalente locale.
3. **Touchpoint per `bi`** — come indizio da verificare in loco, non ordine
   alla lettera: il tuo fork ha esteso `PAGES` a una lista di sezioni per
   pagina (struttura stabile + coda, nominate esplicitamente) per ottenere lo
   stesso risultato — rendere sia la panoramica strutturale sia la coda. Il
   contratto nuovo lo ottiene senza whitelist di nomi: verifica se la tua
   estensione locale è ancora necessaria o se puoi tornare al canone,
   riducendo la divergenza. Se hai ragioni locali per restare parametrizzato
   per nome (per esempio per escludere deliberatamente una sezione dalla
   vista), motivale: non è più il canone a richiederlo.
4. Rigenera le viste e verifica `git status` vuoto alla seconda rigenerazione
   consecutiva (determinismo) — stesso presidio di `constraint`/`view` già in
   uso nel gate `/commit`.
5. Se la tua collezione mescola, sotto la stessa intestazione della coda,
   prosa storica di fili consumati senza un'intestazione propria: sappi che
   ora renderizza anche quella (cfr. il watchpoint aperto in
   `i3/liste-o3-i1-fedeli-alla-fonte.md`). Non è richiesto potarla per
   recepire questa prescrizione; se scegli di farlo, è una decisione
   editoriale locale sul contenuto della tua collezione, non un obbligo del
   canone.

## Chiusura

La prescrizione resta attiva finché i sei adottanti non hanno recepito la
riscrittura nel proprio fork (dove esiste una vista equivalente) e aggiornato
il marker `i3/allineamento-metodo.md`. Un repo senza vista a elenco generata
non ha nulla da recepire qui.
