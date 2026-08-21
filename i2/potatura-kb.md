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

## Scaglioni successivi

1. componenti documentali: `readme`, `claude`, `agents`, `index` e
   `project-structure`;
2. manutenzione della KB: `knowledge-base`, `kb-tools` e
   `cognitive-fidelity`;
3. lavoro e agenti: `plan`, `tasks`, `verdict` e `skill`;
4. impianto teorico: `action-cycle`, `action-cycle-matrix`,
   `processing-layers`, `input`, `output`, sei nodi-stadio e
   `development-meta-cycle`.

Ogni scaglione deve dichiarare parole e nodi prima/dopo, cosa è stato fuso o
eliminato e quale comportamento resta invariato.
