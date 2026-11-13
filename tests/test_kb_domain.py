"""Il controllo di dominio di `method`: ogni strumento di `o3/` è nell'indice."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("kb_domain", ROOT / "o3" / "kb_domain.py")
kb_domain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb_domain)


class StrumentiRegistrati(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "o3" / "view").mkdir(parents=True)
        (self.root / "o3" / "__pycache__").mkdir()
        for nome in ("uno.py", "due.py", "kb_domain.py", "view/build.py"):
            (self.root / "o3" / nome).write_text("", encoding="utf-8")

    def indice(self, testo: str) -> list[str]:
        (self.root / "o3" / "prescriptions.md").write_text(testo, encoding="utf-8")
        return kb_domain.non_registrati(self.root)

    def test_tutti_registrati(self) -> None:
        self.assertEqual(self.indice("`uno.py` `due.py check` `view/` `build.py`"), [])

    def test_script_e_cartella_mancanti(self) -> None:
        self.assertEqual(self.indice("`uno.py` e build.py"), ["due.py", "view/build.py", "view/"])

    def test_un_nome_piu_lungo_non_vale(self) -> None:
        self.assertEqual(self.indice("`uno.py` `due.pyc` `view/` `build.py`"), ["due.py"])

    def test_il_repo_non_ha_strumenti_fuori_indice(self) -> None:
        self.assertEqual(kb_domain.audit(ROOT, None), {next(iter(kb_domain.audit(ROOT, None))): []})


if __name__ == "__main__":
    unittest.main()
