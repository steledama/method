---
ciclo: runtime
---

# Segnale: una skill porta più cadenze via il suo argomento-scope

Data: 2026-07-12 · Fonte: nixos — refactor di `update-review` in `update` con
argomento-scope (`home` | `system` | `docker`)

## Il segnale

Il modello di ricorrenza in `skill.md` / `plan.md` lega **una riga di ricorrenza
a una skill**: gli esempi codificati — `monthly-review`, `update-review`,
`elabora-trascrizione` — sono tutti mono-ritmo. In nixos `update-review`, reso
scope-parametrico (`update home|system|docker`), porta **più cadenze dentro una
sola skill**, e la cadenza non dipende solo dall'argomento ma anche dal **ruolo
dell'host** (`mondo: casa | lavoro`):

- ramo **home** (`pkgs-ai`) → quotidiano, tutti gli host, ed **esegue**
  (`nix flake update ai` + `home-manager switch`, autonomo per la regola Home
  Manager di `CLAUDE.md`);
- ramo **system** → **diagnostico**, ma sdoppiato dal ruolo dell'host non solo
  nella cadenza (**settimanale** a casa, **mensile** sui server lavoro) ma
  nell'**input stesso** che aggiorna: `nixpkgs` per gli host di casa,
  `nixpkgs-stable` — pin separato — per i server; lo stesso argomento `system`
  mappa su risorse diverse secondo il `mondo`;
- ramo **docker** (server) → **diagnostico**, mensile, accompagna il giro
  mensile del `system` dei server.

La ricorrenza non si attacca alla skill, e nemmeno alla sola coppia (skill +
argomento): si attacca a **(skill + argomento + `mondo` dell'host)**. La stessa
capacità compare **più volte** in `## Scadenze` — una riga per cadenza — e lo
stesso argomento (`system`) porta secondo il `mondo` non solo cadenze diverse ma
una **risorsa diversa** da aggiornare (`nixpkgs` vs `nixpkgs-stable`): prova
concreta che il ritmo — e ciò che il ritmo tocca — non è proprietà della skill.

## L'attrito osservato

Con «una skill → una riga», la voce `## Scadenze` di `update-review` era
etichettata `(settimanale)`, ma il ramo AI l'utente lo aggiorna **ogni giorno**,
prima di lavorare, su qualunque host. La cadenza settimanale registrata — anche
in `skill.md` come «diagnosi settimanale» (righe 117-118, 148) — è **falsata
dalla realtà**: nasconde il ramo quotidiano e la natura esecutiva ormai assunta
dal ramo home. Modellare la ricorrenza sulla skill costringe a dichiarare una
cadenza sola per una capacità che ne ha diverse — per argomento e per ruolo
dell'host — e a scegliere «esegue» o «diagnostica» per una che fa entrambe
secondo lo scope.

Il futuro del ramo quotidiano è già previsto dal canone (terza specie: run
automatizzato senza data, config dello scheduler come fonte di verità): un timer
systemd renderebbe quel ramo una riga-macchina, lasciando il ramo settimanale
come riga-mondo. Anche questo suppone che le due righe possano coesistere per
**la stessa** skill.

Nessun verdetto qui (i1 è valenza-neutro): se questo generalizzi — la riga di
`## Scadenze` è per (skill + argomento + `mondo` dell'host)? una skill
multi-scope resta una skill o va spezzata? come si scrive una cadenza che dipende
dal ruolo dell'host in un plan condiviso tra host? — e la correzione dei fatti su
`update-review` (una cadenza settimanale → quotidiano / settimanale-casa /
mensile-server; diagnostica → esegue sul ramo home) sono valutazione i2→i3 in
`method`.
