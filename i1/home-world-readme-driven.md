---
ciclo: runtime
---

# Segnale: il World della home deve venire dal README e restare dominio

Data: 2026-07-07 · Fonte: `salute`, durante l'allineamento della home statica al
canone di presentazione emerso dagli adottanti

## Il segnale

Allineando `salute` alla home snella già presente negli altri repo, è emersa una
differenza tra due piani che il canone tendeva a confondere: la home come mappa
dell'artefatto e la sezione `World` come dichiarazione del mondo del dominio.

La prima correzione locale ha portato `salute` alla struttura canonica della
home: header `Artefatto`, polo Goal, matrice dei sei atti del ciclo e polo
World. Subito dopo, confrontando i cinque repo con home (`method`, `nixos`,
`bi`, `economia`, `salute`), è emerso che il modello più pulito per i repo di
dominio è `bi`: il builder legge `### Goal` e `### World` dal README e mostra
`World` come semplice testo. In `salute` ed `economia`, invece, il World era
ancora hardcoded nel builder e trasformato in card; in `method` e `nixos` le
card hanno una giustificazione strutturale diversa, perché rappresentano
rispettivamente gli adottanti e gli host.

Applicando la variante README-driven a `salute`, il builder ha fatto emergere un
secondo segnale: la sezione `### World` del README conteneva anche prosa
metodologica e dettagli di pipeline (`world/`, `i1/`, `i2/`, `map.md`). Quando
quella sezione è diventata fonte unica della home, il testo tecnico è finito
visibilmente nel polo World. L'errore non era nel builder ma nel README: il World
non descriveva abbastanza il mondo vissuto del dominio.

## Raffronto osservato

- `bi`: Goal e World sono letti dal README; World è testo semplice sul dominio
  operativo (Danea, WooCommerce, Baserow, Google Sheets, fornitori).
- `salute`: prima del fix, Goal veniva dal README ma World era hardcoded in card;
  dopo il fix, World viene dal README e descrive corpo-mente vissuto,
  sensazioni, emozioni, reazioni, stati mentali, relazioni, visite, referti,
  decisioni e scadenze.
- `economia`: l'HTML generato appare già snello, ma il builder conserva logica
  precedente con World hardcoded in card; rigenerare rischia di riportare il
  drift.
- `method`: caso speciale; il World runtime sono gli adottanti, quindi la resa a
  card deriva da una lista strutturata del README e non da un blocco locale di
  presentazione.
- `nixos`: caso speciale; il World è rappresentato dagli host, derivati dalla
  sezione `## Host` del README, quindi le card sono una mappa strutturale del
  dominio tecnico.

## L'attrito osservato

Il canone dice che `### Goal` e `### World` del README sono heading fissi e
machine-readable, ma non distingue ancora abbastanza tra:

- testo README come fonte della home;
- resa semplice del World per i repo di dominio;
- resa strutturata a card quando il World è una lista di entità strutturali
  canoniche (adottanti, host);
- dettagli di membrana e pipeline, che appartengono alle sezioni operative del
  README o ai nodi, non al polo World della home.

Quando la home legge davvero `### World`, la sezione smette di essere solo
orientamento umano e diventa un contratto: se contiene metodo invece di dominio,
la home lo amplifica. Questo rende il drift visibile.

## Da valutare (i2→i3, non ancora verdetto)

1. Il canone della home deve prescrivere che, per gli adottanti di dominio,
   `Goal` e `World` siano entrambi derivati da `README.md` e resi come testo
   semplice?
2. Le card nel polo World vanno ammesse solo quando derivano da una lista
   strutturale del README (adottanti in `method`, host in `nixos`), non da un
   blocco hardcoded nel builder?
3. Il nodo `readme` deve precisare che `### World` descrive il mondo vissuto o
   operativo del dominio, mentre dettagli su `world/`, strati `i1/i2/o*` e
   register stanno in sezioni operative separate?
4. La propagazione attesa è: `salute` come modello pilota, poi riallineamento di
   `economia` e verifica dei casi speciali `method`/`nixos` senza cancellarne la
   rappresentazione strutturale.
