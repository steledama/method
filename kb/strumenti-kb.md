---
data: 2026-05-24
stato: maturo
---

# Strumenti KB

Gli strumenti KB sono script versionati che rendono deterministica la manutenzione della knowledge base. Non sostituiscono il giudizio dell'LLM o dell'utente: spostano però la parte fragile e ripetitiva del lavoro — parsing dei link markdown, conteggi dei backlink, verifica del README, controllo del formato dei nodi — dentro codice stabile, testabile e riusabile.

Questa divisione del lavoro riduce gli errori di sessione. L'LLM resta utile per interpretare i risultati, decidere quali problemi siano reali, proporre connessioni semantiche e scrivere i nodi; lo script invece garantisce che i numeri strutturali siano calcolati sempre nello stesso modo. La skill audit-kb usa `scripts/kb_tools.py` come backend proprio per evitare di ricostruire parser e regex a ogni audit.

Il repo metodo contiene la versione portabile di `scripts/kb_tools.py`. Questa versione distingue due livelli:

- strumenti base per qualunque KB: audit strutturale, backlink, orfani, copertura README, migrazione formato e candidati terminologici
- strumenti generici per progetti code-based: inventario dei file codice e copertura codice → nodi KB

I controlli avanzati che dipendono dal dominio restano locali. In un progetto NixOS possono confrontare host, profili e moduli con `flake.nix`; in un progetto BI possono misurare la documentazione degli script applicativi; in un progetto finanziario possono confrontare nodi e JSON autoritativi. Il metodo fornisce lo scheletro, i progetti aggiungono le fonti di verità.

Dal punto di vista dell'osservatorio metodo, gli strumenti hanno anche una funzione comparativa: rendono possibile misurare periodicamente lo stato dei progetti adottanti con una superficie comune e distinguere ciò che è salute strutturale della KB da ciò che è fedeltà specifica al dominio.

## Esposizione degli strumenti

Per rendere l'LLM consapevole degli strumenti a disposizione senza creare
duplicazione, ogni progetto dovrebbe esporli su tre livelli:

- README.md: elenco brevissimo degli strumenti e link ai nodi, per discovery e
  orientamento iniziale
- CLAUDE.md: istruzioni operative, cioè quale strumento usare per quale intento,
  comandi minimi e condizioni di escalation
- nodi KB: reference stabile del workflow, varianti, limiti, troubleshooting e
  dettagli che non devono appesantire i file root

La regola pratica è: README orienta, CLAUDE istruisce, KB approfondisce. Quando
un comando o una procedura compare in più livelli con lo stesso dettaglio, il
progetto sta creando una futura fonte di drift. Quando invece uno strumento è
documentato solo in un nodo ma non compare nel README o in CLAUDE, l'agente può
non scoprirlo o scegliere un workflow peggiore.

Comandi principali:

- `python3 scripts/kb_tools.py audit --format markdown`: genera il report completo con segnali a tre livelli (errore / avviso / info) in formato appendibile a log.md
- `python3 scripts/kb_tools.py audit --format json`: genera lo stesso audit in formato strutturato per altri strumenti
- `python3 scripts/kb_tools.py audit --format markdown --append-log`: appende direttamente il report a log.md
- `python3 scripts/kb_tools.py backlinks nodo.md`: mostra link in uscita e backlink di un nodo
- `python3 scripts/kb_tools.py orphans`: elenca i nodi senza backlink
- `python3 scripts/kb_tools.py readme`: verifica copertura e link del catalogo README
- `python3 scripts/kb_tools.py migration`: verifica frontmatter, footer Connessioni e link inline residui
- `python3 scripts/kb_tools.py terms --limit 20`: propone candidati grezzi a nuovi nodi da termini ricorrenti
- `python3 scripts/kb_tools.py inventory`: nella versione portabile inventario generico dei file codice; nelle versioni locali può diventare inventario delle entità principali del progetto
- `python3 scripts/kb_tools.py coverage`: nella versione portabile copertura generica codice → nodi KB; nelle versioni locali può diventare copertura documentale specifica
- `python3 scripts/kb_tools.py facts`: comando locale opzionale per confrontare fatti documentati ad alta fiducia e fonti tecniche o documentali del progetto
- `python3 scripts/kb_tools.py fidelity`: comando locale opzionale anti-drift che combina fatti verificabili, warning di copertura e checklist semantica

Limite di scope: `kb_tools.py` audita la salute strutturale di `kb/` e `todo/`. Non copre lo strato output, che vive fuori da `kb/` e ha nomi locali per ogni progetto. La valutazione dello strato output è qualitativa: si usa la checklist di Norman (visibilità, feedback, mapping, constraint) in una sessione di revisione, non uno script automatico. Questo è intenzionale — la domanda chiave è se l'utente agisce, non se il file ha link validi.

