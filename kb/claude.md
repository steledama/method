---
data: 2026-05-23
stato: bozza
---

# CLAUDE

CLAUDE.md è la costituzione operativa del progetto per gli agenti. Risponde alla domanda: come devo agire in questo repo? Contiene regole d'azione, vincoli, permessi, procedure sicure e riferimenti rapidi; non contiene conoscenza stabile del dominio.

La distinzione è essenziale. Se CLAUDE.md spiega come funziona il sistema, diventa documentazione narrativa e compete con la KB. Se invece resta costituzione operativa, può essere caricato spesso senza gonfiare il contesto e senza creare una seconda fonte di verità.

Regole:

- apre con il bootstrap di sessione esplicito: ordine di lettura README → mappa del progetto → nodo tematico → CLAUDE.md
- contiene comportamenti consentiti, proibiti o da chiedere
- include il controllo iniziale sui task aperti quando il progetto usa `plan.md` + tasks/
- nei repo adottanti, può ricordare di controllare la storia recente di `metodo`
  quando serve recepire generalizzazioni portabili, ma non deve trattare
  `../metodo/tasks/` come backlog operativo locale
- indica operativamente gli strumenti: quale usare per quale intento, con i
  comandi minimi ad alta frequenza
- può elencare i comandi quotidiani ad alta frequenza (formatter, validazione locale, entry point KB) ma rimanda alla KB per la reference completa
- rimanda ai nodi KB per architettura, procedure e spiegazioni stabili
- chiude con una tabella "Riferimenti rapidi" che mappa intenti operativi ai nodi KB
- non è fonte di fatti per audit o fedeltà cognitiva
- la dimensione è un segnale: oltre ~100 righe è probabile sovrapposizione con la KB, e il contenuto in eccesso va trasferito nei nodi tematici

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                                                                                                | Confronto con il metodo                                                                                                                          |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `nixos`    | bootstrap esplicito, permessi, validazione, formatter, vincoli e riferimenti rapidi.                                                                | Molto vicino alla teoria: file operativo, compatto e non usato come fonte di verità del dominio.                                                 |
| `bi`       | revisione completata dopo la fotografia iniziale: `CLAUDE.md` compattato e task locale di dettaglio chiuso.                                          | Sotto monitoraggio qualitativo: il criterio resta che `CLAUDE.md` deve essere costituzione operativa, non manuale di dominio.                    |
| `economia` | bootstrap con `stato.md`, `scadenze.md` e mappa, comandi, risorse esterne e riferimenti rapidi.                                                      | Buon adattamento: include vincoli di dominio e stato corrente senza trasformarsi in manuale esteso.                                              |
| `salute`   | il più esteso: project overview, filosofia, struttura, guidelines e operazioni; ora rimanda a `kb/verifica-nel-vivere.md` per il filing back.       | Eredita la fase storica del progetto: utile, ma può alleggerirsi progressivamente usando pointer verso `metodo/` e nodi locali.                  |

Il caso `bi` ha mostrato perché il metodo insiste sulla separazione tra costituzione operativa e documentazione. Più `CLAUDE.md` diventa completo, più diventa costoso da caricare e più rischia di divergere dai nodi. La regola pratica è: se un paragrafo spiega come funziona il sistema, appartiene a `kb/`; se dice cosa l'agente può o deve fare, appartiene a `CLAUDE.md`.

Per gli strumenti, CLAUDE.md è il livello operativo della tripartizione README/CLAUDE/nodi descritta in `strumenti-kb`: dice quando usare uno strumento, quali comandi minimi sono sicuri e quando leggere il nodo di dettaglio; la reference estesa resta nei nodi o negli script versionati.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [agents](agents.md)
- [readme](readme.md)
- [struttura-progetto](struttura-progetto.md)
- [skill](skill.md)
- [strumenti-kb](strumenti-kb.md)
