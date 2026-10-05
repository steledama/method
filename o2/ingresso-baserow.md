---
sintesi: "Ingresso di baserow (settimo adottante) nell'osservatorio secondo o3/ingresso-adottante.md. Attende l'adozione locale in ~/baserow, condotta da una sessione lì sul passaggio di consegne di TODO.md (6c51eb7); si sblocca quando il marker locale segna aligned. Qui vivono la condizione, i candidati già classificati e i punti da rileggere."
ciclo: runtime
---

# Ingresso di baserow nell'osservatorio

Task in attesa (`w1`). Il custode ha deciso il 2026-10-05 di portare `baserow`
fra gli adottanti, dopo che un reboot di `svezia` ha mostrato l'assenza di un
backup automatico. L'adozione locale la conduce una sessione in `~/baserow`,
seguendo il passaggio di consegne scritto in `TODO.md` (commit `6c51eb7`).
L'ingresso dal lato `metodo` segue
[`o3/ingresso-adottante.md`](../o3/ingresso-adottante.md) e parte solo quando
l'adozione locale è verificabile.

## Condizione di sblocco

In `~/baserow` esistono il symlink `method/`, `goal.md`, `world.md`, la sezione
README canonica e `i3/allineamento-metodo.md` con `status: aligned`. Il canone
di riferimento al 2026-10-05 è `f21594b7d30f9f92f97053f6c2f6a9de3390997c`: se
`metodo` avanza durante l'adozione, il marker dichiara quale commit ha recepito.

## Candidati già classificati

Ricerca del 2026-10-05, da ripetere all'atto perché il repo nel frattempo
cambia:

- **inventario corrente da aggiornare**: `world.md` (elenco e conteggio),
  `README.md` (i poli, e «sette repo» della sezione canonica, che conta anche
  `metodo`), `CLAUDE.md` (`/adottanti`), `o1/plan.md` (`## Scadenze`),
  `goal.md` (obiettivo 2, da rileggere: mescola inventario e cronaca);
- **baseline da aggiungere**: `i3/audit-adottanti.md`, senza anticipare il
  cursore mensile;
- **fotografie da preservare**: `i2/bootstrap-adottanti.md`, «recepita dai
  sei» in `o3/prescriptions.md` e i fili `i3/` che contano i sei a una data;
  `i3/skill-per-arco-tripartito.md` («sette repository») va riletto prima di
  classificarlo.

## Da verificare all'ingresso

- checkout sullo standby: il 2026-10-05 `norvegia` aveva `~/baserow` a
  `e981bff`, un commit dietro `svezia`;
- perimetro di `view/`: solo hostname, porte e topologia, nessun dato delle
  tabelle né credenziali;
- prescrizioni aperte recepite già nella forma corrente
  (`migrazione-viste`, `esiti-per-stadio-nel-commit`), non in una superata;
- il primo `/adottanti` utile (2026-11-01) è la prima verifica nell'uso: il
  segnale è lo stato del backup raccolto da un `/eval perceive` locale.