Regole d'uso:

- gli script producono dati strutturali; le decisioni restano interpretative
- i candidati terminologici non sono automaticamente nuovi nodi: vanno filtrati semanticamente
- i controlli anti-drift devono partire da pochi fatti affidabili e crescere solo
  quando una fonte di verità è chiara
- `audit` misura la salute strutturale della rete; `fidelity` misura segnali di
  aderenza al dominio e non sostituisce la checklist semantica
- l'audit completo non va appendito integralmente a log.md (memoria interpretativa, non archivio di output): quando un audit produce un'osservazione significativa, registrarne solo una sintesi sotto forma di voce log; l'output esteso resta ricostruibile su qualunque commit storico via `git checkout <hash> && python3 scripts/kb_tools.py audit`. Le correzioni emerse dall'audit vanno trattate come passaggio separato.
- quando una skill può usare uno script versionato, deve preferirlo a regex improvvisate nella sessione
- gli script devono restare senza dipendenze esterne quando possibile, così funzionano su qualunque host con Python 3
- le estensioni locali devono preservare i comandi base, così skill e agenti possono contare su una superficie comune tra repository
- i controlli di frontmatter devono distinguere i tipi documentali: obbligatorio nei nodi `kb/`, obbligatorio nei task `todo/`, non richiesto nei file root

Skill:

- audit-kb: usa kb_tools.py, interpreta il report e non corregge automaticamente senza richiesta
- commit: applica formatter, controlla diff e crea commit secondo convenzioni locali
- skill locali: descrivono workflow specifici del dominio, ma riusano strumenti versionati quando possibile
- vecchi comandi: da evitare se la stessa funzione può essere espressa come skill o regola di bootstrap

Wrapper Codex:

- .codex/skills contiene wrapper leggeri, non copie delle skill
- ogni wrapper rimanda alla skill canonica in .claude/skills
- i wrapper servono solo per discovery da parte di Codex
- se una skill viene rimossa o fusa, va rimosso anche il wrapper corrispondente

Requisiti per un nuovo progetto:

- copiare o creare scripts/kb_tools.py se serve audit strutturale
- creare .claude/skills/audit-kb con istruzioni locali e backend script
- creare .claude/skills/commit se il progetto ha convenzioni di commit
- creare wrapper .codex/skills solo se il progetto deve supportare Codex
- aggiungere formatter disponibili in CLAUDE.md, senza inventare strumenti non installati

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                                                                                                  | Confronto con il metodo                                                                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `nixos`    | `kb_tools.py` espone comandi base più `inventory`, `facts`, `coverage`, `fidelity`; `scripts/check.sh` aggrega formatter, audit, fact check e fidelity.             | È il laboratorio più avanzato per anti-drift code-based: la fonte dichiarativa Nix rende verificabili host, profili, moduli e copertura.                     |
| `bi`       | `kb_tools.py` espone comandi base e aggiunge copertura documentale degli script (`script_missing_docs`, `script_docs_count`). Graphify è strumento locale separato. | Buona superficie strutturale; la fedeltà BI deve ancora fondarsi su fonti primarie applicative, non su documentazione interna.                               |
| `economia` | `kb_tools.py` espone comandi base più `facts` sulla mappa; l'audit produce segnali a livelli errore/avviso/info.                                                    | Adattamento utile a un dominio documentale: i facts verificano presenza e coerenza delle entità, ma non sostituiscono controllo umano su importi e scadenze. |
| `salute`   | `kb_tools.py` espone la superficie base (`audit`, `backlinks`, `orphans`, `readme`, `migration`, `terms`).                                                          | Adeguato a una KB concettuale: per ora la priorità è salute strutturale e filing back, non inventario tecnico.                                               |

La fotografia strutturale quantitativa per repo (nodi, link, esiti audit, file segnalati) vive nel nodo `confronto-progetti-adottanti`, fonte unica per i dati cross-repo: qui resta solo il confronto qualitativo sulla superficie degli strumenti, che cambia di rado.

Il confronto chiarisce il confine dello strumento portabile. La superficie base deve restare comune; i controlli `facts` e `fidelity` devono essere locali finché il dominio decide quali fatti sono verificabili e quali fonti sono primarie. Il repo metodo può però produrre un report cross-repo che invoca gli strumenti locali e normalizza gli esiti.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [knowledge-base](knowledge-base.md)
- [pattern-karpathy](pattern-karpathy.md)
- [struttura-progetto](struttura-progetto.md)
- [osservatorio-metodo](osservatorio-metodo.md)
- [connessione](connessione.md)
- [nodo](nodo.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
- [output](output.md)
- [ciclo-azione](ciclo-azione.md)
