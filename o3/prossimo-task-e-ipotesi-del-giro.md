---
data: 2026-10-20
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, baserow, danea-auto
---

# Ogni giro dichiara il prossimo task e le ipotesi che ha formato

## Cosa e perché

Il centro del ciclo è la revisione delle priorità: nuove percezioni,
verifica delle interpretazioni in `i2/`, verdetto contro il Goal (o proposta
di correggerlo), dipendenze e priorità, e infine il prossimo task, confermato
o cambiato. Nei giri autonomi dall'11/10 questo sbocco non arriva al custode
(`i1/giri-ipotesi-implicite-e-prossimo-task-2026-10-20.md`):

- `/exec plan` chiude col task consigliato, ma il resoconto di `/cycle` non
  lo chiede e la vista non lo mostra; `plan=vuoto`, l'esito più frequente
  nella maggior parte dei repo, non distingue la coda riesaminata e
  confermata da quella non guardata;
- un'ipotesi può nascere e cadere senza passare da `interpret`: in `bi` una
  tesi causale scritta in un task il 19/10 è smentita il 20/10, con
  `interpret=vuoto` in entrambi i giri. È ricostruibile da git solo perché il
  secondo giro l'ha citata.

Il canone ora chiede (`kb/skill.md`, `kb/interpret.md`, `kb/plan.md`):

- il trailer **`Prossimo:`** nel commit di ogni giro che invoca `exec plan`:
  `<task> (confermato)`, `<task> (cambiato, era <task>; <causa>)` oppure
  `nessuno (<motivo>)`, col titolo della riga del plan. Un cambio nomina la
  causa risalendo la catena; una conferma dice cosa è stato riesaminato;
- in `eval interpret`, il riconoscimento delle **ipotesi formate nel giro**
  dalla forma («perché», «quindi», previsioni, generalizzazioni da pochi
  casi), portate nel presidio con affermazione, provenienza, criterio di
  smentita e orizzonte; le smentite si citano, non si riscrivono;
- nella vista, il prossimo task in home e nella pagina del giro; il giro è
  giallo se il trailer manca o se il task differisce da quello precedente
  nella storia, anche quando l'agente lo dichiara confermato. Il confronto
  lo fa la vista, non l'agente.

## Ricetta per il /method locale

1. **`exec`**: nel fork, dopo il trailer `Esiti:`, il formato di `Prossimo:`;
   al passo 4 di `plan` il confronto con l'ultimo `Prossimo:` della storia e
   le due forme di chiusura (conferma motivata, cambio con causa). Preservare
   le parametrizzazioni di dominio.
2. **`eval interpret`**: il paragrafo «Ipotesi formate nel giro» e l'esito
   che elenca le ipotesi nate, confermate o smentite. Mappare il presidio sul
   repo: la sintesi `i2/` pertinente, il registro delle ipotesi se esiste, o
   un filo con criterio. Nessun contenitore nuovo se uno esistente basta.
3. **`cycle` e `commit`**: le due voci nuove del resoconto finale e
   `Prossimo:` fra i trailer. Se il prompt locale del ciclo autonomo elenca
   il contenuto del resoconto o i trailer, allinearlo.
4. **Vista**: `o3/view/ciclo.py`, `tests/test_ciclo.py` e la regola
   `.ciclo-prossimo` di `o3/view/assets/system-image.css` dal canone;
   `project.py` resta locale. Verifica con i test e `build.py --check`.
5. **Primo giro dopo il recepimento**: non ha un `Prossimo:` precedente con
   cui confrontarsi; dichiara la testa della coda attuale come
   `(confermato)` e la motiva. Da lì il confronto è meccanico.
6. Registrare il recepimento nel marker `i3/allineamento-metodo.md`.

## Indizi da verificare sul posto

- **bi**: il caso del 19–20/10 in `o2/diagnosi-crescita-orfani.md`
  (`6a0bc3d1`, `8635f663`) è materiale per il primo giro: la tesi smentita
  può entrare nel presidio come ipotesi caduta, con la formulazione
  originale.
- **economia**: `i2/angolo-nostradamus.md` è già un registro di previsioni;
  probabile destinazione naturale delle ipotesi formate nel giro.
- **danea-auto**: non ha ancora `/cycle` (`ciclo-autonomo`, prescritta il
  2026-10-11) né `presidio-ipotesi`; l'osservazione che li rinviava è chiusa
  il 2026-10-20. Conviene recepire le tre insieme. La previsione aperta sul
  rinnovo di LibreOffice (verso il 27/10) è già nella forma richiesta e non
  va toccata dal recepimento.
- **crm**: fuori dal ciclo autonomo dal 2026-10-19 e verso la dismissione;
  recepisce solo se torna a fare giri.

## Verifica

`git log --format='%(trailers:key=Prossimo,valueonly)'` dà una riga per ogni
giro con `exec plan`. La home mostra il prossimo task accanto a ogni giro e
un cambio di priorità in giallo. All'audit `/adottanti` si leggono insieme
`Esiti:` e `Prossimo:`: quante conferme, quanti cambi, quanti con causa
nominata; e quante ipotesi nate o smentite in `interpret`.
