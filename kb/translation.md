---
stato: iniziale
---

# Translation

Un artefatto letto in due lingue ne tiene una sola come fonte di verità. La
lingua canonica la dichiara il README; l'altra è una copia derivata, come una
vista: fa fede il sorgente, e una differenza fra le due si risolve correggendo
la copia. Due lingue mantenute alla pari raddoppiano ogni scrittura e lasciano
senza risposta la domanda su quale delle due dica il vero.

La copia è un file gemello accanto al sorgente, con la sigla della lingua prima
dell'estensione: `node.it.md` accanto a `node.md`. La vicinanza rende visibile
quale sorgente ha la copia e quale no, e la copia non entra nell'inventario dei
nodi: non ha `stato`, non ha voce nel catalogo e si nomina col sorgente. Il suo
frontmatter porta solo `fonte:`, l'hash git del blob del sorgente da cui deriva:
un'impronta del contenuto, non una data né un commit, che resta vera anche
quando sorgente e copia cambiano nello stesso commit.

Si traduce solo la superficie letta da fuori: README, nodi e deck. Le collezioni
di lavoro, i register, le regole operative e le skill vivono nella sola lingua
canonica, perché il ciclo le riscrive a ogni giro e una copia lì raddoppierebbe
il lavoro senza un lettore che la chieda. La lingua dei file è distinta da
quella della conversazione col custode, che resta la sua.

## Allineamento

- la copia la produce l'agente dal sorgente e vi scrive `fonte:` con l'hash
  corrente (`o3/traduzioni.py fonte <file>`);
- un controllo deterministico confronta `fonte:` con l'hash del sorgente: una
  copia indietro è un ritardo dichiarato, si segnala e non ferma il commit;
- una copia senza sorgente o senza `fonte:` valida è un errore strutturale e
  ferma il commit;
- una copia mancante non si segnala: la traduzione procede a lotti, partendo
  dalla porta d'ingresso (README e hub);
- i link di una copia puntano ai gemelli quando esistono, altrimenti ai
  sorgenti.

## Adattamento al dominio

Un repository monolingue non ha gemelli e non paga nulla: il controllo trova
zero copie. La scelta della lingua canonica e del perimetro tradotto è locale
all'adottante e si dichiara nel suo README.

Connessioni:

- [view](view.md)
- [node](node.md)
- [readme](readme.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [kb-tools](kb-tools.md)
- [presentation](presentation.md)
- [project-structure](project-structure.md)
