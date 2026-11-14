---
sintesi: "Dal 13/11 sera `o3/adottanti.py` non trova più il checkout di `nixos-lavoro` e lo dà assente: la voce di `world.md` riscritta in `b71e299` va a capo fra la cartella e l'host, e la regex `CHECKOUT` vuole uno spazio. Da scegliere se riunire la riga del register o rendere la regex tollerante agli a capo."
ciclo: dev
decidere: "Riunire su una riga la voce di nixos-lavoro in world.md, o rendere la regex CHECKOUT di o3/adottanti.py tollerante agli a capo?"
---

# Lettura di nixos-lavoro

## Il fatto

Il giro di `method` del 2026-11-14 (tentativo `e8949226`) lancia
`python3 o3/adottanti.py --ssh stato`: `bi` e `baserow` rispondono da
`svezia`, `nixos-lavoro` esce come «checkout assente su questo host e non
raggiungibile». Il giro del 13/11 delle 15:00 lo leggeva ancora
(`c53e570`).

Fra i due giri il custode ha riscritto la voce in `world.md` (`b71e299`,
13/11 19:33): oggi la riga 32 finisce con la cartella, `~/nixos`, e la 33
comincia con l'host, `su svezia`. La regex di `o3/adottanti.py`, riga 94,

```
checkout `~/([\w.-]+)`(?: su `([\w.-]+)`)?
```

vuole uno spazio letterale prima di `su`: con l'a capo l'host non entra,
lo script cerca il checkout su `deck`, dove nessuna cartella della home ha
il remote `tt-sviluppo/nixos`, e dà l'adottante assente. È una lettura
del codice e del testo, non una prova eseguita: il giro non lancia
`python3 -c`.

Conseguenza: finché resta così, giri e audit non leggono marker, stato e
build di `nixos-lavoro`. `o3/prescrizioni.py` importa `adottanti` da
`adottanti.py`, quindi ha lo stesso limite: una prescrizione nuova non
risulterebbe mai recepita da tutti e sette.

## Alternative

- **Riunire la riga in `world.md`**: un ritocco di forma al register, che il
  giro non tocca. Ripara subito, ma la prossima riformattazione può
  ripetere il guasto.
- **Regex tollerante**, `\s+` al posto degli spazi, in `o3/adottanti.py`
  (che serve anche `prescrizioni.py`), con un test sulla voce a capo:
  strumento in `o3/`, quindi proposta. Ripara in modo durevole.

Proposta del giro: la seconda, con la prima come ripiego immediato. Decide
il custode.

## Passi

1. Scegliere l'alternativa.
2. Applicarla e verificare con `python3 o3/adottanti.py --ssh stato` che
   `nixos-lavoro` torni leggibile da `svezia`.
3. Togliere il campo `decidere:` e chiudere il task.
