---
data: 2026-10-25
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, baserow, danea-auto
---

# Le proposte da decidere e il register della delega nella home

## Cosa e perché

Il custode deve trovare una proposta in attesa anche quando è uscita dagli
ultimi giri, e deve poter aprire da lì i criteri della delega. Fino a oggi una
proposta era un'intestazione «Da decidere» nel corpo di un task `o2/`: nessuno
strumento la trovava e niente obbligava a toglierla. In `method` l'unica
proposta così segnata (`o2/home-fatto-da-fare.md`) era già stata decisa il
2026-10-21, quattro giorni prima, e l'intestazione diceva ancora «Da decidere».

Il custode ha deciso il 2026-10-25 (`autonomy.md`, `kb/tasks.md`,
`kb/view.md`):

- una proposta persistente si dichiara col campo **`decidere:`** nel
  frontmatter del task `o2/`, con la questione in una frase; il corpo tiene
  alternative, motivo e decisione richiesta. Quando il custode decide, il campo
  si toglie e il corpo registra la decisione con la data;
- la home della vista ha una sezione **«Da decidere»** che elenca i task col
  campo, letti dalla release perché sono versionati;
- `autonomy.md` diventa una **pagina della vista**, accanto a `goal.md` e
  `world.md` ma senza polo: non è uno stadio del ciclo. La home la collega
  dalla sezione delle proposte.

## Ricetta per il /method locale

1. **Vista**: da canone `o3/view/sources.py` (campo `decidere` di
   `TaskDetail`, `pending_proposals`, etichette), `build_pages.py`
   (`REGISTERS` con `autonomy.md`), `build_system_image.py`
   (`proposals_html` in home) e i due test nuovi di
   `tests/test_build_pages.py`. `project.py` resta locale. Un repo con la home
   personalizzata colloca la sezione dove la legge il suo custode. Verifica
   con i test e `build.py --check`.
2. **Register**: in `autonomy.md`, il paragrafo sulle proposte persistenti
   («Decisioni riservate») prende la forma del campo e del suo consumo.
   È un cambio del register che il custode ratifica nel `/method` locale.
3. **Skill**: in `cycle` (passo «Durante il giro») la proposta nel task
   `o2/` si scrive col campo `decidere:`; se il prompt locale del ciclo
   autonomo descrive la forma delle proposte, allinearlo. Il nodo
   `kb/tasks.md` arriva via symlink.
4. **Proposte esistenti**: cercare nei task `o2/` intestazioni o frasi «da
   decidere». Una ancora aperta prende il campo; una già decisa perde
   l'etichetta e registra la decisione. Non decidere niente nel recepimento:
   si cambia solo la forma.
5. Registrare il recepimento nel marker `i3/allineamento-metodo.md`.

## Indizi da verificare sul posto

- **danea-auto**: il register vive anche in Windows e la vista è servita
  da `danea2`; verificare che `autonomy.md` non porti dettagli da tenere
  fuori dalla LAN prima di renderlo come pagina.
- **salute**: la vista eredita il compartimento dei dati sanitari; il
  register non ne contiene, ma una proposta `o2/` può contenerne. La questione
  in `decidere:` si scrive senza dati personali.
- **bi** e **baserow**: il checkout è anche superficie servita; la pagina
  del register segue la loro pubblicazione ordinaria.

## Verifica

`grep -l '^decidere:' o2/*.md` restituisce i task che la home elenca, e
nessun task `o2/` ha più un «da decidere» nel corpo senza il campo. La home
mostra «Da decidere» (o «Nessuna proposta in attesa di decisione.») e il
collegamento ai criteri della delega, e `autonomy.html` esiste nella vista.
