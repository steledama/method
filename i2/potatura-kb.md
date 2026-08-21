---
ciclo: dev
---

# Potatura minimalista della KB

Prima fotografia della revisione semantica richiesta dal custode. L'audit
meccanico non rileva il problema: una rete può essere integra e tuttavia
richiedere troppo lessico per essere compresa.

## Criterio

Un concetto merita di restare se almeno una di queste condizioni è vera:

- cambia una decisione o un comportamento;
- distingue casi che altrimenti verrebbero confusi;
- comprime più regole operative in una spiegazione più semplice;
- è necessario a una fonte teorica che regge una parte effettivamente usata
  del metodo.

Se non supera il test, va eliminato o fuso. L'eleganza esplicativa, da sola,
non basta.

## Primo scaglione

Le metafore `atrio`, `ali` e `stanze` descrivevano root, componenti e directory
senza produrre una differenza operativa. Erano penetrate in 23 file Markdown:
`atrio` compariva 53 volte; `ali` strutturale 7 volte. La loro rimozione non
cambia nomi, collocazione, strumenti o bootstrap.

`project-structure.md` concentrava struttura corrente, storia della migrazione,
fotografie degli adottanti, esempi e razionali presenti altrove. Il primo
scaglione lo riduce a specifica corrente; Git conserva la storia e
l'osservatorio le fotografie.

## Secondo scaglione

La revisione dei componenti documentali ha distinto le funzioni reali:

- `readme` resta perché definisce l'orientamento al dominio;
- `claude` resta perché definisce ciò che l'agente deve sapere prima di agire;
- `project-structure` resta come specifica di collocazione e convenzioni;
- `agents` è assorbito in `claude` e `project-structure`: documentava un
  wrapper di poche righe senza un concetto autonomo;
- `index` è assorbito dal catalogo vivo `kb/kb.md`, da `node` e da `kb-tools`:
  non aggiungeva un comportamento oltre «indicizza tutti i nodi».

Quantità **misurate** prima/dopo lo scaglione: cluster da 3.171 a 1.088 parole;
KB da 52.159 a 50.014 parole; nodi da 48 a 46. Dal punto di partenza della
potatura la KB è scesa da 55.861 a 50.014 parole.

## Terzo scaglione

I tre nodi sulla manutenzione restano distinti perché rispondono a domande
diverse:

- `knowledge-base`: che cosa deve sopravvivere alle sessioni e quale funzione
  svolge;
- `kb-tools`: quali controlli ripetitivi sono affidati a codice deterministico;
- `cognitive-fidelity`: come verificare ciò che formato e link non possono
  decidere.

La revisione ha rimosso cornice teorica già trattata altrove, fotografie degli
adottanti, esempi storici, procedure di installazione e ripetizioni reciproche.
È rimasta una sola descrizione per identità, interfaccia degli strumenti e
checklist qualitativa. La skill `kb` è stata inoltre corretta perché puntava al
nome dismesso `fedelta-cognitiva.md`.

Quantità **misurate** prima/dopo lo scaglione: cluster da 3.675 a 796 parole;
KB da 50.014 a 47.129 parole; nodi invariati a 46. Dal punto di partenza della
potatura la KB è scesa da 55.861 a 47.129 parole.

## Quarto scaglione

I quattro nodi sul lavoro e sugli agenti conservano responsabilità autonome:

- `plan`: ordine, obiettivi e dipendenze della coda;
- `tasks`: specifica temporanea del lavoro sostanziale;
- `verdict`: giudizio corrente sulle tensioni rispetto ai goal;
- `skill`: capacità ricorrente e invocabile, distinta dal task consumabile.

Sono state eliminate genealogie delle forme, cronache degli adottanti, esempi
estesi e procedure già prescritte nelle `SKILL.md`. Restano lo schema canonico
del plan, il frontmatter dei task, i vincoli epistemici del verdetto e i criteri
che distinguono skill autonome, scope e cadenze.

Quantità **misurate** prima/dopo lo scaglione: cluster da 7.840 a 1.116 parole;
KB da 47.129 a 40.371 parole; nodi invariati a 46. Dal punto di partenza della
potatura la KB è scesa da 55.861 a 40.371 parole.

## Quinto scaglione

L'impianto teorico conserva un nodo per ciascuna funzione: modello del ciclo,
protocollo della matrice, livelli di elaborazione, due archi, sei atti e
meta-ciclo di sviluppo. Nessuna fusione avrebbe ridotto il numero di concetti
senza confondere scala, direzione o funzione.

Sono state rimosse esegesi estese delle fonti, dimostrazioni ripetute,
fotografie datate degli adottanti, casi storici e prescrizioni già presenti
nelle skill. `action-cycle-matrix` non incorpora più risultati destinati a
invecchiare: conserva il protocollo falsificabile e demanda le fotografie
all'osservatorio.

Quantità **misurate** prima/dopo lo scaglione: cluster da 11.935 a 2.054
parole; KB da 40.371 a 30.371 parole dopo l'aggiornamento del catalogo; nodi
invariati a 46.

## Esito complessivo

La potatura è conclusa. La KB passa da 55.861 a 30.371 parole e da 48 a 46
nodi. Due nodi privi di funzione autonoma sono stati assorbiti; tutti i nodi
residui hanno superato il criterio. La riduzione è di 25.490 parole, circa il
46% del punto di partenza, senza cambiare struttura delle collezioni, strumenti
o contratti operativi.
