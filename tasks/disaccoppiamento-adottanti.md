---
data: 2026-06-15
stato: aperto
---

# Disaccoppiamento adottante↔metodo: dichiara e taci

Aperto in sessione 2026-06-15. Il dolore ricorrente — a ogni rename di nodo si
toccano `CLAUDE.md`, `README.md` e altri file dei quattro adottanti — segnala un
coupling eccessivo alla struttura interna del metodo. L'obiettivo non è
eliminare ogni collegamento, ma distinguere la dipendenza generale dal metodo
dalle connessioni che hanno un significato locale preciso.

## Decisione

L'adottante dichiara una volta, nel proprio `README`, di adottare il metodo come
insieme. Il contratto stabile è composto da:

- symlink `method/`;
- dichiarazione di adozione nel `README`;
- hub `cognitive-artifact-design.md`, unico nome di nodo assunto stabile.

Da questa dichiarazione non segue un divieto assoluto di link ai nodi interni.
I riferimenti diretti restano ammessi quando esprimono una dipendenza
**semantica** o **operativa** reale:

- un nodo locale collega esplicitamente il proprio concetto a un concetto del
  metodo;
- una regola o uno strumento locale rimanda alla propria specifica canonica;
- un task usa un nodo metodologico come vincolo o contesto necessario.

Sono invece coupling accidentale, da rimuovere:

- inventari diffusi dei nodi del metodo;
- elenchi orientativi che duplicano il hub;
- richiami aggiunti solo per dire genericamente «questa regola viene dal
  metodo»;
- path interni copiati in più file senza una funzione locale distinta.

La formula «dichiara e taci» significa quindi: **dichiara una volta l'adozione;
altrove collega solo ciò da cui il contenuto dipende davvero**.

## Casa del principio

Il principio entra come sezione di `kb/method-development.md`, non come nodo
autonomo. Descrive infatti il confine di evoluzione e propagazione tra canone e
adottanti: interfaccia stabile, struttura interna volatile, ultimo miglio
deciso nel repo adottante.

## Implementazione

1. Formalizzare in `method-development.md` la distinzione tra dipendenza
   generale, connessione intenzionale e coupling accidentale.
2. Riscrivere gli step di onboarding nel `README` di `method`: dichiarare il
   metodo e il hub, senza prescrivere un inventario di path in `CLAUDE.md`.
3. Cercare nei quattro adottanti i riferimenti a `method/*.md` e classificarli
   secondo la decisione sopra; la metrica non è «zero link», ma «zero link senza
   funzione locale».
4. Preparare in `prescriptions/` un runbook unico con i criteri e i touchpoint
   osservati. Ogni adottante lo applica tramite il proprio `method-review`,
   verificando in loco quali link mantenere, riscrivere o rimuovere.
5. Dopo l'adozione nei quattro repo, rimuovere la prescrizione esaurita e
   aggiornare il verdetto corrente.

La passata sugli adottanti precede il rename `deck`→`view`: riducendo prima i
riferimenti accidentali, il rename successivo tocca solo le connessioni
intenzionali rimaste.

## Criteri di chiusura

- il principio vive in `method-development.md`;
- l'onboarding non prescrive più link diffusi alla struttura interna;
- ogni riferimento residuo negli adottanti è classificabile come semantico o
  operativo;
- la prescrizione è stata applicata dai quattro `method-review`;
- audit e ricerca globale non trovano link rotti né inventari duplicati;
- il rename `deck`→`view` può propagare senza una nuova bonifica generale.

## Relazione con gli altri task

Il task è primo in ordine per costo/opportunità, non perché il task «Strato di
presentazione» dipenda tecnicamente da esso. È l'ultima passata generale pagata
per l'over-coupling; i rename successivi devono avere un costo proporzionato
alle sole dipendenze reali.
