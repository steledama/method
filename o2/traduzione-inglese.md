---
sintesi: "Inglese lingua canonica, italiano secondario (custode, 2026-11-07). Forma decisa e fissata in kb/translation.md con il controllo o3/traduzioni.py nel gate; restano le traduzioni a lotti, da avviare su indicazione del custode."
ciclo: dev
---

# Traduzione in inglese

## Origine

La proposta l'ha portata la sessione `nixos` su `deck`, inoltrata il
2026-11-07 su richiesta del custode, insieme alla licenza: prima la licenza
(commit `d00059d`, che copre anche le traduzioni), poi la traduzione. Il
messaggio non porta autorizzazioni nuove.

## Decisioni

Il 2026-11-07 il custode ha deciso:

- la lingua principale è l'inglese, quella secondaria l'italiano: fa fede
  l'inglese;
- accettate le proposte su perimetro, allineamento, adottanti e ordine;
- collocazione nel file gemello (`kb/node.it.md`), non in un albero
  separato;
- si fissa la forma, le traduzioni non ancora.

La forma vive in [translation](../kb/translation.md); il controllo
deterministico è `o3/traduzioni.py check`, lanciato dal gate di `/commit`.

## Da fare, su indicazione del custode

In pausa dal 2026-11-12 (`p1` nel plan), su decisione del custode: si
riprende al riesame
del 2026-12-01 del filo [ciclo autonomo](../i3/ciclo-autonomo.md), o prima
se serve un lettore in inglese. Così il cambio di lingua non si mescola ai
`/method` degli adottanti mentre il ciclo autonomo è in osservazione.

- **Lotti.** Ogni lotto riscrive in inglese il sorgente e ne deriva il
  gemello italiano con `fonte:`. Si comincia da `README.md` e dall'hub
  `cognitive-artifact-design.md`, poi i nodi `kb/` e il deck.
- **Solo inglese.** Le collezioni `i1/`–`i3/` e `o1/`–`o3/`, i register,
  `CLAUDE.md`, `AGENTS.md`, `autonomy.md` e le skill passano all'inglese senza
  gemello.
- **Strumenti.** Le etichette che gli strumenti cercano nei testi (per
  esempio `Connessioni:` in `o3/kb_tools.py`, le sezioni delle viste) vanno
  rese bilingui o tradotte insieme al lotto che le tocca, perché l'audit non
  si rompa.
- **Nomi dei file.** Oggi convivono indici in inglese (`prescriptions.md`,
  `verdicts.md`) e strumenti in italiano (`prescrizioni.py`, `scadenze.py`,
  `lanciatore.py`), e item delle collezioni in italiano. Da decidere prima
  del primo lotto se i nomi passano all'inglese: gli script sono path che
  host e adottanti lanciano, quindi una rinomina chiede una prescrizione
  (rilievo della revisione del 2026-11-13).
- **Adottanti.** Il cambio di lingua del canone si recepisce con il normale
  `/method` di ciascun adottante: la delega di questo repo non li copre.
  Quando i primi nodi passano all'inglese, una prescrizione in `o3/` lo
  segnala.
