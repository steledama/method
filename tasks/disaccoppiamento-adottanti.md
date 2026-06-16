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
- una **sezione README canonica** che dichiara l'adozione del metodo (riferimento +
  brevissima descrizione, il symlink `method/` in root) e i due poli del ciclo del
  dominio — **Goal** e **World** — sotto heading fissi e machine-readable;
- hub `cognitive-artifact-design.md`, unico nome di nodo assunto stabile.

La sezione README canonica è comune ai 5 repo (i 4 adottanti e `method`) ed è anche
la sorgente da cui la home (task «System image visiva») ricava i poli Goal e World:
i riferimenti del polo World sono **espliciti** per repo, mai derivati per euristica
dall'organizzazione del remote (che differisce — es. `bi` su `tt-sviluppo`, gli altri
su `steledama`). La sua struttura è formalizzata in `kb/readme.md`.

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

La _struttura_ README canonica che ne è il veicolo concreto vive invece in
`kb/readme.md`: il principio (method-development) dice _perché_ disaccoppiare, il
nodo `readme` dice _quale forma uniforme_ prende la dichiarazione.

## Implementazione

1. Formalizzare in `method-development.md` la distinzione tra dipendenza
   generale, connessione intenzionale e coupling accidentale.
2. Formalizzare in `kb/readme.md` la sezione README canonica: dichiarazione di
   adozione + symlink `method/` + i due poli Goal e World sotto heading fissi e
   machine-readable.
3. Restrutturare il `README` di `method` alla sezione canonica (poli Goal e World
   espliciti) e riscriverne gli step di onboarding: dichiarare il metodo e il hub,
   senza prescrivere un inventario di path in `CLAUDE.md`.
4. Cercare nei quattro adottanti i riferimenti a `method/*.md` e classificarli
   secondo la decisione sopra; la metrica non è «zero link», ma «zero link senza
   funzione locale».
5. Preparare in `prescriptions/` un runbook unico (criteri di classificazione dei
   link + adozione della sezione README canonica) e applicarlo in ogni adottante
   tramite il proprio `method-review`, verificando in loco quali link mantenere,
   riscrivere o rimuovere. È il **round 1** della propagazione del cluster, distinto
   dal round 2 (rename `deck→view`) del task successivo.
6. Dopo il round 1 nei quattro repo, rimuovere la prescrizione esaurita e
   aggiornare il verdetto corrente.

La passata sugli adottanti precede il rename `deck`→`view`: riducendo prima i
riferimenti accidentali, il rename successivo tocca solo le connessioni
intenzionali rimaste.

## Criteri di chiusura

- il principio vive in `method-development.md`;
- la struttura README canonica vive in `kb/readme.md` e i 5 README espongono le
  sezioni Goal e World sotto heading fissi;
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
