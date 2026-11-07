---
sintesi: "Il custode ha deciso il 2026-11-07 che la lingua canonica di method è l'inglese e l'italiano è secondario. Resta da decidere come si deriva l'italiano senza raddoppiare la manutenzione: cosa si traduce, dove vive la copia e come se ne verifica l'allineamento."
ciclo: dev
decidere: "Con quale perimetro, collocazione e verifica di allineamento si deriva l'italiano dall'inglese canonico?"
---

# Traduzione in inglese

## Origine

La proposta l'ha portata la sessione `nixos` su `deck`, inoltrata il
2026-11-07 su richiesta del custode, insieme alla licenza: prima la licenza
(commit `d00059d`, che copre anche le traduzioni), poi la traduzione. Il
messaggio non porta autorizzazioni nuove.

## Decisione presa

Il 2026-11-07 il custode ha stabilito che la lingua principale è l'inglese
e quella secondaria l'italiano. L'inglese fa fede: una differenza fra le
due versioni si risolve correggendo l'italiano.

## Punti da decidere

- **Perimetro.** Proposta: si traduce in italiano solo la superficie letta
  da fuori, cioè `README.md`, `kb/` e `presentation/`. Le collezioni di
  lavoro (`i1/`–`i3/`, `o1/`–`o3/`), i register, `CLAUDE.md`, `AGENTS.md`,
  `autonomy.md` e le skill passano al solo inglese. Senza questo taglio ogni
  giro del ciclo raddoppia le scritture.
- **Collocazione.** Le due forme possibili sono un file gemello
  (`kb/node.it.md`) oppure un albero separato (`it/kb/node.md`). Il gemello
  tiene vicine le due versioni e rende evidente quando ne manca una;
  l'albero separato lascia `kb/` pulita per gli adottanti, che la leggono
  via symlink.
- **Allineamento.** Proposta: l'italiano è una derivazione, come le viste.
  Lo produce l'agente e porta il commit della fonte inglese da cui deriva;
  il gate di `/commit` segnala in modo deterministico la copia rimasta
  indietro. Un nodo inglese cambiato con l'italiano vecchio è un ritardo
  dichiarato, non un errore che blocca il commit.
- **Adottanti.** Leggono `kb/` via symlink e hanno code e `kb/` locale in
  italiano. Il passaggio del canone all'inglese cambia ciò che vedono e le
  skill che forkano. Da decidere se lo recepiscono con il normale `/method`
  o se serve un avviso apposito; la delega di questo repo non li copre.
- **Ordine.** Proposta: prima si fissa la forma in un nodo `kb/`
  (generalizzabile: qualunque adottante bilingue la riusa), poi si traduce
  a lotti partendo da `README.md` e dall'hub `cognitive-artifact-design.md`.
