---
ciclo: dev
---

# La ricorrenza ha per soggetto il battito, non la skill

Ratificato (2026-07-12), dalla valutazione i2→i3 della percezione «skill
multi-cadenza via argomento-scope» (catturata da `nixos`, commit `16dc294`,
consumata da questo filo), approfondita su `economia` e `bi`.

Il segnale: in `nixos` il refactor `update-review` → `update` (argomento di
scope `home|system|docker|all`) porta tre cadenze dentro una sola skill —
quotidiana ed esecutiva sul parco AI, settimanale diagnostica sugli host di
casa, mensile diagnostica sui server — e lo stesso argomento `system` aggiorna
risorse diverse (`nixpkgs` vs `nixpkgs-stable`) secondo il ruolo dell'host. Il
canone (`skill.md § Skill di dominio e ricorrenza`) separava già capacità e
ricorrenza ma li riaccoppiava di nascosto: «la ricorrenza → riga» al singolare,
esempi tutti mono-ritmo, `update-review` descritto come «diagnosi settimanale».

**Verdetto: non nasce un nodo dedicato; il soggetto della riga di
`## Scadenze` è il battito** — la coppia invocazione (con scope) + porzione di
mondo su cui insiste — non la skill. La generalizzazione forte è il
raffinamento di una regola che il canone già possedeva, «chi possiede
l'orologio» (`plan.md`): porzioni diverse di mondo possiedono orologi diversi
per la stessa capacità, e persino risorse diverse dietro lo stesso argomento.
Gli strumenti si adeguano al mondo, l'artefatto si conforma. Corollari incisi:

- la skill multi-scope non si spezza per ritmo — solo se diverge la capacità;
- la stessa capacità può essere esecutiva su un ramo e diagnostica su un
  altro: il confine di autorizzazione segue le risorse dello scope;
- a molte entità le cadenze migrano in config dichiarativa per entità (fonte
  di verità, come la config scheduler della terza specie), il plan tiene il
  polso aggregato;
- righe di specie diverse coesistono per la stessa skill (il ramo quotidiano
  di `update` è destinato a riga-macchina via timer systemd, il settimanale
  resta riga-mondo).

Corroborazioni dall'approfondimento: `economia` mostra il mono-battito come
caso degenere (la porzione di mondo di `monthly-review` ha un orologio solo,
la busta paga); `bi` estende su tre fronti — la specifica `ordini` (fornitore
come argomento, default `all`) scala a molte entità con cadenze in config
dichiarativa modulate dalle vendite; la raccolta prezzi concorrenza mette
l'orologio sulla freschezza del dato d'input, non sull'esecuzione (script
idempotenti); lo stesso strumento porta battiti di natura diversa (raccolta vs
manutenzione, due righe semestrali).

Trattamento applicato: rafforzati `skill.md` (ricorrenza per battito,
argomento di scope, corollari, esempi e fatti corretti) e `plan.md § Scadenze`
(raffinamento di «chi possiede l'orologio», coesistenza di righe e specie).
La tripla nixos-specifica (skill + argomento + `mondo` dell'host) resta
istanza di dominio: l'invariante canonico parla di «porzione di mondo», senza
importare la facet locale.

Watchpoint aperti: la skill `ordini` di `bi` è in specifica — quando atterra
sarà la prima istanza reale della config-per-entità e della cadenza modulata
dal mondo; la migrazione a timer systemd del ramo quotidiano di `update`
collauderà la coesistenza di specie per la stessa skill.
