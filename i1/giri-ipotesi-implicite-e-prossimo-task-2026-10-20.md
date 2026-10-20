---
ciclo: runtime
---

# Giri autonomi: ipotesi implicite e prossimo task non registrato

Data: 2026-10-20 · Fonte: sessione col custode su `deck`, lettura dei commit
pubblicati di `bi`, `danea-auto` e dei trailer `Esiti:` dei sette dal
2026-10-11; skill `cycle` ed `exec` canoniche e codice di `o3/view/`.
Sollevato dal custode leggendo i resoconti dei giri.

## Un'ipotesi formata e smentita senza passare da `interpret` (`bi`)

- **19/10** (`bi` `6a0bc3d1`, `Esiti: … interpret=vuoto …`): in
  `o2/diagnosi-crescita-orfani.md` il giro scrive «dopo il 16/10 non è
  entrato nessun orfano nuovo e nessuno è uscito, perché l'uscita passa da
  `wl`/`bl`, scritture manuali». Spiegazione causale scritta come fatto,
  dentro un task, senza criterio di smentita né orizzonte; nessuna voce in
  `i2/`.
- **20/10** (`bi` `8635f663`, di nuovo `interpret=vuoto`): il dato feriale
  la contraddice (87 ingressi con data feed 19/10, uscite da date
  precedenti) e il giro scrive «la tesi del 19/10 … è smentita o
  incompleta».
- La tesi è ricostruibile da git perché il secondo giro l'ha citata, non
  perché il primo l'avesse marcata. La smentita è arrivata dal dato, non da
  un riesame.

Contrasto nello stesso periodo: `danea-auto` scrive nel filo
`i3/rallentamento-libreoffice.md` una previsione datata con criterio
(«intorno al 13/10», `230f1e2`) e il giro del 15/10 la riconosce da solo
(`i2/presidio-ipotesi-adottanti.md`, osservazione chiusa).

## Il prossimo task non arriva al custode

- `/exec plan`, passo 4, chiede di chiudere «indicando il task consigliato»;
  il resoconto finale di `/cycle` non lo elenca, e la pagina del giro rende
  solo il resoconto. Nessun campo della vista porta il prossimo task.
- Dall'11/10, `plan=vuoto` è l'esito più frequente dello stadio: `salute`
  7 su 8, `economia` 6 su 8, `bi` 4 su 5, `crm` 4 su 5, `method` 5 su 5
  (`nixos` 3 su 6, `baserow` 0 su 4, `danea-auto` 0 su 3, conteggio dai
  trailer su `origin`). «Vuoto» non distingue la testa della coda riesaminata
  e confermata dalla coda non guardata; un cambio di priorità non ha un
  segno proprio.

Il custode considera la revisione delle priorità il centro del ciclo: nuove
percezioni → verifica delle interpretazioni in `i2/` → confronto coi goal
(o proposta di correggerli) → dipendenze e priorità → prossimo task
confermato o cambiato, con il cambio evidenziato.
