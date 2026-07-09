# Segnale: il significato senza artefatto discrimina `world` e substrato

Data: 2026-07-09 · Fonte: `bi`, durante la migrazione del substrato runtime fuori dalla root

## Il segnale

Operando in `bi` sulla migrazione delle cartelle runtime (`output/`, `data/`,
`foto/`, `pending/`, `processed/`) è emerso un discriminante pratico per il
confine fra substrato interno e membrana `world`:

> se l'artefatto sparisse domani, questo contenuto avrebbe ancora significato
> operativo per il dominio?

Il test ha riclassificato `foto/` contro l'ipotesi iniziale. Le foto prodotto
nominate per SKU non sono substrato i1: sono asset del business. Restano utili
per sito, listini, operatori e venditori anche senza BI. Il contratto umano SKU
rafforza la classificazione: l'operatore che deposita immagini nominate per
codice compie un atto del mondo, non una scrittura interna dell'artefatto.

La controprova è che il test non promuove tutto a `world`: `drift-report.json`
muore senza il ciclo che lo produce e lo legge; `1_backorders.json` è
interscambio fra script; `arles-stocklist.csv` è uno snapshot fornitore superato
dal run successivo. Questi contenuti non hanno autonomia di significato senza
BI, quindi restano substrato dello stadio appropriato o traccia o3.

## L'attrito osservato

La classificazione precedente per cartella e per ruolo di pipeline portava a
leggere `foto/` come cattura i1 o staging di `fotoUpload`. Il contenuto, però,
ha due proprietà diverse dal substrato:

- sopravvive semanticamente all'artefatto che lo usa;
- viene scritto anche da attori del mondo, non solo dall'artefatto per sé stesso.

Questa distinzione produce conseguenze operative falsificabili in `bi`:

- HA: oggi un failover perde il magazzino foto, presente solo su `norvegia`;
  sul mount condiviso i due host vedrebbero lo stesso stato;
- superficie umana: su Drive l'operatore gestisce le immagini da GUI e da
  qualunque dispositivo, senza SSH;
- autonomia del repo: un clone BI resta completo senza trascinare centinaia di
  MB di JPG.

Il medium resta una decisione tecnica: prima del cutover serve prova I/O reale
su rclone (`fotoUpload` su campione, listing dei 10k file, settaggi vfs-cache).
Se il medium degrada, il fallback è un supporto world diverso, non il ritorno a
substrato.

## Da valutare (i2→i3, non qui)

1. Il test «significato senza l'artefatto» va canonizzato in `world.md` come
   criterio operativo per `world` vs i1/substrato?
2. Il secondo discriminante «chi scrive» è parte dello stesso criterio o una
   regola distinta? Ipotesi: contenuti scritti da attori del mondo tendono a
   essere membrana; contenuti scritti dall'artefatto per sé stesso tendono a
   essere substrato.
3. La materializzazione `world` deve ammettere esplicitamente più superfici
   fisiche per un adottante (es. `client/` Syncthing + Drive foto), purché il
   README/map dell'adottante le dichiarino?

## Stato locale del segnale

In `bi` il task «Migrazione substrato runtime fuori dalla root» è stato
aggiornato: `foto/` migra alla membrana `world` via mount Drive condiviso, non a
`i1/foto`; README e `map.md` dichiarano la seconda superficie world; il primo
passo resta la prova I/O prima del flip.
