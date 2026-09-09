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
Il generatore ora rende, nell'ordine della fonte, l'intro prima della prima
`##` e ogni sezione `##` per intero — paragrafi e liste, qualunque nome
la collezione dia alle proprie sezioni. Dettaglio e razionale completo in
`i3/liste-o3-i1-fedeli-alla-fonte.md`; principio canonico in `kb/view.md`,
«Il contratto è strutturale, non nominale».

## Ricetta di recepimento

1. Porta la riscrittura di `o3/build_lists.py` (canone: il commit successivo
   a `2891892` che chiude `i3/liste-o3-i1-fedeli-alla-fonte.md`): il render
   diventa un walker generico sulle sezioni `##` del file sorgente
   (`sections()`), non più un estrattore di un blocco sotto un nome fisso
   (`contenuti_items()`). Preserva la tua eventuale parametrizzazione locale
   di `PAGES` (sorgente/prefisso-link/titolo per pagina) — quel livello non
   cambia.
2. Porta la normalizzazione dei link relativi in `presentation.py:inline_markdown`
   (`posixpath.normpath` sul link_prefix combinato): necessaria perché ora si
   renderizzano anche i link nell'intro della collezione, scritti relativi
   alla fonte in punti diversi del file, non solo quelli della coda.
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
