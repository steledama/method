---
stato: bozza
---

# Perceive (i1)

Perceive cattura ciò che arriva dal Mondo prima di interpretarlo. Il segnale può
essere feedback a un atto oppure un evento esogeno. La registrazione è
goal-guidata nella rilevanza ma neutra nella valenza: selezionare cosa osservare
non autorizza ancora a dire se sia buono, cattivo o vero.

La cattura persistente è on-demand. Se la fonte resta accessibile e precisa non
serve duplicarla; `i1/` conserva solo materiale effimero o segnali che
richiedono un riflesso stabile. Quando il segnale è stato interpretato e il suo
contenuto è risalito, la copia consumata si elimina dall'indice e dalla
collezione.

Il grezzo che serve alla percezione ma non va versionato può stare in `i1/`,
ignorato da git: snapshot di feed, code di elaborazione, log, trascrizioni dei
giri del ciclo autonomo. È locale all'host che lo produce, tenuto con una
retention, e non si pubblica: la vista serve solo i `.md` versionati. Versionata
resta la cattura filtrata, scritta on-demand quando il grezzo porta un segnale
che deve durare. La regola `.gitignore` precede la prima scrittura, perché un
file non ignorato sporca il working tree e ferma il giro successivo. Il grezzo
già persistente e raggiungibile altrove non si sposta: si sposta in `i1/` quando
lì lo raggiunge chi percepisce, per esempio il giro, che fuori dalla cartella di
lavoro non legge.

Connessioni:

- [input](input.md)
- [interpret](interpret.md)
- [world](world.md)
- [goal](goal.md)
- [source-of-truth](source-of-truth.md)
