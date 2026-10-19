# Ciclo autonomo di method

Esegui `/cycle autonomo`: un giro `eval all → exec all → commit` senza
custode, secondo la skill `cycle` del repository. Qui sta solo ciò che è
locale.

## Copertura

Sei al gradino 1: il timer lancia l'unità `ciclo-method` su `deck` ogni
giorno alle 15:00, un'ora dopo `nixos`, perché il perceive trovi i giri degli
adottanti del giorno; il giro è coperto da `ciclo-autonomo`. Un avvio a mano
dell'unità resta coperto dallo stesso criterio. Il perimetro è quello del
criterio `ciclo-autonomo` di `autonomy.md`, regola di sospensione compresa; i
permessi sono quelli di `o3/ciclo/permessi.json`, che il giro non modifica.

Trailer di copertura nel commit del giro:

```
Impatto-motivo: ciclo-autonomo (autonomy.md, ciclo schedulato)
```

## Perimetro

Il giro tiene vivi `i1/`, `i2/`, `i3/`, plan, task e i nodi di `kb/`. Un nodo
`kb/` arriva subito agli adottanti via symlink: correggilo solo con una fonte
verificata e dichiara nel resoconto ogni nodo toccato. Prescrizioni e
strumenti in `o3/`, skill canoniche, `presentation/`, `CLAUDE.md`,
`autonomy.md` e `goal.md` restano proposte. `/adottanti` e `/method` non
girano nel giro.

## Adottanti

Il perceive legge i marker `i3/allineamento-metodo.md` dai checkout locali
di `deck`. Per i repo di `svezia` (`bi`, `crm`, `baserow`, `danea-auto`) il
checkout locale può essere indietro: aggiorna i riferimenti remoti con
`git -C /home/stele/<repo> fetch --quiet origin` e leggi il marker con
`git -C /home/stele/<repo> show origin/main:i3/allineamento-metodo.md`, senza
toccare il working tree. `ssh` non è concesso; se il fetch fallisce, dichiara
il limite senza dedurre uno stato che il checkout non mostra.

Lo stato dei giri autonomi sta in `i1/giri/` del repo quando il repo lo
dichiara (campo `giri` in `o3/cicli.nix` di `nixos`; `method` dal 2026-10-19),
altrimenti in `~/.local/state/ciclo/<repo>/`: `tentativi.jsonl` e
`ultimo.json`, da leggere con il tool Read: esito, commit, push e dinieghi. La riga `chiusura` porta
`oggetto` (prima riga del commit del giro, o null) e `dinieghi` (lista di
`{tool, input}`, input troncato), oltre al conteggio `permission_denials`;
le chiusure scritte da `ciclo-namespace` e quelle anteriori al 2026-10-19
non hanno i due campi. I trascritti `giri/*.jsonl` degli adottanti restano
fuori, perché portano i dati di `salute` ed `economia`; quelli di `method` in
`i1/giri/` si aprono solo per il dettaglio di una riga di `tentativi.jsonl`, e
una frizione che deve durare diventa una cattura `.md` versionata in `i1/`
(`kb/perceive.md`). Il gradino di un adottante si verifica nel suo
`autonomy.md` e nel suo prompt del ciclo (`o3/ciclo/prompt.md`, o
`.claude/ciclo-prompt.md` finché non ha migrato).

## Host e verifiche

L'host è `deck`, il checkout servito: il commit ripubblica le viste di
`method` in LAN. Verifiche: `python3 o3/view/build.py --check` sempre,
`python3 o3/kb_tools.py audit` con modifiche a `kb/`.
