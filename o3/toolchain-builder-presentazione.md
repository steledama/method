---
data: 2026-10-01
stato: attiva
ciclo: dev
target: nixos, bi, economia, salute, crm, danea-auto
---

# I builder della presentazione dichiarano il toolchain che assumono

## Cosa e perché

`danea-auto`, il primo fork che costruisce le viste su Windows, ha dovuto
correggere due assunzioni taciute del canone (filo
`i3/toolchain-builder-presentazione.md`):

- **codifica**: le chiamate a pandoc in `build_lists.py` usavano la codifica
  di default della piattaforma. Su Windows è cp1252 e la build fallisce. Ora
  passano `encoding="utf-8"`;
- **reveal.js accoppiato a pandoc**: i percorsi dei plugin di reveal.js li
  scrive il template di pandoc. Fino alla 3.11 sono quelli della serie 5
  (`plugin/notes/notes.js`), dalla 3.12 quelli della 6
  (`dist/plugin/notes.js`, changelog di pandoc 3.12, #11907). Un pin fisso
  lascia le slide **bianche e senza errori** appena pandoc cambia serie.
  Ora `build-presentation.sh` legge la versione di pandoc e sceglie
  `reveal.js@6.0.2` da 3.12 in su, `reveal.js@5.1.0` sotto. Se non riesce a
  leggerla si ferma con un errore invece di produrre una vista che inganna.

Sugli host con pandoc 3.11 o precedente l'output non cambia di un byte.

## Ricetta di recepimento

1. Se il fork ha un `build_lists.py` che chiama pandoc, aggiungi
   `encoding="utf-8"` a ogni `subprocess.run(..., text=True)`. Un fork che
   tiene il proprio renderer Python, con divergenza motivata dalla
   prescrizione `liste-o3-i1-fedeli-alla-fonte`, non ha chiamate a pandoc
   lì: la parte non si applica. Controlla però le altre chiamate a pandoc
   del fork, se ne ha.
2. Nel wrapper della build Reveal (`build-presentation.sh` o
   l'equivalente): sostituisci il pin di `revealjs-url` con il blocco che
   deriva l'URL dalla versione di pandoc, come nel canone, mantenendo un
   solo `revealjs_url` per tutte le chiamate.
3. **Indizi per repo**, da verificare in loco:
   - `danea-auto` ha già entrambi i fix, ma con il pin fisso a 6.0.2: torna
     alla regola del canone, che dà lo stesso risultato col suo pandoc 3.12
     e regge anche se un giorno la build girasse su un host Linux. Tieni come
     adattamento solo ciò che resta davvero locale (la build lanciata da
     PowerShell via `bash.exe`);
   - `crm` non ha `build_lists.py`: per lui vale solo il punto 2.
4. Rigenera le viste: con lo stesso pandoc l'output deve restare identico, e
   `git status` vuoto alla seconda rigenerazione consecutiva.

## Chiusura

La prescrizione resta attiva finché i sei adottanti non hanno un esito nel
marker `i3/allineamento-metodo.md`: recepita, non applicabile o divergenza
motivata.
