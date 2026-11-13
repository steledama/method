---
sintesi: "Dalla revisione del repo del 2026-11-13 restano due semplificazioni da fare con misure e non alla cieca: snellire le skill eval ed exec, e separare in o3/ gli strumenti dalle prescrizioni senza rompere i path che host e adottanti lanciano."
ciclo: dev
---

# Semplificazione di skill e struttura di `o3/`

## Origine

Revisione del repository chiesta dal custode il 2026-11-13. La bonifica dei
residui, gli indici a una riga, la divisione di `kb/view.md` e la mappa di
lettura di `kb/plan.md` sono fatte (in git dal 2026-11-13). Restano due punti
che la revisione ha indicato e che non si chiudono con una riscrittura in
sessione.

## Skill `eval` ed `exec`

Sono circa 340 righe l'una; la sezione `plan` di `exec` ne occupa 200. A una
lettura completa sono liste di controllo che rimandano ai nodi, e ogni voce
nasce da un caso dei giri: la ripetizione col canone è minore di quanto il
conteggio delle righe suggerisca. Tagliare senza misura rischia di togliere
un presidio a un ciclo che gira ogni giorno in otto repo, coi fork degli
adottanti da riallineare.

Passi:

1. misurare con `o3/skill_tools.py` che cosa le skill ripetono dei nodi e
   quali voci non hanno mosso nessun esito negli ultimi giri;
2. proporre al custode i tagli voce per voce, col caso che ciascuna presidia;
3. applicare, e prescrivere il recepimento solo se cambia il contratto.

## Strumenti e prescrizioni in `o3/`

`o3/` tiene insieme prescrizioni per gli adottanti, procedure interne e circa
7.000 righe di Python. Spostare gli script in una sottocartella romperebbe i
path lanciati dalle unità degli host, dai permessi dei giri e dalle skill dei
sette adottanti (`python3 method/../o3/lanciatore.py`, `o3/view/build.py`).
L'indice ora li registra tutti e l'audit lo verifica (`o3/kb_domain.py`).

Alternative: lasciare la cartella com'è, con l'indice come unica mappa;
spostare le prescrizioni e le procedure in una sottocartella, lasciando fermi
gli script; spostare gli script con una prescrizione ai sette. La seconda
costa meno, ma tocca `o3/prescrizioni.py` e i `/method` che leggono le
prescrizioni.

## Criterio di chiusura

Le due questioni hanno una decisione del custode, applicata o scartata col
motivo.
