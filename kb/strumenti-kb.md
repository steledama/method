---
data: 2026-05-09
stato: maturo
---

# Strumenti KB

Gli strumenti KB sono script versionati che rendono deterministica la manutenzione della knowledge base. Non sostituiscono il giudizio dell'LLM o dell'utente: spostano però la parte fragile e ripetitiva del lavoro — parsing dei link markdown, conteggi dei backlink, verifica del README, controllo del formato dei nodi — dentro codice stabile, testabile e riusabile.

Questa divisione del lavoro riduce gli errori di sessione. L'LLM resta utile per interpretare i risultati, decidere quali problemi siano reali, proporre connessioni semantiche e scrivere i nodi; lo script invece garantisce che i numeri strutturali siano calcolati sempre nello stesso modo. La skill audit-kb usa `scripts/kb_tools.py` come backend proprio per evitare di ricostruire parser e regex a ogni audit.

Comandi principali:

- `python3 scripts/kb_tools.py audit --format markdown`: genera il report completo con segnali a tre livelli (errore / avviso / info) in formato appendibile a log.md
- `python3 scripts/kb_tools.py audit --format json`: genera lo stesso audit in formato strutturato per altri strumenti
- `python3 scripts/kb_tools.py audit --format markdown --append-log`: appende direttamente il report a log.md
- `python3 scripts/kb_tools.py backlinks nodo.md`: mostra link in uscita e backlink di un nodo
- `python3 scripts/kb_tools.py orphans`: elenca i nodi senza backlink
- `python3 scripts/kb_tools.py readme`: verifica copertura e link del catalogo README
- `python3 scripts/kb_tools.py migration`: verifica frontmatter, footer Connessioni e link inline residui
- `python3 scripts/kb_tools.py terms --limit 20`: propone candidati grezzi a nuovi nodi da termini ricorrenti
- `python3 scripts/kb_tools.py inventory`: inventario delle entità principali del progetto (host, profili, moduli o equivalenti per dominio)
- `python3 scripts/kb_tools.py facts`: confronto tra fatti documentati ad alta fiducia e fonti tecniche o documentali del progetto
- `python3 scripts/kb_tools.py coverage`: segnali su aree principali potenzialmente scoperte dalla documentazione
- `python3 scripts/kb_tools.py fidelity`: aggregatore anti-drift che combina fatti verificabili e warning di copertura

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

Connessioni:

- [metodo-kb](metodo-kb.md)
- [knowledge-base](knowledge-base.md)
- [pattern-karpathy](pattern-karpathy.md)
- [struttura-progetto](struttura-progetto.md)
- [connessione](connessione.md)
- [nodo](nodo.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
