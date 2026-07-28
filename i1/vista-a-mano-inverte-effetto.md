---
ciclo: runtime
---

# Segnale: una vista derivata mantenuta a mano può invertire l'effetto che cerca

Data: 2026-07-28 · Fonte: custode, su esperienza `salute` (il deck del quadro
corporeo, 273 righe di HTML scritte a mano, reso generato da `i2/` e dalla
sezione `## Scadenze` di `o1/plan.md`)

## Il segnale

Il 12 luglio il commit `1c2b939` di `salute` ha assorbito l'esito di una visita
medica: sei file di `i2/` e `o1/plan.md` aggiornati, un esame ritirato su
indicazione del medico, un'area ridimensionata da gialla `~35` a verde `~25`. Il
deck — la superficie viscerale dello **stesso** quadro, allora HTML scritto a
mano — non era tra i file toccati: era fermo al commit `ea73d72` del 8 luglio, e
lo è rimasto per sedici giorni, fino a questa sessione.

In quei sedici giorni il deck non era genericamente incompleto. Continuava a
mostrare l'area in banda gialla e a elencare tra le prossime decisioni
«chiedere» proprio l'esame che il medico aveva sconsigliato: **invitava
all'azione che la fonte aveva appena ritirato**. Misurato sul deck vecchio: una
decisione su cinque non esisteva più in nessuna fonte, una seconda ne
contraddiceva il contenuto, e quattro scadenze reali del plan non comparivano
affatto.

Osservazioni emerse **facendo** la conversione a vista generata, non prevedibili
prima:

- **il drift ha colpito il fatto più fresco, non il più vecchio.** L'unico
  aggiornamento sostanziale del mese è esattamente ciò che la vista non ha
  recepito. Una vista a mano non degrada in modo uniforme: diverge dove la
  fonte si muove, cioè dove conta;
- **nessun controllo esistente lo vedeva.** L'audit strutturale del repo
  riportava e riporta 0 link rotti e 0 problemi su 197 nodi mentre il deck
  contraddiceva la propria fonte. Gli audit strutturali non attraversano il
  confine tra una vista e ciò da cui deriva;
- **il filo `i3/` registrava metà del fatto.** Diceva che il quadro aveva
  assorbito la decisione medica — vero della fonte, falso della superficie che
  la rende. Il filo non aveva un posto dove distinguere le due;
- **la difformità di una fonte non era rumore ma un secondo significato.** Il
  parser è inciampato su un file-area su otto: non dichiarava la coppia
  `Prossima azione`/`Entro` come gli altri, ma una `Riapertura`. La tentazione
  era normalizzare la fonte alla forma maggioritaria; la difformità però
  distingueva un'area _dormiente_, che aspetta un trigger, da una _attiva_, che
  aspetta una data — la stessa distinzione che `plan` fa tra una scadenza
  (orologio del mondo) e una pausa con condizione di risveglio. Appiattirla
  avrebbe distrutto informazione.

Risoluzione locale adottata (fatto, non prescrizione): il deck si genera da
`i2/` e dal plan; il generatore legge le fonti come un contratto e **esce con
errore** se banda o score dichiarati nella tabella del quadro divergono dal
file-area, o se un file-area non è indicizzato nella tabella. Verificato
iniettando la discordanza reale: la build rompe con il nome dell'area e i due
valori a confronto. Il contratto ammette entrambe le forme dell'azione aperta
invece di imporne una.

## Domande per i2 (nessun verdetto qui, i1 è valenza-neutro)

- il runbook [view](../kb/view.md) dice come una vista derivata si costruisce e
  si pubblica; dice anche che deve **fallire** quando le fonti divergono?
  «Derivata» senza «verificata» sembra una mezza garanzia, ma il campione è uno;
- una vista mantenuta a mano è un caso particolare della seconda
  rappresentazione di [constraint](../kb/constraint.md) — un fatto che vive in
  due posti — o è una specie a sé, perché la seconda rappresentazione è scritta
  in un altro linguaggio e non si legge mai accanto alla prima? Nel caso del
  plan le due copie stanno nello stesso file e si vedono; qui no;
- il costo del drift non è simmetrico tra domini. Una vista stale su un dominio
  sanitario invita ad azioni ritirate da un medico; su altri domini è rumore. Il
  metodo distingue le viste dove la deriva è innocua da quelle dove è dannosa, o
  tratta tutte le viste allo stesso modo?
- «prima di appiattire una difformità della fonte, chiedersi se è un secondo
  significato» è lo stesso corollario di «migrare è fondere, non cancellare»
  (recepito da `dc16aa2..6133ace`) applicato a un altro asse — schema contro
  fonte, invece che copia contro copia? Se sì, la regola appartiene a un posto
  solo o a entrambi;
- serve una classe di controllo «la vista regge il contratto» accanto agli audit
  strutturali, oppure un generatore che rompe la build **è** già esattamente
  quel controllo, e la domanda giusta è quali viste non sono ancora generate?
- un filo `i3/` che valuta un artefatto composto (fonte + superficie che la
  rende) ha bisogno di dichiarare **quale dei due** sta misurando? Qui il
  verdetto era vero della fonte e falso della vista, e nulla nella forma del
  filo obbligava a distinguerli.
