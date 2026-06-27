---
stato: iniziale
sintesi: "Il meccanismo di estensione del frontmatter per un attributo intrinseco di dominio è sanzionato in kb/node.md (criterio dei 4 requisiti: intrinseco, valori chiusi e singolo, non derivabile, verificabile da kb_tools). Il campo `data` è stato rimosso del tutto (falliva non-derivabile e non-verificabile). Resta da: dotare kb_tools della verifica di una proprietà faceted dichiarata; sciogliere la generalizzabilità agli altri adottanti. Sblocca la Fase 4 di nixos (campo `mondo` su ~40 nodi)."
---

# Attributo intrinseco di dominio nel frontmatter dei nodi

## Decisione presa

Il segnale i1 da `nixos`
([perceptions/frontmatter-senza-slot-per-attributo-di-dominio.md](../perceptions/frontmatter-senza-slot-per-attributo-di-dominio.md))
è sciolto sul merito: il metodo **sanziona** un meccanismo di estensione del
frontmatter oltre `{data, stato}`, governato dal **criterio dei quattro requisiti**
ora inciso in [`kb/node.md`](../kb/node.md) — la proprietà è ammessa solo se
**intrinseca**, a **valori chiusi e singola** (faceted, non tag aperto), **non
derivabile** da una fonte di verità esistente, e **dichiarata e verificabile** da
`kb_tools`. La proprietà specifica resta **locale all'adottante**; ciò che il canone
sanziona è il meccanismo, non la singola proprietà.

## Lavoro residuo

- **`kb_tools`: verifica della proprietà faceted dichiarata.** Il quarto requisito
  («dichiarata e verificabile») esige che `tools/kb_tools.py` sappia leggere un
  insieme di valori ammessi dichiarato dall'adottante e verificare, per ogni nodo,
  presenza del campo e appartenenza al dominio — come già fa per `stato`. È
  implementazione in `method` (backend canonico). Da decidere: dove vive la
  dichiarazione del dominio dei valori (config dell'adottante? convenzione?) e come
  `kb_tools` la scopre senza cablare nomi di campo specifici.

- **Generalizzabilità (punto 2 del segnale).** Il **meccanismo** è canone e vale per
  tutti. Resta da verificare, adottante per adottante, se ne nasce una **proprietà**:
  per `bi`, `economia`, `salute` l'esito atteso è «adozione di una proprietà propria»
  oppure «non applicabile, oggi». Nessuno è obbligato ad avere attributi estesi.

## Punto 3 — campo `data`: chiuso (rimosso)

Sciolto il 2026-06-27: `data` è **rimosso del tutto** dal frontmatter di nodi e task.
Applicando lo stesso criterio di demarcazione appena inciso, `data` falliva due
requisiti — **non derivabile** (la data di creazione è una fetta della storia git) e
**verificabile** (`kb_tools` ne controllava solo la presenza, mai il valore: una data
sbagliata era invisibile, e verificarla significherebbe ri-derivarla da git, rendendola
ridondante). La contro-giustificazione «àncora di provenienza robusta alle riscritture
di history» è reale ma non basta: àncora un valore che nessuno strumento consuma, e un
adottante con quel bisogno specifico (`nixos` pre-split pubblico) lo risolve fuori dal
canone, non come campo sanzionato. `stato` resta l'unico campo obbligatorio, perché
giudizio non ricostruibile. Inciso in `kb/node.md` e `kb/tasks.md`, propagato ai nodi e
allineato in `kb_tools` (check di presenza su `stato`).

## Applicazione attesa (a valle, in nixos)

Una volta dotato `kb_tools` della verifica: campo `mondo: lavoro | casa | trasversale`
sui ~40 nodi della KB di `nixos` (oggi la ripartizione ~9/8/23 vive solo nella prosa
di un task) più il check. Lì la **Fase 4** (predisposizione separazione lavoro/casa)
è sospesa in attesa di questo sblocco. L'applicazione è lavoro dell'adottante, non di
`method`: qui resta il meccanismo e il suo supporto in `kb_tools`.

## Criterio di chiusura

`kb_tools` verifica una proprietà faceted dichiarata; l'esito di generalizzabilità è
registrato per i quattro adottanti (il campo `data` è già chiuso, rimosso). A quel
punto il filo in `verdict.md` si chiude e `nixos` può eseguire la Fase 4 senza
ulteriori dipendenze da `method`.
