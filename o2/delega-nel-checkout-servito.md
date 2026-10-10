---
sintesi: "Da decidere: dove il checkout è anche una superficie servita (timer, cron, scheduler che leggono HEAD o il working tree), commit e pull sono rilasci. Proposta: il bootstrap lo fa riconoscere prima del primo atto e autonomy.md nomina quella superficie; prescrizione ai sette dopo la decisione."
ciclo: dev
---

# Delega nel checkout servito

Stato: **da decidere** (`confine-delega`, impatto alto: cambia la forma
canonica dei criteri di autonomia che gli adottanti recepiscono).

## Motivo

La lettura in [`i2/casi-delega-adottanti.md`](../i2/casi-delega-adottanti.md)
trova quattro casi in due adottanti (`bi`, `crm`) in cui il checkout del
ciclo delegato è anche una superficie servita: in `bi` il commit è già in
esercizio per i cron, in `crm` il timer pubblica l'`HEAD` sulla 8002 e il
pull è partito prima che l'agente riconoscesse `svezia`. La stessa
condizione è dichiarata senza caso in `baserow` (`5fc585c`) e
`danea-auto`. [consent](../kb/consent.md) dice che la delega comprende
commit e push e che gli adottanti ne definiscono il perimetro; non dice che
il perimetro va letto sulla superficie servita prima del primo atto. Un
battito schedulato, senza custode, non potrebbe chiedere su quel confine.

La scelta fra le due vie del passo 3 di `pull-autonomo` resta di dominio:
i custodi di `crm`, `baserow` e `bi` hanno scelto tre soluzioni diverse.

## Alternative

1. **Riconoscimento nel canone (proposta).** Una frase in
   [consent](../kb/consent.md): dove commit, pull o push del checkout sono
   rilasci o pubblicazioni, `autonomy.md` nomina quella superficie e dice
   quale atto del ciclo la raggiunge; il bootstrap fa riconoscere host e
   checkout prima del primo atto. Prescrizione ai sette con indizi per repo
   (`bi`, `crm`, `baserow`, `danea-auto` con superficie nota; `deck` per le
   viste di `nixos`, `salute`, `economia`). Costo: un giro `/method` per
   adottante.
2. **Attendere il battito del 2026-11-01.** Evidenza prima della struttura:
   oggi i casi sono quattro, tutti risolti dal custode nella stessa
   sessione. Il rischio è arrivare ai criteri del pilota senza il criterio.
3. **Solo osservatorio.** Nessun canone: `/adottanti` verifica la
   superficie servita nel giro mensile. Lascia il riconoscimento alla
   memoria del custode.

## Decisione richiesta

Scegliere fra 1, 2 e 3. Con la 1, l'agente scrive il nodo e la
prescrizione nel giro successivo; con la 2, il task torna al battito; con
la 3, si aggiunge un controllo allo step dei casi di `/adottanti` e il
task si chiude.

## Verifica

Accettata la 1: il nodo regge `kb_tools.py audit` e la build; la
prescrizione si chiude quando i sette marker la dichiarano recepita e
nessun nuovo caso riporta un atto non riconosciuto su un checkout servito
entro il battito successivo.
