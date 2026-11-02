---
description: Audit runtime-o1 periodico dei progetti adottanti — ciò che si vede solo guardandoli insieme, con la parte meccanica in o3/adottanti.py audit e il giudizio sul campione di decisioni — senza toccare le code locali
user-invocable: true
---

# adottanti

Esegui questa skill dalla root di `metodo`. È l'**o1-runtime** del ciclo:
l'audit periodico top-down sui progetti adottanti dichiarati in `world.md`.
Risponde a una domanda sola: **che cosa si vede solo guardando i repository
insieme?** Mai «ecco i tuoi task». È una skill di dominio di `metodo` (il suo
Mondo runtime sono gli adottanti): non fa parte del quartetto e gli adottanti
non la forkano.

La cadenza è la riga `(mensile)` in `## Scadenze` di `o1/plan.md`; gli esiti
vanno nel filo [`i3/audit-adottanti.md`](../../../i3/audit-adottanti.md),
riscritto in place a ogni giro.

## Confini (la lama)

- **Sola lettura** sui repo adottanti: nessun file scritto, nessun task
  proposto o inserito nelle loro code.
- **Niente doppioni**: ciò che il `/method` locale, i giri giornalieri o la
  coda dell'adottante già coprono resta a loro. La composizione delle code è
  un indizio debole (`kb/development-goal.md`): qui ne restano due numeri, non
  una lettura.
- Se emerge drift di canone, l'atto top-down è una **prescrizione in `o3/`**;
  se risale una lezione dal basso, è un **segnale in `i1/`**; tutto il resto è
  coda di dominio e non ci riguarda.
- Quando un progetto entra nel territorio, l'ingresso segue la procedura
  [`o3/ingresso-adottante.md`](../../../o3/ingresso-adottante.md): è un
  evento fuori giro, non un audit aggiuntivo.

## Procedura

### 1. Rapporto meccanico

Aggiorna i riferimenti remoti con un `git fetch` per adottante (`fetch` è
concesso anche sui checkout di altre sessioni), poi lancia:

```
python3 o3/adottanti.py audit
```

Lo script legge `origin/main` e non scrive nei checkout. Il rapporto ha sette
sezioni:

- **canale**: marker, ritardo verso HEAD, canone non recepito oltre la soglia;
- **prescrizioni aperte**: `prescrizioni.py` contro la voce del marker;
- **viste**: build `--check` sull'estrazione, `/_stato` contro `origin/main`,
  porta raggiunta, per i sei e per `metodo`;
- **accenti**: copia in `world.md` contro `project.py`, unicità sull'insieme;
- **skill**: quartetto, `/cycle` e `/method`, con i wrapper Codex speculari;
- **casi della delega** «da inoltrare», con l'età e la presenza in
  `method/i1/`;
- **code e giri**: righe dev/runtime e giri autonomi del mese.

Ogni scarto è una riga `ROSSO`. Hash uguali non provano un rendering
corretto, e una porta non raggiunta resta «non verificata», non fresca.

### 2. Giudizio

Due cose, e nient'altro:

- **i rossi**: per ognuno, prescrizione o3, segnale i1 o niente, con la
  fonte letta. Un rosso falso (lo script segnala ciò che non è uno scarto) si
  dichiara e, se ricorre, diventa una correzione dello script;
- **il campione di decisioni**: una decisione `Autonomia: agente` per
  adottante, fuori dal giro schedulato, letta **contro il diff** e non solo
  contro il motivo (filo `i3/verdetto-piu-sicuro-del-materiale.md`).
  Includi autonomie riuscite e conferme inutili, non solo i problemi. Un
  episodio motiva una domanda locale, non un obbligo per tutti; ogni modifica
  alle condizioni della delega torna al custode.

Dichiara perimetro e limiti: l'assenza di rossi non prova l'assenza di
attrito.

### 3. Chiudi il giro

- Riscrivi `i3/audit-adottanti.md` nella forma breve, al massimo una
  schermata: rossi aperti con la loro classificazione, esito del campione,
  limiti. Le fotografie restano nel rapporto e in git. Aggiorna la riga del
  filo in `i3/verdicts.md`.
- Avanza la riga `(mensile)` di `o1/plan.md` alla prossima occorrenza.
- Riporta in conversazione il tempo impiegato, i rossi con la loro
  classificazione e l'esito del campione.
