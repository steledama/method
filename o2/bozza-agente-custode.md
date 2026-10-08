---
sintesi: "Una bozza che censisce gli usi di «agente» e «custode» nel repo, propone la distinzione da portare nel README e lascia aperte le domande che l'uso attuale non risolve."
ciclo: dev
---

# Bozza agente e custode

Il custode propone il 2026-10-08 di chiamare **agente** l'agente IA e
**custode** l'agente umano. La distinzione va nel README, non in un nodo
aggiunto, e va verificata su ogni occorrenza dei due termini.

## Cosa si sa

- Nei nodi `kb/` `agente` ricorre circa 40 volte, `custode` 8, `agente
umano` 4 (conteggio del 2026-10-08, da rifare sul repo intero).
- `kb/consent.md` chiama agenti tutti e due («i due agenti del sistema»,
  «l'umano è l'agente che chiude il cappio»). È coerente con la cognizione
  distribuita, da cui il metodo parte: lì l'agente non è per definizione
  artificiale.

## Lavoro

1. Censire le occorrenze di `agente`, `custode`, `umano`, `LLM`, `IA`,
   `modello` in `kb/`, register, skill e bussole, e classificarle: IA,
   umano, entrambi, ambiguo.
2. Scrivere nel README la distinzione dove l'uso è netto.
3. Correggere le occorrenze improprie, nodo per nodo.

## Domande aperte

- Serve un termine che comprenda entrambi (oggi «agente» lo fa in teoria)?
  Se sì quale, e dove lo si usa.
- «Custode» indica un ruolo (chi tiene goal, world e criteri) o la persona?
  In `goal.md` è «Custode umano: Stefano».
- Le domande senza una strada netta dall'uso restano qui, non si chiudono per
  decreto.
