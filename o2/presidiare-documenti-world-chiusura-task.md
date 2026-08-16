---
sintesi: "Estendere la chiusura dei task alle materializzazioni prodotte sulle superfici dichiarate in world.md: enumerarle, distinguere effetti ed evidenze durevoli dalle copie operative consumate e proporre la pulizia con target e autorità espliciti."
ciclo: dev
---

# Presidiare documenti World alla chiusura task

## Problema

La chiusura canonica di un task controlla `o1/plan.md`, il file `o2/` e
l'eventuale prescrizione `o3/`, ma non rende esplicito il controllo dei
documenti operativi che il task ha prodotto sulle superfici dichiarate in
`world.md`. In `salute` il PDF di un canovaccio medico è così sopravvissuto alla
chiusura del task fino a una revisione successiva, benché decisioni ed esiti
fossero già risaliti nell'artefatto.

Il secondo segnale ha sciolto l'attesa sull'estensione per-stadio del criterio
«significato senza artefatto» (`i3/criterio-world-substrato.md`): il difetto è
nel perimetro del controllo con cui `exec plan` riconosce il task chiuso, non
soltanto nella supervisione della collezione `o3/`.

## Atto

- incidere in `kb/tasks.md` che la chiusura enumera anche le materializzazioni
  note del task sulle superfici dichiarate del Mondo;
- applicare il test di `kb/world.md`: effetti ed evidenze con significato
  autonomo restano nel Mondo, le copie operative consumate sono candidate alla
  pulizia;
- aggiungere il controllo allo scope `plan` di `.claude/skills/exec/SKILL.md`,
  coordinandolo con `perform` quando il task aveva anche una prescrizione
  `o3/`;
- verificare retrospettivamente la formulazione sul caso `salute` e stabilire
  se il cambio di skill richiede una prescrizione di propagazione agli
  adottanti.

## Vincoli

- leggere soltanto le superfici che il register `world.md` dichiara;
- non trasformare la chiusura in una scansione indiscriminata del Mondo: la
  specifica del task e la prescrizione sono la mappa primaria dei prodotti da
  cercare;
- non cancellare effetti, evidenze o fonti che conservano significato senza
  l'artefatto;
- una rimozione esterna richiede target esatto e autorità esplicita: in loro
  assenza la skill propone la pulizia e si ferma;
- fondere prima di potare: verificare che il contenuto utile sia già risalito
  nell'artefatto o resti in una fonte durevole.

## Criterio di chiusura

`kb/tasks.md`, il criterio World e `exec plan` descrivono un unico controllo
ripetibile; il caso `salute` viene classificato senza memoria di sessione; la
distinzione copia operativa/evidenza impedisce sia il residuo inosservato sia
la cancellazione generica nel Mondo; l'eventuale propagazione ai fork è
predisposta oppure dichiarata non necessaria.
