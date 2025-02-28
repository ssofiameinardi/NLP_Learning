import spacy 
from spacy.tokens import Doc

# Define un método con argumentos
def has_token(doc, token_text):
    in_doc = token_text in [token.text for token in doc]
    return in_doc

# Añade una extensión en el Doc con el método
Doc.set_extension("has_token", method=has_token)

doc = nlp("El cielo es azul.")
print(doc._.has_token("azul"), "- azul")
print(doc._.has_token("nube"), "- nube")

# Respuesta: True - azul
# Respuesta: False - nube