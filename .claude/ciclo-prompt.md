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
permessi sono quelli di `.claude/ciclo.json`.

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
di `deck`: quelli dei repo di `svezia` possono essere indietro rispetto a
`origin`, e `ssh` non è concesso. Dichiara il limite, senza dedurre uno stato
che il checkout non mostra.

Dei repo con ciclo autonomo su `deck` (`salute`, `economia`, `nixos`) leggi
i soli `~/.local/state/ciclo/<repo>/tentativi.jsonl`, con il tool Read: esito,
commit, push e dinieghi dei giri del giorno. I trascritti in `giri/` restano
fuori, perché portano i dati di `salute` ed `economia`.

## Host e verifiche

L'host è `deck`, il checkout servito: il commit ripubblica le viste di
`method` in LAN. Verifiche: `python3 o3/view/build.py --check` sempre,
`python3 o3/kb_tools.py audit` con modifiche a `kb/`.
