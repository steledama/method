---
data: 2026-05-23
stato: bozza
---

# CLAUDE

CLAUDE.md è la costituzione operativa del progetto per gli agenti. Risponde alla domanda: come devo agire in questo repo? Contiene regole d'azione, vincoli, permessi, procedure sicure e riferimenti rapidi; non contiene conoscenza stabile del dominio.

La distinzione è essenziale. Se CLAUDE.md spiega come funziona il sistema, diventa documentazione narrativa e compete con la KB. Se invece resta costituzione operativa, può essere caricato spesso senza gonfiare il contesto e senza creare una seconda fonte di verità.

Regole:

- apre con il bootstrap di sessione
- contiene comportamenti consentiti, proibiti o da chiedere
- può elencare comandi quotidiani ad alta frequenza
- rimanda ai nodi KB per architettura, procedure e spiegazioni stabili
- non è fonte di fatti per audit o fedeltà cognitiva
- quando supera il ruolo operativo, il contenuto va trasferito nei nodi tematici

## Applicazione nei progetti adottanti

| Progetto | Situazione attuale | Confronto con il metodo |
| -------- | ------------------ | ----------------------- |
| `nixos` | 88 righe, bootstrap esplicito, permessi, validazione, formatter, vincoli e riferimenti rapidi. | Molto vicino alla teoria: file operativo, compatto e non usato come fonte di verità del dominio. |
| `bi` | 824 righe con ambiente, produzione, standard script, pattern Baserow, git, documentazione, URL e task management. | È il caso principale di drift: contiene molta conoscenza stabile che dovrebbe vivere in nodi KB o runbook, lasciando in CLAUDE solo regole d'azione e pointer. |
| `economia` | 99 righe, bootstrap con `stato.md`, `scadenze.md` e mappa, comandi, risorse esterne e riferimenti rapidi. | Buon adattamento: include vincoli di dominio e stato corrente senza trasformarsi in manuale esteso. |
| `salute` | 228 righe, project overview, filosofia, struttura, node structure, content guidelines e operazioni. | Eredita la fase storica del progetto: utile, ma contiene spiegazioni metodologiche che oggi dovrebbero essere pointer verso `metodo/` e nodi locali. |

Il caso `bi` mostra perché il metodo insiste sulla separazione tra costituzione operativa e documentazione. Più `CLAUDE.md` diventa completo, più diventa costoso da caricare e più rischia di divergere dai nodi. La regola pratica è: se un paragrafo spiega come funziona il sistema, appartiene a `kb/`; se dice cosa l'agente può o deve fare, appartiene a `CLAUDE.md`.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [agents](agents.md)
- [readme](readme.md)
- [struttura-progetto](struttura-progetto.md)
- [skill](skill.md)
