---
ciclo: runtime
---

# Segnale: la sezione cause del plan diventa una seconda fonte di verità

Data: 2026-07-28 · Fonte: custode, su esperienza `economia` (potatura della
sezione «cause delle attese e delle pause» di `o1/plan.md`, cresciuta a 78
righe su 179)

## Il segnale

In `economia` la sezione delle cause aveva raggiunto il 44% del file. Il
custode l'ha percepita come «fuori controllo» e sospetta di essere davanti a
una seconda fonte di verità sullo stato dei task, accanto ai file `o2/`.
Sintomi osservati misurando, non a impressione:

- **duplicazione viva**: nella stessa sessione lo stesso fatto è stato scritto
  in tre posti — nodo KB (dominio), file task `o2/` (stato del task) e bullet
  del plan (copia). Due dei tre sono legittimi;
- **la sezione ha sforato il proprio titolo**: tre bullet su dieci
  riguardavano task marcati `—`, cioè senza blocco: né attese né pause. Il
  criterio era scivolato da «perché è fermo» a «note su ogni task»;
- **ordine divergente**: la tabella è ordinata per imminenza della prossima
  mossa, i bullet no; i due ordini avevano divergito senza che nessuno se ne
  accorgesse;
- **importi duplicati**: un solo bullet portava sette cifre negoziali che
  vivono nel file task e cambiano a ogni scambio con la controparte;
- **la colonna `Dip.` contraddiceva il proprio bullet**: un task marcato `—`
  il cui bullet descriveva un'attesa altrui.

Due osservazioni emerse **facendo** la potatura, non prevedibili prima:

- **la direzione del drift non era uniforme**. L'assunzione naturale è che il
  plan sia la copia stale; in due casi su otto era il contrario — il plan
  portava il fatto più recente e contraddiceva il file task. Potare senza
  guardare avrebbe distrutto informazione;
- **la dottrina esisteva già e non era mai stata eseguita**. Il passo 4 di
  `verdicts-review` dice da sempre che il plan è coda pura e che le cause che
  sono narrativa di stato migrano nel filo o nel task. La regola era scritta,
  condivisa e inapplicata.

Risoluzione locale adottata (fatto, non prescrizione): budget di tre righe per
voce — causa, risveglio, puntatore a `o2/` — solo per i task non-`—`, in ordine
di tabella; da 78 righe a 38. La regola è stata scritta sia nella skill locale
sia in `CLAUDE.md`, perché la skill gira solo se invocata mentre `CLAUDE.md` è
caricato a ogni sessione.

## Domande per i2 (nessun verdetto qui, i1 è valenza-neutro)

- una regola di consolidamento senza **soglia misurabile** è eseguibile? Il
  caso suggerisce che «migra il dettaglio altrove» resti dormiente finché non
  acquista un numero, ma il campione è uno;
- «tre righe» è una soglia portabile o un numero tarato su `economia` (15 task
  aperti, contro i 2 del canone)? Se portabile, è una soglia o un rapporto
  rispetto alla dimensione della tabella?
- la dottrina appartiene al nodo [plan](../kb/plan.md), con le skill che si
  limitano a farla rispettare, o è già lì e manca solo la parte operativa?
- «verifica in che direzione punta il drift prima di potare» vale solo qui o è
  un corollario di ogni istruzione di potatura e consolidamento del metodo,
  incluse quelle su `## Scadenze`, sui fili `i3/` e sulle prescrizioni `o3/`?
- quando un artefatto porta **sia una struttura sia una prosa** sugli stessi
  item (tabella + cause, indice + note), la coerenza tra i due va controllata
  esplicitamente? Il caso mostra che divergono in silenzio;
- il ritardo di ritorno del canone verso i fork (qui: sedici giorni perché il
  protocollo post-evento, nato in `economia`, rientrasse nel suo fork) è un
  costo accettato del modello o un segnale a sé?
