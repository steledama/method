"""Regressioni di fedeltà delle viste: gerarchia e destinazioni dei link.

Usa Pandoc come la build; eseguire con python3 -m unittest discover -s tests.
"""

import importlib.util
import unittest
from html.parser import HTMLParser
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "build_lists", Path(__file__).resolve().parents[1] / "o3" / "build_lists.py"
)
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
        rendered = Elements(MODULE.render_markdown(source, "../i1/"))
        self.assertIn((("ul", "li", "ul", "li"), "Figlio"), rendered.text)
        self.assertIn((("h3",), "Dettagli"), rendered.text)
        self.assertIn((("ol", "li"), "Primo"), rendered.text)
        self.assertIn((("h2",), "Ultima sezione"), rendered.text)
        self.assertEqual(rendered.text[-1], (("p",), "Conclusione."))
        self.assertFalse(any("h1" in tags for tags, _ in rendered.text))

    def test_reference_links_images_queries_and_code(self):
        source = """# Indice

[Locale][ref] [Web](https://example.org/a?x=1&y=2) [Ancora](#dettagli)
[Mail](mailto:utente@example.org) [Assoluto](/file)
![Figura](immagini/schema.png)

[ref]: ../kb/node.md?x=1&y=2#forma

```markdown
## Non è una sezione
[Letterale](../kb/node.md)
```
"""
        html = MODULE.render_markdown(source, "../i1/")
        parsed = Elements(html)
        for tag, key, target in [
            ("a", "href", "../kb/node.md?x=1&y=2#forma"),
            ("a", "href", "https://example.org/a?x=1&y=2"),
            ("a", "href", "#dettagli"),
            ("a", "href", "mailto:utente@example.org"),
            ("a", "href", "/file"),
            ("img", "src", "../i1/immagini/schema.png"),
        ]:
            self.assertIn((tag, key, target), parsed.targets)
        self.assertFalse(any(tags == ("h2",) for tags, _ in parsed.text))
        self.assertEqual(html, MODULE.render_markdown(source, "../i1/"))


if __name__ == "__main__":
    unittest.main()
