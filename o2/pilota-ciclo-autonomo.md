---
sintesi: "Un adottante scelto insieme fa girare il ciclo autonomo a intervalli concordati per un periodo di osservazione, e il suo esito decide se e come estenderlo agli altri."
ciclo: dev
---

# Pilota del ciclo autonomo

Un repo fa da apripista per il loop agentico di base, su cui poi si
articolano i loop di dominio.

## Prerequisiti

- Push autonomo recepito nel repo pilota: soddisfatto, recepito dai sette
  il 2026-10-08 (in `bi` con l'eccezione del codice del ciclo).
- Trailer di autonomia e impatto (in `/commit` dal 2026-10-08) e sezione
  «fatto» della home: il custode
  deve vedere i giri prima di toglierne la conferma.
- Criteri per il ciclo autonomo schedulato concordati nel register: la delega
  corrente copre solo cicli avviati dal custode.
- La scelta di dove gira il ciclo autonomo: timer systemd dal modulo `cicli` di
  `nixos` (`6a6a7ed`), con Claude Code; collaudato al gradino 0 di `salute`.
- Il ciclo autonomo visibile nella home, con semaforo e pagina del giro
  ([home](home-fatto-da-fare.md)): va in parallelo al ciclo autonomo, prima del
  gradino 1.

## Scelta del pilota e gradini

Decisa dal custode il 2026-10-11: due piloti in parallelo, uno per host,
`salute` su `deck` e `crm` su `svezia`. Il ciclo autonomo di runtime è
direzione costitutiva del metodo (`goal.md`): tutti i repo ci arrivano,
gradualmente, ciascuno con i propri limiti da analizzare.

- **Gradino 0**: l'unità vera avviata a mano dal custode (`systemctl start`).
  È un ciclo avviato dal custode, coperto da `ciclo-delegato`; prova ambiente
  dell'unità, credenziali, permessi, push e tempo massimo.
- **Gradino 1**: timer acceso, cadenza bassa. È il ciclo autonomo schedulato e
  attende i [criteri](criteri-autonomia.md).
- **Gradini successivi**, un repo alla volta per host: su `deck` poi
  `economia`; su `svezia` poi `baserow`, quindi `nixos`, quando il modulo ha
  retto i primi giri, e `bi` in coda; `method` quando il canone ha visto
  girare il ciclo autonomo negli adottanti; `danea-auto` per ultimo, fuori
  `nixos`. Il custode, 2026-10-15: `baserow` passa davanti a `nixos`, perché ha
  una manutenzione semplice e il ciclo autonomo di `nixos` toccherebbe il
  proprio scheduler. Su `svezia` un solo timer acceso alla volta: `baserow`
  entra al gradino 1 dopo che `crm` ha retto il suo.

Perché questi due: `salute` ha checkout solo su `deck`, pochi cambi e nessun
rilascio legato al push, ma dati personali da tenere fuori dalle letture
automatiche verso l'esterno. `crm` dà giri con materia e il suo confine
(checkout che è anche pubblicazione) è già deciso in `autonomy.md`. `nixos`
non apre la scala: il ciclo autonomo toccherebbe il proprio scheduler e il repo che
governa gli host, con più sessioni concorrenti. `baserow` farebbe soprattutto
giri vuoti; `bi` ha ogni push come rilascio; in `method` un errore autonomo
arriva agli adottanti via symlink.

## Andamento

- **`salute`, gradino 0, 2026-10-11** (`deck`): primo giro avviato a mano,
  riuscito con commit `2eb8a69` e push, 4,5 minuti, 77 turni, 1,85 USD
  dichiarati. Skill `eval`, `exec` e `commit` invocate dal tool Skill;
  Calendar via `gog` e push via ssh senza agent funzionano nell'unità. Due
  permessi negati su comandi composti, rifatti spezzati. Il giro ha
  corretto da sé un errore di `o3/health_data.py` che annullava una
  decisione del custode, con test: è il primo caso del campione da rileggere
  contro le fonti. Il custode ha deciso di togliere da `deck` il Drive di
  Letizia, gli altri remote non suoi e la chiave GitHub di Letizia invece di
  recintarli (`nixos` `74b1328`).
- **Sonde del recinto, 2026-10-11** (unità `ciclo-<repo>-sonda`, senza
  Claude): sola lettura sui mount FUSE superata. Lo stop per sessione
  concorrente taceva, perché dal namespace dell'unità `/proc/<pid>/cwd` è
  illeggibile: spostato in un `ExecStartPre=+` fuori dal namespace, ora
  ferma con 15. Con `--setting-sources project` i deny di
  `.claude/settings.json` valgono anche nel ciclo autonomo e i suoi allow si
  ereditano nei workspace fidati; senza fonti il giro perde `CLAUDE.md` e
  skill. Regola da prescrivere: gli allow di `settings.json` stanno dentro
  quelli del file del ciclo autonomo, i deny sono liberi.
- **`salute`, secondo giro manuale, 2026-10-11** (`deck`): riuscito con
  commit `1d7fe22` e push, 2,5 minuti, 44 turni, 0,89 USD. La skill `cycle` invocata in modo `autonomo`, riga `Attenzione:` presente, semaforo
  giallo per proposte e dinieghi. Le correzioni dei permessi del primo giro
  tengono (`sort`, lettura di `method/`). Una foto pressoria illeggibile non
  registrata e lasciata come proposta in `o2/`. Due difetti, dichiarati
  dall'agente stesso: tre dinieghi su `git` (il deny intero su `git branch`
  e `git -C`) e un `Co-Authored-By` che ha staccato i trailer, perché il
  ciclo autonomo non legge `attribution` dalle impostazioni utente. Il giro
  resta fuori dal conteggio degli esiti; `1d7fe22` non si riscrive. Il
  custode ha deciso lo stesso giorno: amend concesso dove è concesso il
  commit, solo prima del push, con la rilettura dei trailer nelle skill
  `commit` e `cycle`; base git comune nella prescrizione
  [ciclo-autonomo](../o3/ciclo-autonomo.md); `attribution` passato
  dall'unità.
