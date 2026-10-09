---
ciclo: runtime
---

# Segnale: `Esiti:` è un trailer solo se sta nell'ultimo paragrafo del messaggio

Data: 2026-10-05 · Fonte: baserow — commit `205c627` e fork di `/commit` in
`36518f9`

## Il segnale

La prescrizione `esiti-per-stadio-nel-commit` misura gli esiti per stadio
leggendo il trailer `Esiti:` dei commit di giro. La skill canonica `/commit`
mostra come scriverlo con un secondo `-m`:

```
git commit -m "descrizione del giro" -m "Esiti: perceive=vuoto interpret=materia compare=materia"
```

Git riconosce come trailer solo le righe `Chiave: valore` dell'**ultimo
paragrafo** del messaggio. In `baserow` `205c627` la riga `Esiti:` era seguita
da una riga vuota e da un `Co-Authored-By:` aggiunto su istruzione dell'harness:
`git log --format='%(trailers:key=Esiti,valueonly)'` restituisce vuoto, mentre
`grep '^Esiti:'` sul corpo trova la riga. Il commit è su `origin` e non viene
riscritto.

Conteggio del 2026-10-05 sui commit dal 2026-09-25, righe `^Esiti:` contro
trailer letti da git:

- `bi` 8/8, `nixos` 3/3, `danea-auto` 24/24, `metodo` 3/3;
- `baserow` 2/1, l'unica perdita;
- `crm` 0/0, nessun giro.

`nixos` e `danea-auto` hanno anch'essi righe `Co-Authored-By:`, ma nello
stesso paragrafo di `Esiti:`, e i loro trailer si leggono tutti.

## Cosa ha fatto l'adottante

Il fork di `/commit` di `baserow` (`36518f9`) ora prescrive: tutti i trailer
nell'ultimo paragrafo, senza righe vuote in mezzo; verifica del messaggio con
`git interpret-trailers --parse` prima del commit e con
`git log -1 --format='%(trailers)'` dopo.

## Contesto

Il custode ha deciso il 2026-10-05 di omettere `Co-Authored-By` in tutti i
repo, come già prescrive la skill canonica. Questo toglie la causa del caso
osservato, ma non la fragilità: qualunque riga aggiunta dopo il paragrafo di
`Esiti:` lo fa ignorare come trailer. Il fork di `danea-auto` vieta già la
riga, eppure 23 suoi commit dal 2026-09-25 la portano: la regola nella skill
da sola non ha fermato l'harness. Da `nixos` `6262067` l'attribuzione è spenta
nelle impostazioni di Claude Code (`attribution` con `commit` e `pr` vuoti),
verificata su `svezia` con una prova e il suo controllo inverso.

Un solo caso di perdita. Il conteggio del 2026-11-01 può comunque leggere le
righe `^Esiti:` del corpo oltre ai trailer, per non perdere `205c627`.

## Stato del seguito

Al riesame del 2026-10-09 la skill canonica `/commit` prescrive tutti i
trailer nell'ultimo paragrafo, insieme. Il marker di `danea-auto` dichiara
anche la verifica con `git interpret-trailers`: è recepimento del presidio,
non un secondo caso osservato di perdita. La cattura resta raggiungibile
fino al conteggio del 2026-11-01 per recuperare `205c627`, come previsto in
`o2/rivalutazione-skill-per-arco.md`; il conteggio confronterà trailer e
righe nel corpo senza duplicare il commit.
