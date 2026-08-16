---
data: 2026-08-16
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, danea-auto
---

# La chiusura dei task controlla anche i documenti nel Mondo

## Cosa e perché

Il secondo segnale reale ha esteso il criterio «significato senza artefatto»
alla chiusura dei task. In `salute`, chiuso il task per un incontro medico, il
PDF operativo era rimasto in `gdrive/varie/` benché decisioni ed esiti fossero
già risaliti nell'artefatto. Il canone ora stabilisce che `exec plan`, prima di
potare un task, controlli anche le sue materializzazioni note sulle superfici
dichiarate in `world.md`.

La regola distingue senza autorizzare: effetti, evidenze e fonti con significato
autonomo restano nel Mondo; copie operative consumate sono candidate alla
pulizia. Una rimozione esterna richiede target esatto e autorità esplicita.

## Ricetta di recepimento

1. Aggiorna il fork locale di `.claude/skills/exec/SKILL.md`, preservandone le
   parametrizzazioni di dominio.
2. Nello scope `plan`, accanto al controllo dei task chiusi, aggiungi
   l'enumerazione delle materializzazioni note sulle superfici dichiarate in
   `world.md`. Usa il file `o2/` e l'eventuale prescrizione `o3/` come mappa
   primaria; non introdurre una scansione indiscriminata del Mondo.
3. Classifica ciascun target col test di `method/world.md`: ciò che conserva
   significato senza l'artefatto è effetto/evidenza durevole; ciò che lo perde è
   copia operativa consumata.
4. Prima di proporre la potatura, verifica che il contenuto utile sia risalito
   nell'artefatto o resti in una fonte durevole. Senza target esatto e autorità
   esplicita, segnala la copia e fermati alla membrana.
5. Coordina il controllo con `exec perform` quando il task aveva anche una
   prescrizione `o3/`: `perform` tiene onesta la collezione, `plan` controlla i
   documenti prodotti nel Mondo.

## Chiusura

La prescrizione resta attiva finché i sei adottanti non hanno recepito il
controllo nel proprio fork di `exec` e aggiornato il marker
`i3/allineamento-metodo.md`. Adattamenti più restrittivi sulle superfici o
sull'autorità restano locali e non impediscono il recepimento.
