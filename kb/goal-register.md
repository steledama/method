---
stato: maturo
---

# Goal register

`goal.md` rende indirizzabile il polo superiore del ciclo: motivo,
obiettivi e puntatori ai segnali che li misurano. È un register versionato
di root, gemello di `world.md`. Conserva il nord; lo stato corrente vive
nelle rappresentazioni che il register rende raggiungibili.

L'intro, dall'H1 al primo H2, è il polo in sintesi che la home deriva senza
euristiche. Le sezioni successive articolano gli obiettivi runtime e il Goal
di sviluppo. Il motivo resta del custode: gli agenti possono proporre uno
scostamento, ma non riscrivere autonomamente il nord.

Ogni obiettivo dichiara almeno un segnale vivo — filo `i3/`, audit, report o
vista — come puntatore alla fonte, oppure un buco di misura esplicito. Il
puntatore dice dove verificare l'obiettivo, senza ricopiarne l'ultimo esito.
Soglie e criteri desiderati fanno parte del nord; una misura osservata è
invece stato. Un buco di misura dichiarato rende visibile una mancanza di
copertura, senza introdurre una cronaca del monitoraggio.

Lo stato del lavoro resta nel filo `i3/` e nella coda `o1/plan.md`, con il
contesto operativo in `o2/`. Etichette come «a regime», fronti aperti,
recepimenti e avanzamenti non si ricopiano nel Goal. Le misure ad alto churn
restano nella fonte, per esempio log o export; una vista le deriva quando
possibile. Le decisioni prese su quelle misure restano versionate, con
provenienza sufficiente a ricostruirle (`verdict`).

La direzione task→obiettivo vive nella colonna `Ob.` di `o1/plan.md`: numero
stabile dell'obiettivo runtime oppure `S` per il Goal di sviluppo. La sezione
Goal di sviluppo dichiara la posizione auspicata lungo le dimensioni comuni
(`development-goal`); la fotografia attuale e lo scarto dal nord si leggono
nei suoi segnali. La coppia `exec`/`eval` controlla i due versi della
cerniera: task→obiettivo e obiettivo→segnale.

Il contenuto degli obiettivi cambia quando il custode cambia il nord; i
puntatori cambiano quando si spostano i segnali. Correggere un collegamento
non equivale a cambiare uno scopo: l'autorità per farlo segue il perimetro
concesso (`consent`). Questa distinzione non assegna nuovi permessi.

Prima di togliere una fotografia dal register, confrontarla con la
rappresentazione di destinazione: se porta il fatto più fresco, fonderlo
lì. Preservare chiavi, soglie desiderate, segnali e lettori, comprese le
viste; evitare che la rimozione di una copia perda l'unica evidenza.

Connessioni:

- [goal](goal.md)
- [world-register](world-register.md)
- [development-goal](development-goal.md)
- [plan](plan.md)
- [verdict](verdict.md)
- [skill](skill.md)
- [project-structure](project-structure.md)
- [consent](consent.md)
