"""Identità del progetto sulle superfici della presentazione.

È l'unico file che il fork parametrizza: sigla e lingua dei titoli, colore
d'accento, sorgente del deck delle Interpretazioni. Stile, struttura delle
viste e contratti restano canone, uguali in ogni repo (`kb/presentation.md`).
"""

# Sigla del repo nei titoli delle viste: «Method Plan», «BI Piano».
SIGLA = "Method"

# Lingua dei titoli delle viste: "en" oppure "it".
LINGUA = "en"

# Colore d'accento, unico per progetto: è ciò che distingue le presentazioni.
ACCENTO = "#4338ca"

# Sorgente del deck delle Interpretazioni, relativa alla root, oppure None se
# il repo non ha un deck. Le tavole si citano come `assets/<nome>` e la loro
# fonte vive accanto al deck.
DECK: str | None = "i2/metodo-in-sintesi.md"

# CSS di dominio delle viste Reveal (diagrammi, componenti di un deck), in
# `presentation/assets/`, caricati dopo deck.css e theme.css. Vuoto se il
# deck usa solo il canone.
CSS_LOCALI: list[str] = []
