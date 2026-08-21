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

## Scaglioni successivi

1. lavoro e agenti: `plan`, `tasks`, `verdict` e `skill`;
2. impianto teorico: `action-cycle`, `action-cycle-matrix`,
   `processing-layers`, `input`, `output`, sei nodi-stadio e
   `development-meta-cycle`.

Ogni scaglione deve dichiarare parole e nodi prima/dopo, cosa è stato fuso o
eliminato e quale comportamento resta invariato.
