---
data: 2026-11-12
stato: attiva
ciclo: runtime
target: nixos, nixos-lavoro, bi, economia, salute, baserow, danea-auto
---

# L'ultimo giro senza `git log` da quotare

Prescrizione del 2026-11-12, dal task [ricorrenza dei dinieghi](../o2/ricorrenza-dinieghi.md),
decisa dal custode in sessione con `method`.

## Il segnale

`o3/dinieghi.py` ha contato, negli ultimi dieci giri dei quattro repo
leggibili da `deck`, la classe `parentesi` in 13 giri fra il 06 e il
12/11/2026: `method`, `nixos`, `salute` ed `economia`. Sono quasi tutti
gli stessi due gesti con cui `eval` ed `exec` aprono il giro, l'ultimo
commit del giro (`--grep=^docs(ciclo)`) e l'ultimo `Prossimo:`
(`--format=%(trailers:…)`), scritti senza virgolette e negati. Le skill li
scrivono quotati, ma la regola nel punto d'uso non è bastata: per la
decisione del custode del 2026-10-27 serve uno strumento che renda
superflua la grafia.

## Cosa cambia nel canone

- `o3/ultimo_giro.py`, in sola lettura sul repo della cartella corrente:
  stampa il commit dell'ultimo giro (oggetto `docs(ciclo)` con trailer
  `Esiti:`), i suoi `Esiti:` e l'ultimo `Prossimo:` della storia. Con
  `--corpo` aggiunge il messaggio intero del giro.
- `eval compare` lo usa per trovare gli eventi dall'ultimo giro, `exec plan`
  per l'ultimo `Prossimo:`. Il cambio arriva con il normale `/method`.
- Il giro di `method` lancia `o3/dinieghi.py` al passo 4 del perceive: il
  conteggio fra repo resta a `metodo`, che osserva i giri di tutti, e non
  si prescrive.

## Cosa fa l'adottante

1. Recepisce le skill `eval` ed `exec` col proprio `/method`, adattando il
   percorso come per `scadenze.py`: `python3 method/../o3/ultimo_giro.py`.
2. Concede lo strumento nei permessi del giro, `o3/ciclo/permessi.json`:
   `Bash(python3 method/../o3/ultimo_giro.py)` e
   `Bash(python3 method/../o3/ultimo_giro.py --corpo)`.
3. Lo dichiara recepito nel marker `i3/allineamento-metodo.md`, nella forma
   «`ultimo-giro` … recepita».

## Verifica

Nel primo giro dopo il recepimento, la lettura dell'ultimo giro e
dell'ultimo `Prossimo:` non lascia dinieghi; `o3/dinieghi.py` lo vede da sé
nei giri leggibili da `deck`.
