---
ciclo: dev
---

# La potatura conserva le regole ma può perdere le verifiche

La rilettura del 2026-10-05 misura separatamente la perdita di conoscenza e
quella del presidio delle verifiche nella potatura `5ea8204` di `metodo`.
È una misura sui file e sulla storia Git, non una verifica del runtime.

## Misura sui sedici fili

Riletti i sedici fili a `5ea8204^`, cercandone la destinazione nel repo
corrente e, per i watchpoint, l'evento atteso negli adottanti. Su sedici:
cinque conservati con le tensioni intatte, due chiusi a ragione, sette
risaliti con una destinazione raggiungibile, due con una lettura viva senza
casa, ripristinata in i2. In più, tre risalite hanno lasciato orfana una
verifica.

- **Conservati e riscritti** (5): `audit-adottanti`,
  `maturazione-nodi-fondativi`, `skill-per-arco-tripartito`,
  `toolchain-builder-presentazione` e `verdetto-piu-sicuro-del-materiale`
  tengono le loro tensioni. L'ipotesi sul montaggio degli scope di dominio
  era già regola in `kb/skill.md`; il watchpoint sulle ritrattazioni di
  `economia` è ora documentato nella [prova sui presidi](presidio-ipotesi-adottanti.md). Si perde solo la nota sul costo di
  discoverability in `bi`, senza lettura che ne dipenda.
- **Chiusi a ragione** (2): `home-minimalista`, con decisioni incise, il
  mini-server «fuori orizzonte» superato dalle presentazioni permanenti e il
  watchpoint sulle tavole generalizzato in `kb/presentation.md` («Fedeltà
  alle fonti»); `liste-o3-i1-fedeli-alla-fonte`, il cui watchpoint si è
  sciolto perché `i1/perceptions.md` non porta più cronaca.
- **Risaliti** (7): `de-cablaggio-binomio-due-agenti` nello `stato: bozza`
  di `kb/agent.md`, con la condizione d'uso reale; `bootstrap-adottanti` e
  `aligned-copre-prescrizioni-aperte` nelle tensioni datate di
  `i3/audit-adottanti.md`; `vista-derivata-e-verificata` in `kb/view.md`
  («Freschezza», con l'escalation); `igiene-stadi-output` in `kb/plan.md`
  (`Ob.`, chiave `S`), con la contraddizione di `economia` sciolta;
  `protocollo-post-evento` e `ricorrenza-per-battito` in `kb/skill.md` e
  `kb/plan.md`.
- **Verifiche orfane** dentro le risalite (3): l'email come superficie i1
  attende ancora la seconda istanza, `acquisti@` di `bi`, che il suo task
  `skill-ordini-fornitori` rinvia; la skill `ordini` di `bi`, prima istanza
  attesa della cadenza in configurazione per entità, esiste dal 2026-07-22 e
  nessuno l'ha valutata; la skill `update` di `nixos`, il cui ramo
  quotidiano doveva collaudare la coesistenza di righe di specie diverse,
  non esiste più. Nessuna lettura corrente ne dipende: per il criterio di
  permanenza tornano a Git, ma sono tre istanze del difetto che il presidio
  deve impedire, con l'evento arrivato e nessun riesame.
- **Letture vive senza casa** (2), ripristinate in i2 con un commit proprio:
  - `attese-a-finestra`: la regola è in `kb/plan.md`, `stato: maturo`, ma la
    verifica attesa è sparita. Il marcatore `!` non compare in nessun commit
    dei plan dei sette adottanti dal 2026-08-22; ora vive in
    `i2/attese-a-finestra.md`. Mostra il limite della regola di potatura:
    lo `stato` di un nodo con più funzioni non porta l'ipotesi di una sola;
  - `ingresso-adottante`: il collaudo prospettico è arrivato con `baserow`
    il 2026-10-05. La prescrizione è stata eseguita e corretta in un punto,
    l'accento delle viste (`f44b6c0`), ma l'esito non era registrato nella
    lettura, ora aggiornata in `i2/ingresso-adottante.md`.

Peso del bisogno nel dominio di `metodo`: la potatura non ha perso
conoscenza stabile, ha perso **verifiche**. Cinque attese su sedici fili
sono rimaste senza presidio, e in tre l'evento era già arrivato. La misura riguarda il canone; non dimostra lo stesso difetto negli adottanti.

## Lettura corrente e provenienza

Lo stato di maturità di un nodo non rappresenta tutte le verifiche delle sue
singole regole. Una potatura deve conservare la raggiungibilità delle ipotesi
ancora in attesa; chiudere una tensione non dimostra la spiegazione.
Le due letture recuperate restano nelle loro case, senza duplicarle qui.

La ricostruzione e le destinazioni sono registrate nel commit `da41329` di
`metodo`; lo stato precedente alla potatura è `5ea8204^`. La misura è distinta
dall'[esito dei bracci](presidio-ipotesi-adottanti.md), che ha portato alla
regola minima in [interpret](../kb/interpret.md) e [verdict](../kb/verdict.md).
