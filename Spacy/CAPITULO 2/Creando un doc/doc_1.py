# Crea un objeto nlp
import spacy
nlp = spacy.blank("es")

# Importa la clase Doc
from spacy.tokens import Doc

# Las palabras y espacios que usaremos para crear el doc
words = ["Hola", ",", "me", "llamo", "Sofia", "."]
spaces = [False, True, True, True, False, False]

# Crea un doc manualmente
doc = Doc(nlp.vocab, words=words, spaces=spaces)

print(doc.text)