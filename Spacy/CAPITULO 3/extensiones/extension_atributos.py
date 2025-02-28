import spacy
from spacy.tokens import Token

# Añade una extensión en el Token con un valor por defecto
Token.set_extension("is_color", default=False)

doc = nlp("El cielo es azul.")

# Sobrescribe el valor de la extensión de atributo
doc[3]._.is_color = True
