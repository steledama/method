---
data: 2026-10-19
stato: attiva
ciclo: runtime
target: salute, nixos, bi, economia, crm, danea-auto, baserow
---

# Il ciclo autonomo: skill `/cycle`, vista e permessi

## Cosa e perché

Dal 2026-10-11 il ciclo autonomo di runtime è direzione costitutiva del metodo
(`goal.md` di `metodo`, Goal di sviluppo): ogni repo ci arriva, gradualmente,
con un ambito di autonomia dichiarato e strumenti rigorosi di tracciabilità,
controllo e verifica. Il primo giro reale (`salute` su `deck`, gradino 0) ha
retto; il custode ha deciso lo stesso giorno tre cose che valgono per tutti.

1. **Il nome.** «Battito» era una metafora scollegata dalla teoria. Il giro
   `eval → exec → commit` è il **ciclo congiunto** di `autonomy.md`, un
   passaggio completo del ciclo d'azione; quando gira senza custode è il
   **ciclo autonomo**. La skill che lo compone è `/cycle`, in sintonia con
   `/eval` ed `/exec`.
2. **La vista.** Il ciclo autonomo si vede nella home, **in parallelo** al
   ciclo stesso: ultimi cinque tentativi col semaforo (verde riuscito, giallo
   da guardare, rosso bloccato) e da ogni riga la pagina del giro. Lo stato si
   legge a richiesta, fuori dalla release (`kb/view.md`, «Stato operativo
   letto a richiesta»). Un repo senza ciclo autonomo lo dichiara.
3. **I permessi.** Le sonde del 2026-10-11 hanno mostrato che con
   `--setting-sources project` il ciclo autonomo eredita allow e deny di
   `.claude/settings.json`, e che senza fonti di progetto perde `CLAUDE.md` e
   le skill. Il recinto vero è l'unità dell'host; i permessi dell'harness sono
   il secondo, e vanno tenuti larghi sulla lettura e stretti sugli atti.

## Ricetta per il /method locale

**Per tutti.**

1. Forkare la skill `cycle` (`.claude/skills/cycle/SKILL.md` e il wrapper
   Codex), parametrizzando verifiche e criteri del repo; elencarla in
   `CLAUDE.md` accanto a `eval` ed `exec`.
2. Allineare `o3/view/` al canone: `ciclo.py`, `serve.py` (opzione
   `--ciclo-state`, rotte `/_ciclo/`), `build_system_image.py` (sezione in
   cima alla home, o `ciclo.home_section()` in un builder di dominio),
   `sources.py` (rotte servite a richiesta nel presidio del compartimento),
   `assets/system-image.css`; `serve.py` con `--ciclo-unita` per i tentativi in
   `i1/giri`; test in `tests/test_ciclo.py` se il repo tiene
   i test delle viste.
3. Chi aveva recepito `battito-nella-home` rinomina invece di aggiungere:
   `battito.py` → `ciclo.py`, `test_battito.py` → `test_ciclo.py`, classi CSS
   `battito-*` → `ciclo-*`, «battito» → «ciclo autonomo» nei testi vivi.
4. Verificare con `python3 o3/view/build.py --check` e i test; aperta come
   file, la home dice che il ciclo autonomo si legge dalla vista servita.

**Solo nei repo con un ciclo autonomo** (oggi `salute`, `crm`, `economia`,
`nixos` e `method`):

