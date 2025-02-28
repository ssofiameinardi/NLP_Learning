import spacy
# Importa las clases Doc y Span
from spacy.tokens import Doc, Span

nlp = spacy.blank("es")

# Las palabras y espacios que usaremos para crear el doc
words = ["¡", "Hola", "Mundo", "!"]
spaces = [False, True, False, False]

# Crea un doc manualmente
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# Crea un span manualmente
span = Span(doc, 1, 3)

# Crea un span con un label
span_with_label = Span(doc, 1, 3, label="SALUDO")

# Añade el span a los doc.ents
doc.ents = [span_with_label]


#Los doc.ents son escribibles así que podemos añadir entidades manualmente sobrescribiéndolos con una lista de spans.
