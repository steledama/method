---
ciclo: dev
---

# Il giro Codex non espone Read per le letture fuori checkout

Nel giro a mano di method dell'11/11/2026, partenza `e8d5b664`
alle 18:13:16 +01:00, il catalogo degli strumenti esposti non comprende un
tool Read per file locali. Il prompt e `/cycle` richiedono quel tool, senza
`cat` o `ls`, per `~/.local/state/ciclo/method/fetch.json` e per gli stati
dei giri fuori checkout. Nessuna lettura alternativa è stata tentata.

Il giro legge i marker con `o3/adottanti.py show` e il proprio
`i1/giri/tentativi.jsonl`; non verifica l'id, l'esito o `ultimo_riuscito`
del fetch corrente. L'età degli origin di svezia resta ignota e i loro log
non provano la freschezza rispetto al server. Per gli adottanti non sono
state lette direttamente le chiusure fuori checkout.

È una capacità mancante nell'interfaccia esposta, non un diniego ricevuto.
Il lavoro di adattamento è in
[lanciatore-ciclo-nel-metodo](../o2/lanciatore-ciclo-nel-metodo.md);
la cattura si consuma quando una lettura autorizzata di questi soli stati
è verificata in un giro Codex. Nessuna proposta allarga il perimetro dei dati.
