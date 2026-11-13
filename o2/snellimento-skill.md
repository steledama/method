---
sintesi: "Dalla revisione del repo del 2026-11-13: snellire le skill eval ed exec con misure e non alla cieca. Fino al riesame del 2026-12-01 del ciclo autonomo si fa solo la misura con o3/skill_tools.py; i tagli si propongono dopo, voce per voce."
ciclo: dev
---

# Snellimento delle skill `eval` ed `exec`

## Origine

Revisione del repository chiesta dal custode il 2026-11-13. La bonifica dei
residui, gli indici a una riga, la divisione di `kb/view.md` e la mappa di
lettura di `kb/plan.md` sono fatte (in git dal 2026-11-13). Resta lo
snellimento delle due skill, che non si chiude con una riscrittura in
sessione.

## Stato

Le skill sono circa 340 righe l'una; la sezione `plan` di `exec` ne occupa 200. A una lettura completa sono liste di controllo che rimandano ai nodi, e
ogni voce nasce da un caso dei giri: la ripetizione col canone è minore di
quanto il conteggio delle righe suggerisca. Tagliare senza misura rischia di
togliere un presidio a un ciclo che gira ogni giorno in otto repo, coi fork
degli adottanti da riallineare.

## Decisioni

Il 2026-11-13 il custode ha deciso:

- i tagli aspettano il riesame del 2026-12-01 del filo
  [ciclo autonomo](../i3/ciclo-autonomo.md): cambiare le skill durante
  l'osservazione mescolerebbe due cause se un giro peggiora, come per la
  traduzione;
- prima di allora si fa solo la misura, che non cambia nulla;
- la struttura di `o3/` resta com'è. Il problema era che gli strumenti non si
  trovavano: ora l'indice li registra tutti e l'audit lo verifica
  (`o3/kb_domain.py`). Spostare script o prescrizioni costerebbe una
  prescrizione ai sette, perché i path sono lanciati dalle unità degli host,
  dai permessi dei giri e dalle skill degli adottanti.

## Passi

1. misurare con `o3/skill_tools.py` che cosa le skill ripetono dei nodi e
   quali voci non hanno mosso nessun esito negli ultimi giri;
2. dopo il riesame, proporre al custode i tagli voce per voce, col caso che
   ciascuna presidia;
3. applicare, e prescrivere il recepimento solo se cambia il contratto.

## Criterio di chiusura

I tagli hanno una decisione del custode, applicata o scartata col motivo.
