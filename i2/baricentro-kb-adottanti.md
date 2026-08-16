---
stato: bozza
ciclo: runtime
---

# Baricentro KB: dove sta il contenuto dei quattro adottanti

Interpretazione cross-repo che rilegge i cataloghi `kb/` dei quattro progetti
adottanti — `economia`, `nixos`, `bi`, `salute` — per chiedersi una cosa che da
dentro un singolo nodo è invisibile: **di cosa parla** il contenuto di una KB, e
**dove si colloca** rispetto al ciclo d'azione. Nasce dalla tensione «la KB è
system image _oppure_ una rappresentazione del mondo?», che è mal posta nel verbo:
il system image è la **funzione** — il canale tra agenti che non si parlano, ed è
l'intero artefatto, di cui la KB è il nucleo formalizzato (cfr.
[system-image](../kb/system-image.md)); rappresentazione-del-mondo è il
**contenuto** (cosa denota). Non competono. Questa interpretazione guarda il
secondo asse — il contenuto — e scopre che non è omogeneo: tassella i poli del
ciclo, e ogni repo ha un **baricentro** diverso.

Per natura è **i2-runtime**, non i2-dev: il suo Mondo sono i quattro adottanti,
non i nodi del metodo. È la prima istanza concreta dell'osservatorio cross-repo
che la rilettura a freddo dell'asse dev/runtime ha riconosciuto come il vero
i2/o2-runtime di `method` (cfr. [action-cycle-matrix](../kb/action-cycle-matrix.md),
celle runtime e «cucitura e asimmetrie»: «il vero runtime di `method` è
l'osservatorio sugli adottanti», non la sintesi i2 del metodo). Resta `bozza`: la classificazione è fatta dai
cataloghi più un campione verificato per repo, non nodo per nodo. Il luogo della
verifica piena è la prima slide di ciascun artefatto (cfr.
[action-cycle-matrix](../kb/action-cycle-matrix.md), «Protocollo di
riempimento»).

> **IL RISCHIO È LA COMPLICITÀ CON SÉ STESSI.** Una tipologia che cerca le
> proprie categorie le trova sempre. Vale solo se ogni baricentro riceve un verdetto
> onesto, e solo se «forzato» o «la categoria non basta» è un esito _gradito_,
> non da smussare. Il repertorio d'atto e le sorgenti-come-nodi sono tenuti
> espliciti, non lisciati.

## Scala di classificazione

Ogni nodo è classificato per **dove sta il suo contenuto sul ciclo**, non per come
è scritto:

- **G — Goal / ought** (polo alto): concetti, valori, obiettivi. Il _dove voglio
  andare_. Cfr. [goal](../kb/goal.md).
- **M — Mondo runtime / is** (polo basso): la realtà del dominio su cui l'artefatto
  agisce. Cfr. [world](../kb/world.md).
- **A — Macchina / Mondo-dev** (la cucitura, in mezzo): com'è fatto l'artefatto
  stesso. È il Mondo del ciclo di sviluppo (cfr. [development-meta-cycle](../kb/development-meta-cycle.md)).
- **N — Norma della macchina**: come l'artefatto deve essere costruito o
  mantenuto — invarianti, convenzioni e principi d'ingegneria. Distinta da G
  (motivo e valori del dominio) e da A (descrizione della macchina).
- **O — Atto / repertorio** (contenuto o3, sceso verso la membrana): _come si
  agisce_ — procedure, pratiche. Prescrive l'atto sul Mondo-runtime.
- **S — Sorgente / autorità**: maestri e fonti promossi a nodo. Non è un polo del
  ciclo: è un'**anomalia strutturale**, perché canonicamente le fonti vivono in
  `sources.md`/`world`, non come nodi. È tenuta perché _emerge_ dai dati.

G/M/A/N sono le quattro regioni primarie. O è una forma laterale d'atto e S
un'anomalia strutturale: segnali onesti, non fallimenti da assorbire.

## Verdetto per repo

**economia — baricentro M (Mondo runtime / is).**

- M (maggioranza schiacciante): `carla-tacchi`, `francesco-vannoni`,
  `conto-condiviso`, `deposito-personale`, `successione-pompa-renato`,
  `prima-casa`, `automobile`, `cronologia-decessi`, `nucleo-familiare`, le agenzie
  immobiliari.
- A (scheggia): `ocr`, `struttura-json`, `trascrizione-audio`, `setup-client`,
  `strumenti-google-workspace`.
- G (un nodo): `obiettivi` — «punto di riferimento strategico… ogni decisione va
  letta in relazione a questi obiettivi». Goal-pole esplicito e singolo.
- _Riga onesta:_ un modello del Mondo filtrato dai goal, quasi puro. Nessuna
  forzatura.

**nixos — baricentro A+O (macchina e atto), con una fetta M.**

- A: `server-role` (pattern NixOS, «unica fonte di verità»),
  `configuration-patterns`, `service-management`, `nix-flakes`, `home-manager`.
- O: `server-reboot`, `disaster-recovery`, `update-workflow`, `post-installation`,
  `nixos-rebuild` — repertorio d'atto sugli host.
- M: `network-architecture` (i 5 host reali, 2 reti, IP), `hardware-inventory`,
  `ssh-matrix`, `wireguard-*`.
- G: assente — e legittimamente: il goal è codificabile (`snello + affidabile`),
  non chiede una KB di valori.
- _Riga onesta:_ è la system image **originale di Norman** — l'artefatto che si
  documenta da sé. Il Mondo c'è ma è minoranza.

**bi — baricentro A↔M (span pieno artefatto–mondo).**

- A: `scripts-fornitori`, `scripts-utility`, `architettura-database`,
  `ciclo-vita-prodotto` («nessuno script aggiorna direttamente la meta-tabella…»),
  `matching-engine`, `baserow-api`.
- M: i fornitori _reali_ (`axro`, `biuromax`, `dtk`, `imcopex`, `orikon`,
  `sovamax`), `fornitori-backorder`, `danea`, `sites`, `clienti`.
- G: `obiettivi-strategici` (Goal-pole pieno, «diversificare… efficienza»).
  Singolo.
- _Riga onesta:_ continuità Mondo↔macchina. È il baricentro più _largo_ dei
  quattro — ed è quello che funziona.

**salute — baricentro G+S (ought e autorità), con M e O sottili.**

- G (maggioranza): `sofferenza`, `attaccamento`, `vacuita`, `non-se`,
  `impermanenza`, `liberazione`, `equanimita`, `corpo-mente`.
- S (strato intero): `de-mello`, `goenka`, `mahasi`, `thich-nhat-hanh`, `pirsig`,
  `fromm`, `hillman`, `popper`, `donald-norman`.
- O: le posture — `saluto-al-sole` (sequenza di asana, repertorio d'atto sul
  corpo), `cobra`, `ujjayi`, `kapalabhati`.
- M (scheggia): `storia-clinica`, `sindrome-vasovagale` (nodo completo che
  _spiega_ un'allerta del corpo), `sistema-nervoso-autonomo`, `respiro`.
- _Riga onesta:_ tutto-ought, autorità abbondanti, l'is del corpo a margine. È la
  malattia, ed è il caso più istruttivo proprio perché meno riuscito.

## Lettura spietata

**I quattro baricentri tassellano il ciclo.** economia sta in basso (Mondo/is),
nixos in mezzo (macchina/atto), bi attraversa basso↔mezzo, salute sta in alto
(Goal/ought). Non è simmetria estetica: sono quattro centri di gravità diversi
sullo stesso ciclo. La tipologia non descrive un repo, descrive la **posizione**
di un repo. È il risultato che regge tutto il resto.

**salute tradisce il proprio `principi-salute`.** Il nodo dei principi locali
dichiara: «non mira a costruire un'enciclopedia spirituale… teoria verificata
nella pratica… corpo e mente come unico campo». Il catalogo dice l'opposto: _è_
un'enciclopedia, sbilanciata sulla teoria, col corpo a margine. Lo scarto tra
l'ought-del-metodo dichiarato e il baricentro reale è visibile solo mettendo il
principio accanto al catalogo — invisibile da dentro ciascun nodo.

**L'aneurisma: la prova più affilata.** Non è del tutto assente — è una riga nella
cronologia di `storia-clinica`: «ott 2025: … aneurisma aorta ascendente 46mm
confermato». Ma non esiste un nodo `aneurisma` che spieghi cos'è, cosa significa,
cosa fare — mentre `sindrome-vasovagale`, allerta _meno_ acuta e «presente da
sempre», ha un nodo completo. Nel ciclo: il segnale-Mondo è stato **catturato
(i1)** ma mai **interpretato (i2)** in un nodo su cui il ciclo possa mordere.
È modellata l'allerta vecchia e familiare, non quella nuova e acuta. È il golfo di
valutazione reso letterale: una KB tutta-ought non interpreta il nuovo is che il
corpo le manda.

**La meccanica del golfo.** Un ciclo calcola uno scarto solo se ha entrambi i poli:
un is (cosa risponde il Mondo) e un ought (il Goal). salute ha quasi solo il polo
alto; senza il termine inferiore non c'è confronto, quindi nessun golfo, quindi
nessuna azione generata. È la ragione strutturale per cui «arricchire la KB con
l'autoanalisi» (il corpo reale, le emozioni come _sono_) non è onestà ma
necessità: senza il polo Mondo, l'arco di valutazione non ha su cosa mordere.

**bi: span pieno ma arco-azione runtime bloccato.** Il baricentro largo è la
salute dell'artefatto, ma la macchina costruisce gli script (agisce sul Mondo-dev)
e quasi mai sui dati (Mondo-runtime). Manca il movimento dell'agente IA verso il
basso, sul Mondo. È l'o-runtime debole della matrice, il gradiente di autonomia
fermo.

**Le sorgenti-come-nodi (S) sono un secondo sintomo.** Solo salute promuove i
maestri a nodo; negli altri tre le fonti stanno in `sources.md`/`world`. Coerente
col tradimento di `principi-salute` («fonti come mappe, non sostituiscono
conoscenza-diretta»): una KB che accumula chi-l'ha-detto invece di cosa-è-vero-per-me.

## Verdetto della fotografia 2026-06-20: la tipologia reggeva, con due tensioni

- La tripletta allora in esame, **G / M / A**, copriva i quattro repo senza
  forzare: ogni baricentro cadeva pulito.
- **Tensione 1 — «Macchina» si sdoppia.** Struttura-dell'artefatto (A:
  `server-role`, `architettura-database`) vs repertorio-d'atto (O: `server-reboot`,
  `saluto-al-sole`): la prima descrive il Mondo-dev, il secondo prescrive l'atto sul
  Mondo-runtime (contenuto o3). Il test successivo ha mostrato che «il come» non
  è una sola regione: A descrive la macchina, N ne prescrive la forma, O
  prescrive l'atto.
