"""Regressioni di fedeltà delle viste: gerarchia e destinazioni dei link.

Usa Pandoc come la build; eseguire con python3 -m unittest discover -s tests.
"""

import importlib.util
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

BUILDERS = Path(__file__).resolve().parents[1] / "o3" / "presentation"
sys.path.insert(0, str(BUILDERS))
SPEC = importlib.util.spec_from_file_location("build_lists", BUILDERS / "build_lists.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class Elements(HTMLParser):
    def __init__(self, markup):
        super().__init__()
        self.stack = []
        self.text = []
        self.targets = []
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        self.targets.extend((tag, key, value) for key, value in attrs if key in {"href", "src"})
        if tag not in {"img", "br", "hr"}:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()

    def handle_data(self, data):
        if data.strip():
            self.text.append((tuple(self.stack), data.strip()))


class ListViewTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.presentation = Path(self.tmp.name)
        (self.presentation / "assets").mkdir()
        (self.presentation / "assets" / "schema.png").write_bytes(b"png")
        (self.presentation / "tasks.html").write_text("vista", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_hierarchy_and_all_sections_survive(self):
        source = """# Indice

Intro.

## Nome locale

- Padre
    - Figlio

### Dettagli

1. Primo
2. Secondo

## Ultima sezione

Conclusione.
"""
        rendered = Elements(MODULE.render_markdown(source, self.presentation))
        self.assertIn((("ul", "li", "ul", "li"), "Figlio"), rendered.text)
        self.assertIn((("h3",), "Dettagli"), rendered.text)
        self.assertIn((("ol", "li"), "Primo"), rendered.text)
        self.assertIn((("h2",), "Ultima sezione"), rendered.text)
        self.assertEqual(rendered.text[-1], (("p",), "Conclusione."))
        self.assertFalse(any("h1" in tags for tags, _ in rendered.text))

    def test_links_closed_on_presentation(self):
        source = """# Indice

[Locale][ref] [Web](https://example.org/a?x=1&y=2) [Ancora](#dettagli)
[Mail](mailto:utente@example.org) [Assoluto](/file) [Vista](tasks.html#/plan)
![Figura](assets/schema.png)

[ref]: ../kb/node.md?x=1&y=2#forma

```markdown
## Non è una sezione
[Letterale](../kb/node.md)
```
"""
        html = MODULE.render_markdown(source, self.presentation)
        parsed = Elements(html)
        for tag, key, target in [
            ("a", "href", "https://example.org/a?x=1&y=2"),
            ("a", "href", "#dettagli"),
            ("a", "href", "mailto:utente@example.org"),
            ("a", "href", "tasks.html#/plan"),
            ("img", "src", "assets/schema.png"),
        ]:
            self.assertIn((tag, key, target), parsed.targets)
        # I link alle fonti fuori dalla cartella restano solo etichetta.
        hrefs = {target for _, _, target in parsed.targets}
        self.assertNotIn("../kb/node.md?x=1&y=2#forma", hrefs)
        self.assertNotIn("/file", hrefs)
        self.assertTrue(html.startswith("<p>Locale "))
        # Il codice letterale non è un link: resta com'è nella fonte.
        self.assertIn("](../kb/node.md)", html)
        self.assertFalse(any(tags == ("h2",) for tags, _ in parsed.text))
        self.assertEqual(html, MODULE.render_markdown(source, self.presentation))

    def test_local_disk_schemes_are_not_external(self):
        # `file:` e i path Windows (`C:\\…`, schema `c:`) portano sul disco di
        # chi costruisce: non sono link esterni, restano etichetta.
        source = "# I\n\n[Disco](file:///etc/hosts) [Win](C:\\dati\\goal.md) [Web](https://x.org)\n"
        parsed = Elements(MODULE.render_markdown(source, self.presentation))
        hrefs = {target for _, _, target in parsed.targets}
        self.assertEqual(hrefs, {"https://x.org"})
        with self.assertRaises(SystemExit):
            MODULE.render_markdown("# I\n\n![F](file:///tmp/f.png)\n", self.presentation)

    def test_image_outside_presentation_breaks(self):
        with self.assertRaises(SystemExit):
            MODULE.render_markdown("# I\n\n![Figura](../i2/tavola.png)\n", self.presentation)


if __name__ == "__main__":
    unittest.main()
