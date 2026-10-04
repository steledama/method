---
data: 2026-10-04
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, danea-auto
---

# Le viste escono in `view/`, il deck curato in `presentation/`

## Cosa e perché

In `presentation/` convivevano due cose diverse: le **viste**, derivate e
rigenerate, e il **deck**, il racconto curato dell'artefatto, scritto e non
derivato. La confusione era arrivata fino a i2, dove in più repo il deck
occupava la collezione delle interpretazioni. Il canone ora le separa
(`kb/view.md`, `kb/presentation.md`):

- `view/` — tutta generata, servita e chiusa su se stessa: la home, una
  pagina 1:1 per ogni `.md` di `goal.md`, `world.md` e delle sei collezioni,
  allo stesso path del repo (`o1/plan.md` → `view/o1/plan.html`), il deck
  reso in `view/presentation.html`, gli asset. Le viste Reveal `tasks` e
  `verdict` e le liste `prescriptions`/`perceptions` sono sostituite dalle
  pagine degli indici e degli item;
- `presentation/` — la sola sorgente del deck, `presentation.md`, con le
  tavole accanto;
- `o3/view/` — i builder (prima `o3/presentation/`), con un solo entrypoint,
  `python3 o3/view/build.py`, e i CSS canonici in `o3/view/assets/`.

Il perimetro reso è più largo di prima: non più solo indici, plan e fili, ma
ogni item delle sei collezioni. `kb/`, README e le istruzioni per gli agenti
restano fuori in ogni repo.

## Ricetta di recepimento

1. **Builder.** `git mv o3/presentation o3/view`, poi prendi dal canone
   `build.py`, `sources.py`, `build_pages.py`, `serve.py`, `assets/` e
   `build_system_image.py` (la sua CONFIG locale si conserva, ma gli `href`
   degli slot puntano ora agli indici: `o1/plan.html`, `o2/tasks.html`,
   `o3/prescriptions.html`, `i3/verdicts.html`, `i2/interpretations.html`,
   `i1/perceptions.html`). `build_views.py` e `build_lists.py` si rimuovono;
   i test locali che li usavano passano a `tests/test_build_pages.py`.
2. **`project.py`.** Allinea al canone: `DECK` punta a
   `presentation/presentation.md` se il repo ha un deck in Markdown;
   `CSS_LOCALI` nomina file in `presentation/`; aggiungi `ESCLUSE`.
3. **Il deck.** Se vive in `i2/` (per esempio `i2/<repo>-in-sintesi.md` con le
   tavole), spostalo in `presentation/presentation.md` con le tavole accanto e
   togli dall'indice `i2/interpretations.md` le voci e la nota di build che lo
   riguardavano. Un builder di dominio (`DECK_BUILDER`) resta in `o3/view/`:
   rileggi i path che usa (`presentation/assets/` diventa `view/assets/`) e
   verifica che la sua pagina passi il presidio. Un deck generato dai dati
   conserva la sua funzione interpretativa: cambiare cartella non la
   cancella, e i contratti runtime dei suoi JSON restano com'erano.
4. **La cartella generata.** Rimuovi le vecchie viste da `presentation/`
   (HTML e `assets/`), lancia `python3 o3/view/build.py` e versiona `view/`.
   In `.gitattributes` i path `o3/presentation/**` e `presentation/**`
   diventano `o3/view/**` e `view/**`.
5. **Esposizione.** `view/` rende ora ogni item delle collezioni. Rileggi i
   vincoli sui dati dove il repo li tiene (`CLAUDE.md` o `world.md`): ciò che
   non deve essere servito sulle reti private va in `ESCLUSE`, oppure resta
   fuori dal repo. La decisione del 2026-10-03 (servizio senza eccezioni)
   non cambia: cambia cosa entra nella cartella, e va scritto.
6. **Servizio permanente, nello stesso giro.** Il servizio dell'host
   privilegiato legge il nuovo path: `view/index.html` come condizione,
   `o3/view/serve.py` come comando. Per `deck` e la coppia server la
   configurazione vive in `nixos` (`o3/modules/home/presentations.nix`):
   finché i repo serviti non sono tutti migrati, la condizione accetta l'una
   o l'altra forma, poi la vecchia si toglie. Per `danea2` la configurazione
   vive in `danea-auto`. Un servizio fermo in silenzio dopo la migrazione è
   l'assenza leggibile mancata.
7. **Skill e bussole.** Nei fork di `/commit`, `exec` e della skill `kb`, il
   comando di build diventa `python3 o3/view/build.py`; README, CLAUDE e
   AGENTS nominano `view/` e `presentation/` per quello che sono.
8. Registra l'esito nel marker `i3/allineamento-metodo.md`.

## Seguito tracciato: `nixos`

Il deck di `nixos` mescola racconto dell'artefatto e lettura causale del boot.
Questa prescrizione ne chiede solo la **migrazione dei path**: la revisione
del contenuto (che cosa resta deck e che cosa torna a i2 come lettura
presidiata) attende l'esito del task `o2/ipotesi-e-confronti-i2-i3.md` in
`metodo`. La prescrizione resta aperta su questo punto finché quel task non
lo sblocca: la migrazione non lo chiude.

## Verifica

Il battito `/adottanti` successivo legge la migrazione nei file, non nei
marker: `o3/view/` presente e `o3/presentation/` assente, `view/` rigenerata
identica da `origin` in una cartella temporanea, deck fuori da `i2/`,
servizio permanente che risponde sul nuovo path dall'host privilegiato.