- **Tensione 2 — le sorgenti (S)** non sono un polo: sono fonti fuori posto. La
  tipologia le segnala come anomalia invece di inventargli una casa — esito gradito.

Zero «forzati» nel senso della matrice: nessun baricentro ha richiesto di piegare
la realtà alla teoria. Ma il caveat anti-complicità resta: i quattro repo li
abbiamo plasmati col metodo. Il test esterno vero è un repo costruito _senza_ il
metodo — vi cadrebbe ancora un baricentro pulito? Finché non lo proviamo, il
risultato è incoraggiante, non conclusivo.

**Aggiornamento 2026-08-12 sul test esterno.** L'ingresso di `crm` come quinto
adottante **non** lo fornisce: è fondato col metodo, struttura prima del codice e
zero adattamenti dichiarati — il caso più plasmato dei cinque, quindi peggiora il
caveat invece di allentarlo. Il candidato è `danea-auto` (cresciuto senza il
canone, valutato per il sesto ingresso), col limite che la sua articolazione
recente viene dalla stessa mano che tiene il canone: condizione, specimen
pre-adozione e limite del risultato stanno in
[maturazione-nodi-fondativi](../i3/maturazione-nodi-fondativi.md). Il conteggio
«quattro» di questa sintesi resta quello del 2026-06-20: è la fotografia di
allora, non un numero da aggiornare.