5. File del repo: `o3/ciclo/permessi.json` (permessi del solo ciclo
   autonomo) e `o3/ciclo/prompt.md` (il prompt dell'unità), versionati come
   prescrizioni dell'atto e non in `.claude/`, che è il binding dell'harness
   (`kb/claude.md`, «File dell'harness»; decisione del 2026-10-19). Chi ha
   ancora `.claude/ciclo.json` e `.claude/ciclo-prompt.md` li sposta con
   `git mv` e lo stesso giorno, in `nixos`, dichiara i due path nei campi
   `settings` e `prompt` della propria voce in `o3/cicli.nix`: finché i
   default del modulo restano quelli vecchi, un giro senza i campi si ferma
   con exit 14. `o3/ciclo` è di sola lettura nell'unità: se il pull d'avvio la
   cambierebbe, il giro si ferma con exit 13 (`pull-in-sola-lettura`, `nixos`
   `9e9e5e1`). Ogni modifica a prompt o permessi si tira giù quindi con un pull
   in sessione sull'host del giro, prima del giro successivo. Il prompt si riduce a
   «esegui `/cycle autonomo`» più ciò che è solo locale: criterio di
   copertura e trailer del gradino, host, verifiche, atti sul Mondo.
   Ogni comando che il prompt nomina sta in `o3/ciclo/permessi.json` scritto
   alla lettera: prompt e permessi sono due elenchi dello stesso perimetro,
   e al primo giro divergono (`bi` e `baserow`, 2026-10-16/17, in
   `i2/casi-delega-adottanti.md` di `metodo`). Il confronto è il giro di
   prova: il gradino 0 passa al gradino 1 solo quando un giro non ha
   dinieghi sui comandi del prompt, letti nel campo `dinieghi` di
   `tentativi.jsonl` o nel resoconto. Un diniego si corregge in una sessione
   col custode, nel prompt o in `permessi.json`, mai nel giro.
6. Criterio in `autonomy.md`: `ciclo-autonomo` (il perimetro del giro senza
   custode), distinto da `ciclo-delegato` (il ciclo avviato dal custode).
7. Permessi, regola comune:
   - gli allow di `.claude/settings.json` stanno dentro quelli di
     `o3/ciclo/permessi.json`; i deny si aggiungono liberamente, perché valgono
     anche nel ciclo autonomo;
   - la lettura è larga: oltre a `cat`, `head`, `tail`, `grep`, `jq` e
     `sed -n`, anche `sort`, `uniq`, `cut`, `tr`, `diff` e `hostname`. Un
     comando composto con un solo pezzo non concesso è negato per intero e
     costa turni (due casi nel primo giro di `salute`, uno nel primo di `crm`
     per `hostname`);
   - il checkout di `method` letto dal repo (symlink `method/`) si concede in
     lettura con `additionalDirectories`: fuori dalla cartella di lavoro il
     modo non interattivo nega anche la lettura. La scrittura resta
     impossibile perché l'unità rende la home in sola lettura;
   - git e verifiche hanno una base uguale in ogni repo, che non si spezza
     per cartella:
     - in lettura `git status*`, `git diff*`, `git log*`, `git show*`,
       `git rev-parse *`, `git branch --show-current`, `git pull --ff-only*`;
     - negli atti `git add *`, `git commit *` (amend compreso), `git push`,
       `git push origin <branch>`;
     - i deny che la recintano, in `.claude/settings.json` perché valgono
       anche in sessione: `git add -A*`, `--all*`, `git add .` e
       `git add . *` (non `git add .*`, che nega anche `.claude/` e
       `.codex/`, primo caso in `crm` il 2026-10-15), `--no-verify`,
       ogni forma di force push, `git reset`, `rebase`, `clean`, `checkout`,
       `switch`, `restore`, `stash`, `merge`, `config`, e di `git branch` le
       sole forme che cancellano, rinominano o forzano (`-d`, `-D`,
       `--delete`, `-m`, `-M`, `-f`, `--force`). Un deny vince sempre su un
       allow: `git branch*` intero negava anche `--show-current` (tre
       dinieghi nel secondo giro di `salute`). Non si concede `git -C *`, che
       aggirerebbe i pattern: la skill lavora dalla cartella del repo;
     - l'amend è concesso dove è concesso il commit, perché chi committa
       possa correggere un trailer sbagliato. Corregge solo il commit non
       ancora pubblicato: il force push resta negato, e un amend dopo il push
       lascerebbe il branch divergente e fermerebbe il giro successivo;
   - i file del giro non si modificano nel giro: deny su
     `Edit(./o3/ciclo/**)` e `Write(./o3/ciclo/**)` in
     `o3/ciclo/permessi.json`, che valgono solo senza custode (la sessione
     legge `.claude/settings.json` e lì il custode e l'agente li modificano in
     modo concordato); nessun comando concesso scrive file per via indiretta
     (`sed -i`, `tee`, redirezioni). Il recinto vero è l'unità, che rende
     `o3/ciclo` di sola lettura;
   - `git add -f*` e `git add --force*` sono negati in `.claude/settings.json`:
     il grezzo ignorato di `i1/` non entra nella storia;
   - restano di dominio, per nome e oggetto, gli script del repo e gli
     strumenti sul Mondo (`rclone`, `gog` e simili);
   - gli atti sul Mondo si concedono per nome e oggetto, mai per famiglia
     intera; gli invii verso persone esterne restano al custode, con un
     wrapper nell'unità dove l'harness non basta (es.
     `gog --gmail-no-send`).
8. Tracce del giro in `i1/giri/`, ignorate da git (`kb/perceive.md`): la
   regola `.gitignore` entra in un commit **prima** del primo giro che vi
   scrive, altrimenti il giro successivo trova il working tree sporco e si
   ferma (exit 10). `eval perceive` legge `tentativi.jsonl` del giro
   precedente (dinieghi, errori, costo, durata) e apre la trascrizione solo
   per il dettaglio; una frizione che deve durare diventa una cattura `.md`
   versionata in `i1/`.
9. Registrare nel marker il recepimento o l'adattamento motivato.

Il ciclo autonomo non legge `~/.claude/settings.json`: ciò che lì vale per
tutte le sessioni, come le variabili d'ambiente e `attribution` vuoto (niente
`Co-Authored-By`, che nel secondo giro di `salute` ha staccato i trailer
dall'ultimo paragrafo), lo passa l'unità dell'host.

Lato host, in `nixos` (non è un passo dell'adottante), per la decisione del
2026-10-19: default di `settings` e `prompt` portati a `o3/ciclo/` quando
tutti i repo con ciclo autonomo hanno spostato i file; `o3/ciclo` del checkout
in `readOnlyPaths` dell'unità; un campo per repo (es. `giri = "i1/giri"`) che
porta in quella cartella `tentativi.jsonl`, `ultimo.json` e `giri/`, mentre
lock, `corrente.json`, `sonde.jsonl` e il settings fuso restano nello stato
dell'unità; prima della prima scrittura `ciclo-avvio` verifica con
`git check-ignore -q` che la cartella sia ignorata e altrimenti si ferma con
exit 14; la vista riceve `--ciclo-state <checkout>/i1/giri` e
`--ciclo-unita ~/.local/state/ciclo/<repo>`, perché le decisioni
(`decisioni.json`, alla chiave del repo) restano accanto alla cartella
dell'unità. L'opzione entra con `serve.py` e `ciclo.py` del 2026-10-19 (caso
segnalato da `bi`): il repo la recepisce prima che `nixos` sposti
`--ciclo-state`, altrimenti la vista perde decisione, partenza attesa e stato
`external`.
Già in esercizio: modulo `cicli`
(`o3/cicli.nix`, unità `ciclo-<repo>` e `ciclo-<repo>-sonda`, stato in
`~/.local/state/ciclo/<repo>/`) e `--ciclo-state` passato alla vista del repo
servita dallo stesso host. Le unità non si riavviano a uno switch
(`X-RestartIfChanged=false`): un bump di Claude Code cambia tutte le unità e
interromperebbe i giri in corso. Un repo il cui giro fa `home-manager switch`
dichiara `homeWritable`: la home resta scrivibile e il recinto è solo
l'harness (oggi `nixos`, scelta del custode del 2026-10-16).

## Indizi da verificare sul posto

- **salute**: ha `battito.json`, `battito-prompt.md`, il criterio
  `battito-delegato` e la vista col battito: rinomina tutto (passi 3, 5, 6) e
  applica i permessi del passo 7. Il secondo giro manuale è previsto per il
  2026-10-12.
- **economia**: ha recepito `battito-nella-home` (`05c2f6d`): passo 3, più
  la skill.
- **nixos**: oltre al recepimento, il modulo dei cicli autonomi e le
  presentazioni sono suoi; `/manutenzione` resta una skill di dominio a sé.
- **danea-auto**: servito da Windows, senza `decisioni.json`: la home dirà
  «nessun ciclo autonomo dichiarato» finché il Task Scheduler non scrive uno
  stato nella stessa forma.
- **bi**, **crm**, **baserow**: home canonica o di dominio da verificare; in
  `bi` il push resta su richiesta quando i commit toccano il codice eseguito
  dal ciclo.