- **`salute`, gradino 1, deciso il 2026-10-11** (`deck`): timer ogni giorno
  alle 12:00 dal 2026-10-12 (`nixos` `cd2be2a`), criterio `ciclo-autonomo`
  ratificato con la regola di sospensione (`salute` `308d4ec`): si torna al
  manuale dopo un rosso per atto fuori delega o ricostruzione sbagliata,
  mentre lo stop per sessione aperta, il push rifiutato e il lock occupato
  sono il sistema che funziona. L'orario segue i dati, non il calendario:
  alle 12:00 sono arrivati notte, pratica del mattino e invio manuale del
  custode, perché la sincronizzazione automatica dell'orologio oggi non è
  affidabile. `Persistent=false`: con `deck` spento il giro salta e la home
  lo segna rosso, con `deck` sospeso parte alla ripresa.
- **`crm`, `svezia`**: ripreso il 2026-10-15, col custode sull'host. Prima
  del gradino 0, `/method` in `crm` recepisce `519bdc7` e i passi 5–7 della
  prescrizione [ciclo-autonomo](../o3/ciclo-autonomo.md) rinviati al pilota:
  `.claude/ciclo.json`, `.claude/ciclo-prompt.md`, criterio `ciclo-autonomo`
  in `autonomy.md`, base git comune. Poi l'unità `ciclo-crm` (già dichiarata
  `manuale` in `nixos` `o3/cicli.nix`) si avvia a mano. Il timer arriva dopo
  un paio di giri manuali puliti. Il prompt dice cosa il giro decide da solo
  sui 9 task dev fermi dal 2026-08-21 e cosa lascia in proposta.
- **`baserow`, `svezia`**: secondo su `svezia`, deciso il 2026-10-15. Prima
  del gradino 0 servono la voce in `nixos` `o3/cicli.nix` e i passi 5–7 della
  prescrizione. Il backup manuale senza restore resta riservato al custode
  nel suo criterio `ciclo-autonomo`.

I tempi fra i gradini si decidono sull'andamento delle prove. Si avanza senza
atti fuori delega, senza arresti invisibili e con un campione di giri riletto
contro le fonti; si torna al gradino precedente, per quel repo, alle
condizioni di sospensione sotto.

## Da fissare alla partenza

Fissare prima dell'avvio intervallo, durata, perimetro degli atti delegati,
criteri di riuscita e condizioni di arresto. I prerequisiti dipendono dai
risultati dei tre task: [criteri](criteri-autonomia.md),
[home](home-fatto-da-fare.md) e [esecutore](dove-gira-il-ciclo-autonomo.md).

- Concordare un campione di decisioni e ricostruzioni da rileggere contro le
  fonti, includendo i verdetti modificati: motivo comprensibile e trailer
  corretti non bastano a provarne la qualità.
- Misurare interventi necessari del custode e tempo di ricostruzione degli
  esiti, con un confronto assistito concordato prima della partenza. Il
  beneficio atteso è meno lavoro di supervisione a qualità conservata;
  frequenza dei giri e quantità dei commit non lo dimostrano.
- Osservare i tentativi anche quando non producono commit: mancata partenza,
  arresto e fallimento devono essere visibili al custode.
- Concordare quando sospendere il pilota e come tornare alla modalità
  assistita, almeno per un atto fuori delega, un impatto alto applicato,
  un arresto invisibile o una ricostruzione errata che altera una decisione.

La delega sulla manutenzione dell'artefatto resta distinta dalle azioni di
dominio. L'esperienza di `/manutenzione` in `nixos` non dimostra da sola la
delegabilità di `eval compare`; negli altri candidati vale lo stesso esame
contro il Goal locale.

## Criterio di chiusura

A fine osservazione, verdetto nel filo [ciclo autonomo](../i3/ciclo-autonomo.md)
su fedeltà delle ricostruzioni, rispetto della delega, visibilità degli
arresti e costo per il custode. Dichiarare copertura e limiti del campione;
un pilota privo di casi informativi non certifica l'autonomia. Il custode
decide se estendere, correggere o tornare alla modalità assistita.
