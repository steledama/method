---
data: 2026-10-29
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, baserow, danea-auto
---

# Le attese dichiarano come si riconosce il risveglio

## Cosa e perché

Il 2026-10-29 il custode ha deciso la forma del risveglio delle attese
(`563e8d1`, `7aa742b`; `kb/plan.md`, «Risveglio»). Ogni `w` dichiara
`probe:` o `arrival:`, ogni `w` e ogni `p` porta `by:`, e un'attesa tenuta dal
custode è una `p`. Il requisito è che l'arrivo non sfugga: la sonda lo
garantisce oltre la cadenza dello strumento, il termine fa da rete sotto
l'arrivo da un canale che il giro non legge, e su una `p` chiede se il task
vale ancora.

All'inizio il recepimento doveva passare dal solo nodo, finché un secondo
adottante non avesse avuto uno strumento che controlla le attese. Il custode
ha cambiato idea dopo che `nixos` ha costruito il primo interprete
(`0a7cb7c`): uno strumento del genere ha un contratto da rispettare, e il
rilievo di `exec plan` da solo non lo verifica.

## Ricetta di recepimento

1. Nella legenda del plan dai a ogni `w` un `probe:` o un `arrival:`, e a ogni
   `w` e ogni `p` un `by:` (data o mese). Un'attesa che aspetta una mossa del
   custode passa a `p`, col primo numero libero della lettera; un'attesa
   composita prende la lettera della prima mossa attesa. Le date dei `by:`
   proposte dall'agente le conferma il custode.
2. Nel fork di `exec plan` aggiungi il rilievo (una `w` senza `probe:` né
   `arrival:`, una `w` o una `p` senza `by:`) e l'evento del `by:` passato,
   coi tre esiti: sollecitare (per una `p`, riprendere), riclassificare o
   rinnovare col motivo; nel giro senza custode la riga va in `Attenzione:`.
   Nel fork di `eval perceive` aggiungi il confronto dei fatti in ingresso
   con le `w` ad `arrival:`. Preserva le parametrizzazioni di dominio.
3. Se il repo ha uno strumento che controlla attese o scadenze, rispetta il
   contratto:
   - prende solo le `w` con `probe:` e mostra i `by:` passati come righe di
     riesame, non come scadute;
   - unisce le righe di continuazione della chiosa prima di estrarre
     `probe:` e `by:`, perché il formatter può andare a capo;
   - valuta solo i tipi del suo vocabolario chiuso, senza il modello, e non
     esegue mai un comando preso dal plan; un tipo sconosciuto è un errore
     segnalato, non un comando;
   - ha test senza rete e un permesso del giro per il solo strumento, che
     concede il custode.

   Senza uno strumento del genere non se ne costruisce uno per questa
   prescrizione: le `w` sondabili si dichiarano comunque con `probe:`, e lo
   strumento nasce quando il controllo a mano ricorre. Il riferimento è
   l'interprete di `nixos` (`o3/scripts/probe.sh`, `0a7cb7c`).

4. Registra il recepimento nel marker `i3/allineamento-metodo.md`, in una
   riga che nomina `risveglio-delle-attese` come recepita.

## Note per repo

Indizi dal confronto del 2026-10-29, da verificare in loco.

- `nixos`: già conforme (`3cb37d2`, `0a7cb7c`); manca solo la riga nel
  marker.
- `danea-auto`: «Riapre: …, o in mancanza `<data>`» è già la forma, da
  riscrivere con le parole chiave; w3, w4 e w6 sono sondabili su log locali.
- `economia`: w1 («l'ok di Stefano») è una `p`; w3 e w4 arrivano da canali
  che il giro non legge e il loro `by:` è una scadenza di sollecito.
- `bi`: va verificato se la decisione di `p1` spetta al custode; se spetta a
  Luigi è una `w`. w2 ha una sonda parziale.
- `salute`: w1 è un `arrival:` riferito dal custode, col `by:` dopo la seduta
  del 3/11.
- `baserow`: nessuna attesa aperta; bastano i fork di `exec` ed `eval`.

## Verifica

`python3 o3/prescrizioni.py verifica risveglio-delle-attese` dà la
prescrizione recepita in ogni adottante. Il primo `exec plan` dopo il
recepimento non trova rilievi sul risveglio, oppure li corregge.
