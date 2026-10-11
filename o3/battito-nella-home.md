---
data: 2026-10-11
stato: attiva
ciclo: runtime
target: salute, nixos, bi, economia, crm, danea-auto, baserow
---

# Il battito si vede nella home

## Cosa e perché

Il custode ha deciso il 2026-10-11, dopo il primo giro reale del battito
(`salute` su `deck`, gradino 0): la manifestazione del battito nella vista
va **in parallelo** al battito stesso, non dopo. È la punta degli strumenti
di controllo e verifica, la gamba che fa da bilancia all'autonomia (`goal.md`
di `metodo`, Goal di sviluppo). Senza, un giro fermato prima del commit non
lascia traccia nella vista, perché la pubblicazione parte dal commit.

Il canone delle viste (`kb/view.md`, «Stato operativo letto a richiesta: il
battito») ora:

- rende in cima alla home gli **ultimi cinque tentativi** col semaforo:
  **verde** riuscito con commit e push e niente per il custode; **giallo**
  riuscito ma con permessi negati o voci di attenzione; **rosso** arresto,
  errore, timeout, commit senza push, giro senza chiusura, partenza mancata;
- porta da ogni riga alla **pagina del giro**: dati del tentativo, commit coi
  trailer, resoconto dell'agente, comandi e strumenti invocati, permessi
  negati, stream completo;
- legge lo stato **a richiesta**, fuori dalla release, con l'opzione
  `--battito-state` di `serve.py` sulla cartella che il modulo `battiti` di
  `nixos` scrive per il repo (`~/.local/state/battito/<repo>`), rotte
  `/_battito/`;
- dichiara gli stati senza tentativi invece di un vuoto muto: nessun
  battito dichiarato, fuori nixos, mai partito, fonte non leggibile.

Un repo senza battito recepisce lo stesso: la home dice «nessun battito
dichiarato» finché non ci arriva. La direzione è comune, i tempi no.

Il semaforo è calcolato da campi espliciti; il giudizio dell'agente alza,
non abbassa. La voce `attenzione` viene dall'ultima riga del resoconto del
giro: `Attenzione: nessuna` oppure `Attenzione: <voci>`. Se manca, il giro
è giallo: l'assenza di un segnale non è un via libera.

## Ricetta per il /method locale

1. Allineare `o3/view/` al canone: nuovo `battito.py`, modifiche a
   `serve.py`, `build_system_image.py` (sezione in cima alla home),
   `sources.py` (rotte servite a richiesta nel presidio del compartimento) e
   `assets/system-image.css`; test in `tests/test_battito.py` se il repo
   tiene i test delle viste. Un builder di home di dominio aggiunge la
   sezione con `battito.home_section()`.
2. Verificare con `python3 o3/view/build.py --check` e i test; aperta come
   file, la home dice che il battito si legge dalla vista servita.
3. **Solo nei repo con battito** (oggi `salute`):
   - il prompt del giro (`.claude/battito-prompt.md`) fa chiudere il
     resoconto con la riga `Attenzione: nessuna` oppure `Attenzione: <voci>`;
   - gli allow di `.claude/settings.json` stanno dentro quelli del file del
     battito (`.claude/battito.json`); i deny si aggiungono liberamente. Con
     `--setting-sources project` il battito eredita entrambi (sonde di
     `nixos`, 2026-10-11).
4. Registrare nel marker il recepimento o l'adattamento motivato.

Il collegamento dello stato al server delle viste (`--battito-state`) è
dichiarato in `nixos`, dove battiti e viste dello stesso repo devono stare
sullo stesso host: non è un passo dell'adottante.

## Indizi da verificare sul posto

- **salute**: primo destinatario, ha un battito vero da mostrare e il
  prompt da completare con la riga `Attenzione:`.
- **nixos**: oltre al recepimento, il modulo `presentations` passa
  `--battito-state` ai repo che hanno un battito sullo stesso host.
- **danea-auto**: servito da Windows, senza `decisioni.json`: la home dirà
  «nessun battito dichiarato» invece di «fuori nixos» finché il Task
  Scheduler non scrive uno stato nella stessa forma.
- **bi**, **economia**, **crm**, **baserow**: home canonica o di dominio da
  verificare; con un builder proprio la sezione va aggiunta a mano.
