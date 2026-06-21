---
data: 2026-06-20
stato: bozza
---

# Baricentro KB: dove sta il contenuto dei quattro adottanti

Interpretazione cross-repo che rilegge i cataloghi `kb/` dei quattro progetti
adottanti — `economia`, `nixos`, `bi`, `salute` — per chiedersi una cosa che da
dentro un singolo nodo è invisibile: **di cosa parla** il contenuto di una KB, e
**dove si colloca** rispetto al ciclo d'azione. Nasce dalla tensione «la KB è la
system image dell'artefatto _oppure_ una rappresentazione del mondo?», che è mal
posta nel verbo: system image è la **funzione** (il canale tra agenti che non si
parlano, cfr. [system-image](../kb/system-image.md)); rappresentazione-del-mondo
è il **contenuto** (cosa denota). Non competono. Questa interpretazione guarda il
secondo asse — il contenuto — e scopre che non è omogeneo: tassella i poli del
ciclo, e ogni repo ha un **baricentro** diverso.

Per natura è **i2-runtime**, non i2-dev: il suo Mondo sono i quattro adottanti,
non i nodi del metodo. È la prima istanza concreta dell'osservatorio cross-repo
che la rilettura a freddo del gate cicli annidati ha riconosciuto come il vero
i2/o2-runtime di `method` (cfr. [action-cycle-matrix](../kb/action-cycle-matrix.md),
celle runtime e «cucitura e asimmetrie»: «il vero runtime di `method` è
l'osservatorio sugli adottanti», non il deck). Resta `bozza`: la classificazione è fatta dai
cataloghi più un campione verificato per repo, non nodo per nodo. Il luogo della
verifica piena è la prima slide di ciascun artefatto (cfr.
[action-cycle-matrix](../kb/action-cycle-matrix.md), «Protocollo di
riempimento»).

> **IL RISCHIO È LA COMPLICITÀ CON SÉ STESSI.** Una tipologia che cerca tre
> categorie le trova sempre. Vale solo se ogni baricentro riceve un verdetto
> onesto, e solo se «forzato» o «la categoria non basta» è un esito _gradito_,
> non da smussare. I due punti dove la tripletta si tende — il repertorio d'atto
> e le sorgenti-come-nodi — sono tenuti espliciti, non lisciati.

## Scala di classificazione

Ogni nodo è classificato per **dove sta il suo contenuto sul ciclo**, non per come
è scritto:

- **G — Goal / ought** (polo alto): concetti, valori, obiettivi. Il _dove voglio
  andare_. Cfr. [goal](../kb/goal.md).
- **M — Mondo runtime / is** (polo basso): la realtà del dominio su cui l'artefatto
  agisce. Cfr. [world](../kb/world.md).
- **A — Macchina / Mondo-dev** (la cucitura, in mezzo): com'è fatto l'artefatto
  stesso. È il Mondo del ciclo di sviluppo (cfr. [nested-cycles](../kb/nested-cycles.md)).
- **O — Atto / repertorio** (contenuto o3, sceso verso la membrana): _come si
  agisce_ — procedure, pratiche. Prescrive l'atto sul Mondo-runtime.
- **S — Sorgente / autorità**: maestri e fonti promossi a nodo. Non è un polo del
  ciclo: è un'**anomalia strutturale**, perché canonicamente le fonti vivono in
  `sources.md`/`world`, non come nodi. È tenuta perché _emerge_ dai dati.

I primi tre (G/M/A) sono la tripletta-bersaglio. O e S sono i due punti dove la
tripletta si tende: il segnale onesto, non un fallimento.

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

## Verdetto: la tipologia regge, con due tensioni

- La tripletta **G / M / A** copre i quattro repo senza forzare: ogni baricentro
  cade pulito.
- **Tensione 1 — «Macchina» si sdoppia.** Struttura-dell'artefatto (A:
  `server-role`, `architettura-database`) vs repertorio-d'atto (O: `server-reboot`,
  `saluto-al-sole`): la prima descrive il Mondo-dev, il secondo prescrive l'atto sul
  Mondo-runtime (contenuto o3). Non rompe la tripletta — la raffina: «macchina» è
  «il come», con due facce.
- **Tensione 2 — le sorgenti (S)** non sono un polo: sono fonti fuori posto. La
  tipologia le segnala come anomalia invece di inventargli una casa — esito gradito.

Zero «forzati» nel senso della matrice: nessun baricentro ha richiesto di piegare
la realtà alla teoria. Ma il caveat anti-complicità resta: i quattro repo li
abbiamo plasmati col metodo. Il test esterno vero è un repo costruito _senza_ il
metodo — vi cadrebbe ancora un baricentro pulito? Finché non lo proviamo, il
risultato è incoraggiante, non conclusivo.

## Ricaduta: il nodo a venire

Questa interpretazione è l'osservazione (i2-runtime). La **generalizzazione** —
un nodo `kb/` sulla tipologia-contenuto della KB (la tripletta G/M/A, le due
tensioni, il baricentro come diagnosi) — è il passo separato che ne discende, da
connettere a [knowledge-base](../kb/knowledge-base.md),
[nested-cycles](../kb/nested-cycles.md), [goal](../kb/goal.md) e
[world](../kb/world.md). Tenere distinti osservazione e nodo evita di canonizzare
quattro casi prima che il test esterno li metta alla prova.

## Riferimenti

- Cataloghi `kb/` dei quattro adottanti (`economia`, `nixos`, `bi`, `salute`),
  letti via `world/` il 2026-06-20; campione verificato per repo.
- [system-image](../kb/system-image.md), [knowledge-base](../kb/knowledge-base.md),
  [action-cycle-matrix](../kb/action-cycle-matrix.md),
  [nested-cycles](../kb/nested-cycles.md), [goal](../kb/goal.md),
  [world](../kb/world.md).
