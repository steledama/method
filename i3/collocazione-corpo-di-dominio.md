---
ciclo: runtime
---

# Il corpo di dominio si colloca in `o3/`: ratifica di una riclassificazione

Il canone ha oscillato in pochi commit su dove vive il corpo di dominio di un
adottante code-based: prima «la configurazione che gira in `nixos` è
o1/runtime» (`project-structure`, sezione uniformità), poi l'inventario
dell'atrio ha introdotto una classe **corpo di dominio** che ne autorizzava la
permanenza in root purché dichiarata (`9af4093`), infine il passo 1 del pilot
ha forzato la posizione attuale: il corpo di dominio va **ricollocato in
`o3/` come o3-runtime**, e la classe che autorizzava la permanenza è abolita
(`05fb179`). Questo filo fissa il perché, che i commit da soli non dicono.

**Perché o3 e non o1.** La dichiarazione (moduli, host, client, script) non è
un piano: è ciò che **prepara e compie l'atto sul Mondo** — il rebuild/deploy
la applica, il commit agisce su di lei. È Perform, non Plan; `o1/` resta il
cruscotto del lavoro aperto. **Perché non la root:** la permanenza in root era
inerzia travestita da classe — con una classe-dispensa il verdetto di fit non
misurava niente, perché tutto ciò che non entrava diventava «corpo di dominio»
a costo zero. Abolita la dispensa, ogni eccezione pesa e il conteggio torna a
essere un verdetto onesto.

**Collaudo.** `nixos` ha eseguito la ricollocazione (`fe4c65d`: `home/`,
`hosts/`, `modules/`, `identity/`, `patches/`, `scripts/` → `o3/`, flake
aggiornato ai path nuovi) con verdetto di fit pieno, e il rebuild reale su
`deck` (2026-07-05) ha confermato che la struttura nuova regge il runtime —
non solo il grep. `economia` (`a0538f5`, 2026-07-05) è il secondo dato: un
toolchain Python con `pyproject.toml` in root ha accettato libreria, config e
test sotto `o3/` (`py_compile` pulito; `pytest` non disponibile nell'ambiente,
verifica parziale).

Claim falsificabile: la regola della collocazione piena regge finché il
toolchain non inchioda il _layout_ oltre ai singoli file. `bi` è lo
stress-test: se ricollocare `client/` e gli esecutori produce troppe eccezioni
o rompe vincoli di build (path attesi da `package.json`, convenzioni `src/`),
il verdetto non è un adattamento locale ma un limite di fit — e questo filo si
riapre. Chiude quando anche `bi` ha eseguito l'inventario senza degradare la
regola.
