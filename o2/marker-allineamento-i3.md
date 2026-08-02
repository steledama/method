---
sintesi: "Traslocare il marker di allineamento (method-review.md/method.md) dalla root dell'adottante a i3/allineamento-metodo.md, nome uniforme nei quattro adottanti, cursore e verdetto fusi in un solo file-i3; aggiornare la prescrizione o3/skill-nomi-verbo-sostantivo.md §3 e i riferimenti nel canone di metodo, poi propagare."
ciclo: dev
---

# Trasloca il marker di allineamento a `i3/`, aggiorna prescrizione e propaga

Verdetto e razionale vivono in
[i3/allineamento-marker-stadio.md](../i3/allineamento-marker-stadio.md); qui
restano il lavoro concreto e il criterio di chiusura.

## Lavoro sul canone di `metodo`

1. **Prescrizione**: sostituire §3-4 di
   [o3/skill-nomi-verbo-sostantivo.md](../o3/skill-nomi-verbo-sostantivo.md)
   («il marker non cambia nome») col nuovo canone di posizione — il marker
   trasloca da root a `i3/allineamento-metodo.md`, cursore
   (`method_commit`, `reviewed_at`, `status`) e verdetto narrativo fusi in un
   solo file. Riusa il canale già attivo (stessa prescrizione, stessi quattro
   target) invece di aprirne uno nuovo.
2. **`.claude/skills/method/SKILL.md`**: la sezione «Marker versionato» e
   ogni passo della procedura che nomina `method-review.md` in root vanno
   riscritti sul nuovo path; il template del marker migra dentro il template
   del filo i3.
3. **`.claude/skills/eval/SKILL.md`** (righe 34-35, 72) e
   **`.claude/skills/adottanti/SKILL.md`** (riga 42): i canali che leggono
   «i marker `method-review.md` degli adottanti dalla root» vanno aggiornati
   al nuovo path in `i3/`.
4. **`kb/skill.md`** (riga 112, descrizione della skill `method`) e
   **`world.md`** (riga 8, «superficie da cui si leggono i marker») e
   **`goal.md`** (riga 28, segnale dell'obiettivo 2): aggiornare il
   riferimento.
5. **`o2/rivalutazione-skill-per-arco.md`** (riga 33): il materiale da
   raccogliere al risveglio del 2026-11-01 cita i marker — aggiornare al
   nuovo path perché la raccolta futura non cerchi un file che non esiste
   più.

Non toccare i fili `i3/` storici che narrano un fatto passato datato
(`skill-per-arco-tripartito`, `igiene-stadi-output`, `vista-derivata-e-verificata`,
`audit-adottanti`, `nome-skill-dominio-verbo-o-sostantivo`): descrivono lo
stato del canone nel momento in cui l'hanno osservato, non si riscrive la
storia.

## Propagazione

`nixos` è nello stato più delicato: ha già `method.md` in root (deroga
diretta dal custode, non il default `method-review.md` degli altri tre). La
prescrizione aggiornata deve dirlo esplicitamente — non basta "sposta
`method-review.md`", va coperto anche il caso "hai già un file col nome
sbagliato nel posto sbagliato". Gli altri tre (`bi`, `economia`, `salute`)
partono dal default e traslocano in un solo passo.

## Criterio di chiusura

Prescrizione aggiornata e riferimenti nel canone di `metodo` coerenti (fatto
qui); propagazione recepita dai quattro adottanti (marker in
`i3/allineamento-metodo.md`, root pulita) — **in attesa**, si chiude col
recepimento via `/method` di ciascuno.
