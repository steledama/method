# Profilo KB — method

La KB canonica da leggere è `kb/`. Il corpus locale è `kb/**/*.md`,
escluso `kb/kb.md`; non seguire symlink verso altri corpus.

## Audit e perimetri

```bash
python3 o3/kb_profile.py --root .
python3 o3/kb_tools.py audit
python3 o3/kb_tools.py inventory
python3 o3/kb_tools.py coverage
python3 o3/kb_tools.py facets
```

`kb_profile.py` misura i nodi locali, valida gli stati di maturità e produce
il manifest per la lettura; non verifica la verità dei contenuti.
`audit` controlla struttura, catalogo, rete e link nei documenti supportati.
`inventory` censisce il codice; `coverage` cerca menzioni in README, KB e
indici di collezione, senza dimostrare sufficienza della documentazione.
`facets` verifica gli attributi dichiarati. Interpreta i falsi positivi del
parser, soprattutto nei template; non confondere presenza di frontmatter con
validità dei suoi valori.

## Review di dominio

Il dominio è il metodo stesso: concetti, norme e fondamenti teorici.
Verifica che ogni nodo sia metodologico e applicabile ad almeno due progetti.
Le fotografie degli adottanti e i dettagli di un singolo dominio non diventano
regole universali per il solo fatto di essere osservati qui.

Per attribuzioni teoriche risali alle edizioni e alle superfici dichiarate in
`world.md`: distingui fonte letta, citazione mediata e provenienza senza testo
consultabile. Non attribuire all'autore la traduzione operativa del metodo.
Le norme locali sono scelte del custode, verificabili contro i contratti del
metodo; il codice degli esecutori mostra la loro implementazione, non prova
la validità della teoria.

Prove di navigazione possibili, da scegliere secondo il lavoro reale:

- dove collocare una nuova informazione, distinguendo conoscenza, segnale,
  interpretazione, verdetto e lavoro futuro;
- come distinguere un adattamento locale da un principio da generalizzare;
- da quale fonte deriva una distinzione fondativa e quale parte è elaborazione
  del metodo.

Controlla contraddizioni fra nodi e istruzioni delle skill che li attuano.
Una procedura operativa della review vive nella skill; i criteri durevoli nei
nodi; gli esecutori sono registrati in `o3/prescriptions.md`.

## Dopo un intervento

Formatta i Markdown modificati con `prettier --write <file...>` e i Python
con `ruff format <file...>`. Riesegui i comandi di audit sopra; per modifiche
al profiler esegui `python3 -m unittest discover -s tests -p 'test_kb_profile.py'`.
Se cambiano le sorgenti delle viste, esegui `bash o3/build-presentation.sh`
e `bash o3/build-system-image.sh`; controlla il diff delle viste derivate.
