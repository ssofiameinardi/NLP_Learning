import spacy
nlp = spacy.load("es_core_news_sm")

data = [
    ("Esto es un texto", {"id": 1, "numero_pagina": 15}),
    ("y otro texto", {"id": 2, "numero_pagina": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    print(doc.text, context["numero_pagina"])

#**************************************************************

from spacy.tokens import Doc

Doc.set_extension("id", default=None)
Doc.set_extension("numero_pagina", default=None)

data = [
    ("Esto es un texto", {"id": 1, "numero_pagina": 15}),
    ("y otro texto", {"id": 2, "numero_pagina": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    doc._.id = context["id"]
    doc._.numero_pagina = context["numero_pagina"]