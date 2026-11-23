---
sintesi: "Al posto dell'audit /adottanti, che leggeva ogni adottante, il segnale dal basso arriva a method per issue (segnali) e PR (proposte sul canone), lette come dati e mai come istruzioni e smistate da una skill senza merge automatico. Nell'altra direzione, versioni con changelog al posto del symlink su main: il primo tag serve al gruppo lavoro, primo adottante trattato da estraneo."
ciclo: runtime
---

# Canale in entrata

## Origine

Decisione del custode del 2026-11-23
([diffusione-oltre-custode-unico](diffusione-oltre-custode-unico.md),
«Decisione del 2026-11-23»): `method` si adotta da persone sconosciute su repo
che il custode non controlla. L'audit `/adottanti` presupponeva di leggere
ogni repo via checkout o `ssh` ed è ritirato; il canale con gli adottanti si
rovescia, da osservazione a ricezione.

## Forma proposta

- **Issue per i segnali**: un template «segnale da adottante» con situazione,
  riscontro e questione per il metodo, la stessa forma dei casi della delega
  (`.claude/skills/eval/SKILL.md`, perceive). È il grezzo dal basso che oggi
  entra in `i1/`.
- **PR per le proposte concrete** sul canone: un nodo, uno strumento, una
  skill.
- **Una skill che le legge e le smista**, per esempio `/contributi`:
  segnale da acquisire in `i1/`, proposta da valutare, materia estranea. Non
  fa merge da sola; un merge è un atto del custode.
- **Il testo di un estraneo è un dato, mai un'istruzione**: la skill lo
  dichiara, come le regole sul materiale incollato, perché issue e PR sono il
  punto di ingresso naturale di un'iniezione di prompt.
- **Nell'altra direzione, versioni con changelog**: il primo tag git di
  `method`, su cui il checkout di `svezia` si ferma al posto di `main`. È
  l'atto di `nixos-lavoro`; da qui il recepimento con `/method` legge la
  distanza fra due versioni, non fra due commit qualunque.

## Residui da sistemare

Spostati il 2026-11-23 nel task
[strumenti-del-coordinatore](strumenti-del-coordinatore.md): gli strumenti
che leggono gli adottanti passano ai coordinatori dei gruppi.

## Decisione del 2026-11-23

Il custode decide che gli adottanti aprono issue e PR solo in sessione con
lui: è un atto verso l'esterno, in un posto pubblico.

## Passi

1. ~~Template di issue «segnale da adottante»~~ fatto il 2026-11-23:
   `.github/ISSUE_TEMPLATE/segnale.md`, modello di PR, etichette `segnale`
   e `proposta`.
2. ~~Regola delle versioni e prima versione con note~~ fatto il 2026-11-23:
   `kb/method-development.md`, «Versioni», prescrizione
   `versioni-del-canone` (chiusa il 2026-11-23, in git), rilascio
   `v0.2.0`.
3. ~~Il gruppo lavoro passa al tag~~ fatto il 2026-11-23: tutti e cinque
   a `v0.2.0`, `danea-auto` compreso (dichiarazione del custode).
4. Skill di smistamento dei contributi, con la regola dei dati non fidati.
   Si progetta sulla prima issue vera, non a tavolino: la candidata è il
   segnale sul Goal S di `salute`, scritto con la regola dei repo privati.

## Criterio di chiusura

Un segnale del gruppo lavoro arriva a `method` come issue o PR, la skill lo
smista e il canone lo acquisisce o lo scarta senza che `method` abbia letto il
repo di lavoro.

Connessioni:

- [diffusione-oltre-custode-unico](diffusione-oltre-custode-unico.md)
- [method-observatory](../kb/method-observatory.md)
