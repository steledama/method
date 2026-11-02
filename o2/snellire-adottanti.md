---
sintesi: "Snellire /adottanti: tenere solo ciò che si vede da un repository all'altro, con la parte meccanica in o3/adottanti.py audit e il giudizio sul campione di decisioni. Adottata dal custode il 2026-11-02 e implementata lo stesso giorno; prova all'audit del 2026-12-01. Resta da decidere se lo script entra nel giro autonomo."
ciclo: dev
decidere: "Il giro autonomo lancia o3/adottanti.py audit il 1° del mese, lasciando al custode solo il giudizio?"
---

# Snellire `/adottanti`

## Origine

Nasce il 2026-11-02 dal quinto audit, su richiesta del custode, che lo ha
trovato poco utile. Quell'audit ha richiesto un pomeriggio e ha riscritto il
filo `i3/audit-adottanti.md` per circa 430 righe. Le cose che ha trovato e
che nessun altro controllo vedeva sono tutte trasversali:

- `o3/prescrizioni.py` non riconosceva tre prescrizioni recepite da tutti,
  quindi il giro non le avrebbe mai chiuse;
- due casi della delega di `danea-auto` erano fermi a «da inoltrare» da due
  settimane;
- la vista di `danea2` non era mai stata verificata da `deck`;
- in `bi`, un commit su un hook di produzione dichiarava un impatto più
  basso di quello che si legge nella fonte.

Il resto ha ripetuto ciò che i giri giornalieri e i `/method` locali già
coprono:

- **marker e prescrizioni**: coincidono coi file da quattro audit di fila;
- **composizione delle code**: `kb/development-goal.md` la chiama un indizio
  candidato che non basta a misurare la maturità, e la coda è dominio
  dell'adottante;
- **conteggio `Esiti:` per la clausola delle skill per arco**: è consumato
  dal verdetto del 2026-11-02.

## La proposta

Adottata dal custode il 2026-11-02, soglie comprese. Implementata lo stesso
giorno: sottocomando `audit` in `o3/adottanti.py` con i test, skill
riscritta in tre passi e indirizzo `host:porta` di ogni vista in `world.md`.
Il primo rapporto ha richiesto un minuto, con tre rossi, uno dei quali falso
(una prescrizione «in corso» trattata come scarto, corretta subito).

L'audit risponde a una sola domanda: **che cosa si vede solo guardando i
repository insieme?** Ogni passo sotto o è meccanico, e allora lo fa uno
script, o richiede giudizio, e allora resta in sessione.

**Parte meccanica**, un sottocomando `o3/adottanti.py audit` in sola
lettura, dopo il `fetch`. Stampa un rapporto i1 su stdout e non scrive file:

1. **canale**: per adottante, `method_commit`, `status` e il ritardo in
   commit verso HEAD. Segnala in rosso solo `action-required` o un ritardo
   che contiene commit su `kb/`, `o3/` o skill canoniche più vecchi di 14
   giorni;
2. **prescrizioni aperte**: `prescrizioni.py verifica` su ognuna. Uno
   scarto fra lo strumento e il marker è un difetto dello strumento o della
   forma, ed è la lente che ha trovato il problema di novembre;
3. **viste**: per i sette, build con `--check` sull'estrazione di `origin`,
   `/_stato` contro `origin/main` e raggiungibilità della porta. Host e
   porte arrivano da `world.md` e dal registro `presentations.nix` di
   `nixos`. Hash uguali non provano il rendering, e la verifica continua a
   dirlo;
4. **accenti**: `project.py` contro la copia in `world.md`, più l'unicità
   sull'insieme;
5. **skill**: quartetto, `/cycle` e `/method` presenti, wrapper Codex
   speculari e nessun residuo;
6. **casi fermi**: le catture «da inoltrare» più vecchie di 7 giorni, con la
   verifica che `method/i1/` non le abbia già;
7. **due numeri per adottante**, al posto della fotografia delle code: righe
   `dev`/`runtime` del plan e giri con `Impatto-motivo: ciclo-autonomo` nel
   mese. Sono dati, senza lettura narrativa.

**Parte di giudizio**, in sessione col custode:

- il **campione di decisioni** (passo 5b di oggi): una decisione
  `Autonomia: agente` per adottante, letta contro il diff e non solo contro
  il motivo. È l'unica parte che uno script non sostituisce;
- la **lettura dei rossi** del rapporto: ognuno si classifica come
  prescrizione o3, segnale i1 o niente, come oggi.

**Filo**: `i3/audit-adottanti.md` diventa breve, al massimo una schermata.
Contiene i rossi aperti con la loro classificazione, l'esito del campione e
i limiti. Le fotografie per adottante e la storia restano in git e nel
rapporto, non nel filo.

## Cosa cambia nei file

- `.claude/skills/adottanti/SKILL.md`: la procedura scende da sette passi a
  tre (lancia lo script, leggi i rossi e il campione, aggiorna il filo e la
  scadenza). Il wrapper Codex resta com'è;
- `o3/adottanti.py`: il sottocomando `audit`, con i test in
  `tests/test_adottanti.py`;
- `i3/audit-adottanti.md`: riscritto nella forma breve al primo audit
  snellito;
- `o1/plan.md`, `## Scadenze`: la riga mensile resta.

Nessun nodo `kb/` cambia, e gli adottanti non sono toccati: `/adottanti`
è una skill di dominio di `metodo`.

## Da decidere

- **lo script nel giro**: con la parte meccanica in sola lettura, il giro
  autonomo potrebbe lanciare `o3/adottanti.py audit` il 1° del mese e
  lasciare al custode solo il campione. Toglierebbe il ritardo di questo
  audit, perché la cella runtime-o1 è ferma a D proprio perché manca un
  innesco. Servono tre modifiche: la frase di `autonomy.md` per cui
  `/adottanti` non gira nel giro, il permesso in `o3/ciclo/permessi.json` e
  il passo nel prompt. Il rapporto dura circa un minuto e raggiunge `svezia`
  e `danea2` in rete.

## Criterio di chiusura

Il task si consuma all'audit del 2026-12-01, il primo snellito: tempo
dichiarato nel resoconto, rossi utili e falsi contati, e decisione del
custode sullo script nel giro.