**Il test è stato eseguito lo stesso giorno, e la condizione di caduta scritta
sopra è stata esercitata.** Esito nel filo; qui conta ciò che tocca _questa_
sintesi. Il baricentro dello specimen (macchina↔is) cade dove la tipologia
predice, quindi il verdetto di giugno regge nella sostanza. Ma le «due tensioni»
diventano **tre**: esiste contenuto **normativo sulla macchina** — norme
d'ingegneria con la motivazione dell'alternativa scartata — che l'ought non
ospita, perché l'ought qui è definito come il polo Goal (valori, obiettivi). E lo
«zero forzati» va **qualificato**: valeva sui quattro cataloghi, non su materiale
esterno, dove è comparso un forzato e **4 unità su 11** sono cadute a due facce
invece che pulite. Entrambe le quantità sono **misurate manualmente** sulla
classificazione dichiarata dello snapshot `fb83c0d`, non stimate né derivate da
dichiarazioni di terzi.

La terza tensione non viene dallo specimen: `kb/design-principles.md` (`maturo`)
è della stessa specie. Non era emersa perché **questa sintesi classificò i
cataloghi dei quattro adottanti e `metodo` si escluse**, mentre i principi di
dominio degli adottanti vivono nei loro README per prescrizione, non come nodi —
il disegno del campione teneva la specie fuori inquadratura. La prima verifica da
fare è quindi interna e mai fatta: applicare la tipologia alla `kb/` di `metodo`.

## Verifica interna sulla KB di `metodo` (2026-08-16)

Unità e criteri sono stati fissati prima della classificazione: i **48 nodi
unici indicizzati** in `kb/kb.md` al commit `6c17107`, uno per unità; codice
primario assegnato per ciò che il nodo denota, non per maturità o forma. La
verifica fu eseguita contro il vecchio insieme G/M/A/O: un nodo veniva marcato
**F** (_forzato_) quando il suo contenuto primario era una norma sulla macchina.
La ratifica del custode del 2026-08-16 ha introdotto **N** per quella specie;
le facce secondarie restano annotate separatamente e non entrano due volte nei
conteggi.

