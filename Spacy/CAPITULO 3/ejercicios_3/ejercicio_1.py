# Usa el método set_extension para registrar los atributos personalizados "author" y "book" en el Doc, con el valor por defecto None.
# Procesa los pares [text, context] en DATA usando nlp.pipe con as_tuples=True.
# Sobrescribe el doc._.book y doc._.author con la información respectiva pasada como el contexto.


import json
import spacy
from spacy.tokens import Doc

with open("exercises/es/bookquotes.json", encoding="utf8") as f:
    DATA = json.loads(f.read())

nlp = spacy.blank("es")

# Registra la extensión del Doc, "author" (por defecto None)
Doc.set_extension("author", default=None)

# Registra la extensión del Doc, "book" (por defecto None)
Doc.set_extension("book", default=None)

for doc, context in nlp.pipe(DATA, as_tuples=True):
    # Añade los atributos doc._.book y doc._.author desde el contexto
    doc._.book = context["book"]
    doc._.author = context["author"]

    # Imprime en pantalla el texto y los datos del atributo personalizado
    print(f"{doc.text}\n — '{doc._.book}' by {doc._.author}\n")