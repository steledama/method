---
sintesi: "Dal 2026-11-04 nixos è diviso in casa e lavoro; tt-sviluppo/nixos è il settimo adottante, letto da deck via fetch come bi e baserow (deciso dal custode il 2026-11-04). Restano la riga fetch su deck, i checkout incrociati nei task di separazione, accento e vista propri."
ciclo: dev
---

# Nixos di lavoro come adottante

## Origine

Messaggio della sessione `nixos` su `deck`, inoltrato via Herdr su richiesta
del custode il 2026-11-04, solo come informazione: le decisioni restano a
`method`. Fatti verificati lo stesso giorno sui checkout di `deck` dopo un
`fetch`.

## I fatti

- `steledama/nixos` resta il repo di casa (`deck`, `game`, `neve`), checkout
  `~/nixos` su `deck`; ciclo autonomo alle 04:30, marker invariato a
  `6d32921`.
- `tt-sviluppo/nixos` è nuovo e privato, nato con `git filter-repo` dai path
  di lavoro: coppia `norvegia`/`svezia`, checkout `/home/sviluppo/nixos` sui
  server. Marker proprio, stesso cursore `6d32921`, con la nota che gli
  adattamenti nominati per `deck` si rileggono alla prossima revisione.
  Metodo applicato riscritto per la coppia (`8c1d461`); ciclo autonomo non
  ancora attivo, girerà su `svezia`, gradino da decidere.
- Su `deck` il clone `~/nixos-lavoro` punta a `tt-sviluppo/nixos` ed è
  temporaneo. Il task `o2/separazione-repo.md` di lavoro, «Revoca e
  chiusura», toglie `steledama` dai collaboratori di `tt-sviluppo/nixos`
  «salvo decisione contraria del custode». Il gemello di casa dice che il
  `fetch` di `bi` e `baserow` nel ciclo di `method` su `deck` resta, perché
  legge i marker da GitHub e non agisce sui server.
- La lista `fetch` del ciclo `method` in `o3/cicli.nix` di casa è
  `bi`, `baserow`, `danea-auto`: il nuovo repo non c'è.
- `world.md` registra `nixos` come «multi-host», checkout `~/nixos` su
  `svezia`: dopo la separazione non è più vero per nessuno dei due repo.

## Alternative

- **Lettura da GitHub, come `bi` e `baserow`** (consigliata). `steledama`
  conserva su `tt-sviluppo/nixos` un accesso in sola lettura, deroga
  dichiarata alla revoca; `deck` tiene un clone permanente; la sessione
  `nixos` di casa lo aggiunge alla lista `fetch`. È il canale degli altri
  repo di `svezia`, non agisce sui server e rispetta la regola «da `deck`
  non si agisce più sui server».
- **Revoca completa.** Il marker si legge solo in sessione col custode sui
  server; il giro autonomo e la parte meccanica di `/adottanti` dichiarano
  il repo fuori portata. L'osservatorio perde un adottante proprio quando il
  suo metodo applicato va riletto.

## Decisione

Il 2026-11-04 il custode accetta la prima alternativa. Applicato in
`method` lo stesso giorno: voci `nixos` e `nixos-lavoro` in `world.md`,
`Read` del marker in `o3/ciclo/permessi.json`, il repo fra quelli di
`svezia` nel `prompt.md` del giro, «sette adottanti» in `world.md`,
`README.md`, `CLAUDE.md` e plan.

## Cosa resta

- Sessione `nixos` di casa: `nixos-lavoro` nella lista `fetch` del ciclo
  `method` in `o3/cicli.nix`. Finché manca, il giro legge un `origin` che
  nessuno aggiorna e lo dichiara.
- Le due sessioni `nixos`, nei rispettivi task di separazione: niente
  revoca degli accessi incrociati. Il custode ha deciso il 2026-11-04 di
  tenere i checkout incrociati per modificare entrambi i repo da
  entrambi i lati: `tt-sviluppo/nixos` su `deck` (`~/nixos-lavoro`, che
  `method` legge anche per il marker) e `steledama/nixos` sulla
  production. Un checkout è una superficie di modifica del repo, non un
  atto sui server.
- Accento proprio: oggi `o3/view/project.py` del repo di lavoro porta
  `#c2410c` come casa, e `/adottanti` lo segnala ripetuto. Si cambia lì e
  si copia in `world.md`.
- Vista: alla prima pubblicazione dalla production, `host:porta` in
  `world.md`; fino ad allora l'audit la dà assente.

Il task si chiude quando fetch, checkout incrociati, accento e vista sono a posto.

Connessioni:

- [method-observatory](../kb/method-observatory.md)
- [world](../kb/world.md)