Classificazione completa, ripetibile sul catalogo:

- **G — 15**: `cognitive-artifact-design`, `kb-content-typology`,
  `augmentation-system`, `action-cycle`, `affordance-signifier`, `constraint`,
  `agent`, `processing-layers`, `cognitive-artifact`, `cognitive-system`,
  `goal`, `development-goal`, `world`, `development-meta-cycle`,
  `pace-layering`;
- **M — 1**: `adopter-comparison`;
- **A — 12**: `knowledge-base`, `kb-tools`, `method-observatory`,
  `system-image`, `action-cycle-matrix`, `output`, `input`, `perceive`,
  `interpret`, `specify`, `perform`, `compare`;
- **O — 5**: `cognitive-fidelity`, `zettelkasten`, `karpathy-pattern`,
  `method-development`, `consent`;
- **N — 15** (F nel test sul vecchio insieme): `node`, `project-structure`, `design-principles`, `view`,
  `connection`, `agents`, `claude`, `readme`, `index`, `plan`, `tasks`,
  `verdict`, `git-history`, `skill`, `source-of-truth`.

Le quantità sono **misurate manualmente** sull'elenco corrente del catalogo:
15 + 1 + 12 + 5 + 15 = 48. Non sono stime né derivate da dichiarazioni di
terzi. La maturità dei nodi non è stata usata come evidenza: fra i casi N
convivono `maturo` (`node`, `design-principles`, `connection`) e `bozza`.

Facce secondarie sostanziali, anch'esse verificate sul contenuto:
`knowledge-base` e `system-image` sono G↔A; `method-observatory` è A↔O con
materiale M; `action-cycle-matrix` è A↔M; `cognitive-fidelity` è O↔A;
`zettelkasten` è O↔G; `design-principles` è N↔G; `source-of-truth` è N↔M.
Sono **8 nodi su 48 misurati** a due facce sostanziali; la doppia faccia non
richiede di forzare la regione primaria.

### Cosa mostra il campione interno

La norma sulla macchina è una specie coerente, non una manciata di eccezioni:
**15 nodi su 48 misurati** condividono la stessa forma primaria. I nove nodi dei
componenti (`agents`–`skill`) dicono quale funzione e quale forma deve avere ogni
parte dell'artefatto; `node`, `project-structure`, `view`, `connection`,
`design-principles` e `source-of-truth` prescrivono gli invarianti trasversali.
Collocarli in A confonderebbe descrizione e norma; collocarli in G allargherebbe
il polo Goal fino a includere convenzioni di costruzione che non sono motivi,
valori od obiettivi del dominio.

Il custode ha ratificato il 2026-08-16 la quarta regione **N — norma della
macchina**. La scelta conserva stretti entrambi i confini che il campione aveva
reso visibili: G resta motivo/valore/obiettivo e A resta descrizione della
macchina. I 15 F del test diventano 15 N nella scala rivista; F resta l'esito
storico che ha falsificato il vecchio insieme di celle, non una quinta regione.
Nessun frontmatter dei 48 nodi va migrato, perché la tipologia resta una
classificazione analitica e non una facet.

## Ricaduta nel canone

Questa interpretazione è l'osservazione (i2-runtime). La **generalizzazione**
vive in [kb-content-typology](../kb/kb-content-typology.md): G/M/A/N come quattro
regioni, O e S come forme laterali, il baricentro come diagnosi. È connessa a
[knowledge-base](../kb/knowledge-base.md),
[development-meta-cycle](../kb/development-meta-cycle.md), [goal](../kb/goal.md) e
[world](../kb/world.md). Il nodo resta `bozza`: la lacuna interna è risolta, ma
un secondo specimen esterno indipendente dal custode non è ancora disponibile.

## Riferimenti

- Cataloghi `kb/` dei quattro adottanti (`economia`, `nixos`, `bi`, `salute`),
  letti il 2026-06-20 dai checkout dichiarati nel territorio di `world.md`;
  campione verificato per repo. (La lettura avvenne allora via un symlink di root
  `world/`, superficie che il canone ha poi abolito — i checkout si dichiarano nel
  register, cfr. `world.md`: la provenienza è aggiornata alla superficie reale,
  non alla sua forma di allora.)
- [system-image](../kb/system-image.md), [knowledge-base](../kb/knowledge-base.md),
  [action-cycle-matrix](../kb/action-cycle-matrix.md),
  [development-meta-cycle](../kb/development-meta-cycle.md), [goal](../kb/goal.md),
  [world](../kb/world.md).
