---
data: 2026-06-15
stato: aperto
---

# Disaccoppiamento adottante↔metodo: dichiara e taci

Aperto in sessione 2026-06-15. Il dolore ricorrente — a ogni rename di nodo si
toccano `CLAUDE.md`/`README.md` dei 4 adottanti — è il sintomo di un
over-coupling: gli adottanti hardcodano path a nodi interni che il metodo fa
evolvere. La cura è invertire la dipendenza: l'adottante dipende dal metodo
**come tutto** (una dichiarazione), non dalla sua struttura interna —
interfaccia stabile, struttura volatile.

## Principio

- **un solo àncora stabile**: la dichiarazione di adozione nel `README`
  dell'adottante + il symlink `method/` + il **hub** `cognitive-artifact-design.md`
  (l'unico nodo il cui nome è contratto di stabilità). Tutto il resto si
  raggiunge da lì e può cambiare nome liberamente.
- **dichiara e taci**: l'adottante cita il metodo una volta, in `README`, in
  modo generale; **evita i link sparsi a path di nodi** nei propri file. Non
  significa «smettere di usare la struttura» — le regole operative locali
  restano, ma parlano in proprio o rimandano al hub, non a `method/<nodo>.md`.
- **trade-off accettato**: l'adottante perde i puntatori precisi «dove è definito
  X»; mitigato dalla scopribilità dei nodi via symlink a partire dal hub.

## Implementazione

1. casa del principio — **decidere**: nuovo nodo `kb/` (es. `loose-coupling.md`)
   oppure sezione in `method-development.md` (la dinamica di sviluppo e
   propagazione). Propendo per la sezione in `method-development`, per evitare
   proliferazione di nodi — da confermare.
2. riscrivere gli **step di onboarding** nel `README` di `method`: oggi gli step
   3-4 dicono di hardcodare i path dei nodi in `CLAUDE.md` — contraddicono il
   principio e vanno invertiti (dichiara il hub, non i singoli nodi).
3. passata sugli adottanti per **ridurre i riferimenti** ai nodi interni,
   lasciando la sola dichiarazione + hub. Va **prima** del rename deck→view: una
   volta tolti i riferimenti diffusi, quel rename non richiede più una seconda
   passata sugli adottanti.

## Relazione con gli altri fili

Questo filo è **primo in esecuzione** proprio per disinnescare il costo del task
«Strato di presentazione»: oggi il rename deck→view costerebbe pieno perché gli
adottanti hanno riferimenti diffusi; ripuliti prima, i rename — questo e i futuri
— costano quasi zero. È l'ultima volta che si paga il prezzo pieno
dell'over-coupling.
