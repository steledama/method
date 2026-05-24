---
data: 2026-05-24
stato: aperto
---

# Confronto skill audit-kb e commit cross-repo

Le skill `audit-kb` e `commit` esistono in tutti i repo adottanti ma con implementazioni divergenti. Non è chiaro quanta divergenza sia configurazione locale legittima e quanta sia drift dal metodo.

## Azione

- leggere le skill `audit-kb` e `commit` di nixos, bi, economia, salute
- confrontare struttura, invocazione di `kb_tools.py`, comportamento di default e differenze
- classificare ogni differenza: configurazione locale (legittima) / estensione portabile (va nel metodo) / drift (da riportare al template)
- aggiornare `kb/skill.md` con la classificazione e le conclusioni

## Criterio di chiusura

`kb/skill.md` ha una sezione con la classificazione porta/locale/drift per `audit-kb` e `commit`. Le estensioni portabili identificate producono eventualmente task separati di implementazione.
