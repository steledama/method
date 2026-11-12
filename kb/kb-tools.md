---
stato: maturo
---

# KB tools

Gli strumenti KB rendono deterministici i controlli ripetitivi: parsing dei
link, backlink, catalogo, frontmatter, formato e copertura. Non decidono quali
concetti siano veri o utili. Lo script produce evidenze; custode e agente le
interpretano e modificano la conoscenza.

`o3/kb_tools.py` è il nucleo usato dalla skill `kb`. Vive nel canone e si
lancia da lì sul repo da verificare, `python3 method/../o3/kb_tools.py
--root . audit`: una copia nell'adottante smette di ricevere il nucleo senza
che nessuno lo veda. I comandi:

- `audit [--format markdown|json]`: report strutturale completo; i link sono
  verificati anche fuori dall'inventario dei nodi — register dei poli, bussola,
  regole e indici delle collezioni — perché un riferimento a un filo rimosso
  resterebbe altrimenti invisibile;
- `backlinks NODE`, `orphans`: topologia della rete;
- `readme`, `migration`: catalogo e convenzioni documentali;
- `facets`: attributi di dominio dichiarati nel frontmatter;
- `tasks`: frontmatter dei task aperti, per il contratto tra plan, indice e file
  della collezione;
- `terms`: candidati terminologici da valutare, non nuovi nodi automatici;
- `inventory`, `coverage`: inventario e copertura per progetti con codice.

I controlli dei collegamenti ignorano gli esempi nei blocchi fenced con
backtick o tilde, anche non chiusi; catalogo, cluster e backlink usano lo
stesso filtro. Il riconoscimento dei link resta euristico: questo filtro
non interpreta inline code, blocchi indentati o fence dentro contenitori
Markdown (liste e citazioni), né sostituisce un parser Markdown completo.

Il nucleo comune resta indipendente dal dominio, e il dominio non lo copia.
L'adottante dichiara ciò che è suo in due file opzionali del proprio repo:

- `o3/kb_tools.toml`, il profilo: cartelle dei documenti, catalogo,
  estensioni ed esclusioni del codice, facet locali;
- `o3/kb_domain.py`, i controlli che sono codice, come `facts` o `fidelity`
  quando dispone di fonti primarie leggibili. Il modulo aggiunge
  sottocomandi, porta le proprie violazioni nel report di `audit` e può
  sostituire `inventory` e `coverage`, che dipendono dal linguaggio del
  repo.

Gli altri comandi base non si sostituiscono, così skill e audit comparativi
usano la stessa interfaccia in ogni repo.

`o3/kb_profile.py --root <repo>`, lanciato allo stesso modo dal canone, produce il profilo quantitativo comune:
manifest dei nodi locali con impronte, righe, distribuzione delle dimensioni e
maturità dichiarata. Esclude catalogo, file nascosti e symlink; enumera anche
nodi non catalogati. Il parametro `--states` adatta il dominio chiuso degli
stati ammessi. Segnala frontmatter assente, stato duplicato o non valido; non è
un validatore YAML generale. Il manifest identifica ciò che va letto, senza
attestare che la lettura sia avvenuta.

`o3/skill_tools.py` è il guardiano quantitativo delle skill, indipendente
dall'harness come gli altri strumenti: `audit` misura dimensioni, crescita e
quota di rimandi, confronta i comandi scritti con i permessi di sessione e
giro, trova i divieti scritti con o senza deny e le chiamate fra skill,
prova gli esempi di trailer `Prossimo:` di skill e prompt del giro contro
il gate di `commit_gate.py`, segnala la prosa che lega il motivo di una
conferma al trailer invece che al corpo, e misura la divergenza delle copie dal canone.
Comandi, divieti, chiamate e trailer si leggono anche nei file accanto a
`SKILL.md`: un ramo estratto porta procedura, e fuori dal controllo la
misura migliorerebbe nascondendo i gesti. Comandi e divieti si censiscono anche in
`CLAUDE.md`, `AGENTS.md` e nel prompt del giro, e un divieto di sessione
retto solo dai deny del giro si segnala come lacuna. Le chiamate fra skill si
cercano con un verbo nella riga o nella precedente; le menzioni senza verbo
escono come candidati, perché un rinvio imperativo può non averne. `classifica` ordina le skill di
`method` e degli adottanti. Non dipende dal dominio, quindi un adottante lo
lancia dal checkout del canone invece di copiarlo. Il giudizio su atomicità e
composizione resta alla revisione (`skill-composition`).

Ogni misura dichiara oggetto, denominatore ed esclusioni. Il profilo del corpus,
la copertura del codice e la verifica delle fonti sono oggetti diversi; i
conteggi dei fork si confrontano solo a perimetro equivalente. I controlli di
rete e catalogo restano nel backend locale, con i suoi limiti di parsing; una
menzione trovata non dimostra sufficienza documentale.

La documentazione segue una sola gerarchia: README rende lo strumento
rintracciabile, CLAUDE indica quando usarlo, i nodi ne definiscono capacità e
limiti, mentre gli indici delle collezioni registrano prescrizioni ed esecutori
concreti. Per questo `coverage` considera README, KB e indici di collezione:
richiedere un nodo per ogni modulo interno trasformerebbe la KB in un inventario
della macchina già custodito da `o3/prescriptions.md`. Ripetere ovunque
procedure, opzioni e file crea drift.

Regole d'uso:

- preferire lo script versionato a parser improvvisati in sessione;
- mantenere separati audit strutturale e revisione semantica;
- confrontare i fatti con fonti primarie, anche documentali, senza usare copie
  della sintesi come conferma indipendente;
- conservare nei fili solo il cambiamento di giudizio prodotto dall'audit, non
  il report rigenerabile;
- tenere le estensioni locali, nel modulo di dominio, e quando possibile
  prive di dipendenze esterne.

Lo scope intenzionale è la struttura della KB e dei documenti supportati. La
qualità delle decisioni, dei router e delle prescrizioni resta una valutazione
qualitativa (`cognitive-fidelity`).

Connessioni:

- [knowledge-base](knowledge-base.md)
- [node](node.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [source-of-truth](source-of-truth.md)
- [method-observatory](method-observatory.md)
- [skill-composition](skill-composition.md)
