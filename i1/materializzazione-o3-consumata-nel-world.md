---
ciclo: runtime
---

# Segnale: una prescrizione o3 consumata può lasciare una materializzazione nel Mondo

Data: 2026-08-16 · Fonte: salute — PDF del canovaccio per l'incontro con il
medico del 2 luglio 2026

## Il segnale

In `salute` un task aveva predisposto il canovaccio per un incontro medico. La
specifica versionata in `o2/` è stata rimossa quando l'incontro e il ritorno del
suo esito hanno chiuso il task; il PDF operativo, però, era rimasto nella
superficie non versionata `gdrive/varie/`. È stato individuato e cancellato solo
durante una revisione successiva.

Il contenuto utile non è andato perso: decisioni ed esiti dell'incontro erano
già risaliti nel diario, nella storia clinica, nel quadro corporeo e nelle
scadenze. Il PDF non documentava l'atto compiuto; era una copia di consegna
della prescrizione, priva di significato operativo autonomo dopo l'incontro.

## L'attrito osservato

`perform` stabilisce già che una prescrizione o3 consumata si elimina quando
l'atto è compiuto e l'esito è risalito. Lo scope `perform` di `/exec`, però,
formula il presidio come supervisione della collezione versionata `o3/`. Non
rende esplicito che una stessa prescrizione può avere materializzazioni su una
superficie dichiarata del Mondo — PDF, export, payload o copia pronta all'uso —
specialmente quando sensibilità o vincoli del dominio ne impediscono la
versione nel repository.

La chiusura del task ha quindi potato intenzione e specifica, ma non ha
enumerato tutti i prodotti operativi generati lungo l'esecuzione. Il difetto
non è l'assenza di una regola sul consumo: è il perimetro fisico troppo stretto
del controllo di chiusura.

## La distinzione da preservare

Una verifica sulle superfici del Mondo non autorizza a cancellare genericamente
gli effetti dell'atto. Il referto, l'email inviata o il documento ricevuto hanno
significato autonomo e sono evidenza del Mondo; il PDF del canovaccio era invece
una materializzazione della prescrizione. Il test del significato senza
artefatto (`world`) offre già il discriminante concettuale, mentre target esatto
e autorizzazione restano necessari per ogni rimozione esterna.

## Domanda aperta

La chiusura di o3 deve includere un controllo esplicito delle materializzazioni
della prescrizione sulle superfici dichiarate del Mondo, classificandole come
effetto/evidenza durevole oppure copia operativa consumata? E lo scope
`perform` di `/exec` deve chiedere questa enumerazione quando chiude una
prescrizione o il task che l'ha prodotta?

## Perché non è generalizzato qui

Il caso mostra una lacuna concreta in un adottante, ma resta un solo caso. La
forma portabile — regola in `perform`, controllo nella skill o entrambi — è una
valutazione i2→i3 di `method`; questa cattura registra il segnale senza
ratificarne in anticipo la soluzione.
