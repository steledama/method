---
description: Audit strutturale o revisione semantica qualitativa della knowledge base.
user-invocable: true
---

# kb

Usa `/kb [audit|review]` dalla root del repository. Il default è `audit`.
Questa è la copia canonica: gli adottanti la forkano e adattano strumenti e
fonti primarie al proprio dominio.

- `audit` fotografa integrità strutturale e drift deterministico senza
  correggere;
- `review` esegue prima `audit`, poi valuta funzione, verità, attualità,
  atomicità, ridondanza, fonti di verità e qualità del catalogo.

La diagnosi e l'intervento restano atti separati. Non modificare la KB durante
la review salvo autorizzazione esplicita successiva del custode.

## Audit

Esegui:

```bash
python3 o3/kb_tools.py audit
python3 o3/kb_tools.py inventory
python3 o3/kb_tools.py coverage
python3 o3/kb_tools.py facets
```

Classifica errori deterministici, warning utili e falsi positivi. I candidati
terminologici non autorizzano nuovi nodi: richiedono giudizio sulla funzione.

## Review semantica

Leggi integralmente:

- `kb/cognitive-fidelity.md`;
- `kb/kb-content-typology.md`;
- `kb/node.md`;
- `kb/source-of-truth.md`.

Leggi README, CLAUDE, `world.md`, catalogo e tutti i nodi della KB. Non
campionare: una revisione profonda deve vedere sovrapposizioni e contraddizioni
tra nodi lontani. Usa dimensione, titoli e ultima modifica Git soltanto per
orientare l'attenzione; una data recente non prova freschezza semantica.

Nel repository `method` verifica anche che ogni nodo resti metodologico e
portabile, applicabile ad almeno due progetti, invece di trattenere dettagli di
un singolo adottante.

### 1. Funzione documentale

Assegna a ogni nodo una funzione dominante: orientamento, modello del dominio,
modello della macchina, norma, runbook, reference o router. Verifica che:

- README orienti senza diventare catalogo o manuale;
- CLAUDE contenga regole d'azione, non conoscenza di dominio;
- il catalogo descriva la funzione dei nodi e non replichi il README;
- ogni nodo giustifichi il proprio peso e non svolga più funzioni incompatibili.

La tipologia descrive ciò che il contenuto denota; la funzione documentale
descrive come viene usato. Non confondere i due assi.

### 2. Presente, storia e lavoro futuro

Per ogni passaggio chiedi se cambia una decisione o un comportamento corrente.

- conserva fatti attuali, invarianti, lezioni operative e assunzioni che
  imporrebbero una revisione;
- lascia a Git cronologia, date, vecchi nomi, commit, migrazioni concluse ed
  esempi superati;
- lascia a `i3/` i verdetti correnti e a `o1/`/`o2/` il lavoro futuro;
- non eliminare misure runtime o conoscenza empirica non ricostruibile da Git
  se continua a influenzare diagnosi o decisioni.

Una alternativa scartata merita spazio solo se impedisce di ripetere un errore;
conservala come vincolo e condizione di revisione, non come cronaca.

### 3. Verità e volatilità

Individua i fatti che possono cambiare e la loro fonte primaria. La
documentazione non valida altra documentazione.

- codice, filesystem, dati strutturati e runtime precedono le copie narrative;
- un fatto volatile ha una sola fonte documentale e gli altri punti vi
  rimandano;
- distingui default dichiarato, assetto operativo di riferimento e stato
  realmente osservato;
- cerca anche path in backtick o testo semplice: possono sfuggire al link
  checker Markdown.

### 4. Atomicità e ridondanza

Valuta la responsabilità, non la sola somiglianza lessicale.

- fondi nodi quando uno non conserva una funzione autonoma;
- dividi soltanto quando emergono responsabilità usate separatamente;
- trasforma i panoramici in router se duplicano comandi e troubleshooting dei
  nodi specialistici;
- separa modello e runbook quando hanno ritmi di cambiamento diversi;
- non creare un nodo per un termine frequente già coperto dal lessico del
  dominio.

### 5. Chiarezza e accessibilità

Controlla titolo, apertura, ordine delle sezioni, esempi, lessico e sintesi.
Verifica che una persona possa scegliere il nodo giusto dal catalogo e che il
nodo esponga presto scopo, confine e fonte di verità. Segnala tabelle o
inventari che aumentano manutenzione senza comprimere davvero informazione.

### 6. Test di potatura

Classifica ogni nodo `mantieni`, `rifinisci`, `fondi`, `dividi` o `elimina`.
Un contenuto giustifica il proprio peso se almeno una condizione è vera:

- cambia una decisione o un comportamento;
- distingue casi altrimenti confondibili;
- comprime più regole in una spiegazione più semplice;
- conserva una fonte o evidenza non ricostruibile altrove;
- è necessario a una parte effettivamente usata del metodo o dominio.

Non fissare una percentuale di riduzione: le righe eliminate sono un esito, non
un obiettivo. Una KB breve ma priva di fatti decisionali è peggiore di una KB
più lunga e fedele.

## Output della diagnosi

Concludi con:

1. verdetto complessivo separando salute strutturale e semantica;
2. contraddizioni o fatti stale con file e riga;
3. candidati prioritizzati a potatura, fusione, divisione o riscrittura;
4. valutazione del catalogo e dei punti d'ingresso;
5. nodi già ben riusciti da non destabilizzare;
6. ordine d'intervento proposto e rischi di perdita informativa;
7. domanda esplicita al custode se vuole applicare le correzioni.

## Intervento autorizzato

Se il custode autorizza una fase successiva:

1. correggi prima contraddizioni, riferimenti morti e fonti duplicate;
2. riduci storia e stato transitorio conservando invarianti e lezioni;
3. semplifica nodi sovraccarichi e sovrapposizioni;
4. aggiorna il catalogo dopo che i confini si sono stabilizzati;
5. formatta i file e riesegui tutti i comandi di `audit` più i check locali;
6. riporta conteggi prima/dopo senza presentarli come misura della qualità.

Non archiviare il report: è una diagnosi i1 rigenerabile. Se cambia un verdetto
aperto, il gate `/commit` valuta l'aggiornamento in place del filo `i3/`.
