# La función getter solo es llamada cuando consultas el atributo. Esto te permite calcular el valor dinámicamente, e inclusive puede tener 
# en cuenta otros atributos personalizados.
# Las funciones getter toman un argumento: el objeto, en este caso el token. En este ejemplo, la función devuelve si el texto de 
# un token se encuentra en nuestra lista de colores.
# Podemos proveer la función mediante el argumento keyword getter cuando registramos la extensión
# Las extensiones de Span casi siempre deben usar un getter, ya que los spans no tienen atributos propios.


import spacy
from spacy.tokens import Token
from spacy.tokens import Span

# Define la función getter
def get_is_color(token):
    colors = ["rojo", "amarillo", "azul"]
    return token.text in colors

# Añade una extensión en el Token con getter
Token.set_extension("is_color", getter=get_is_color)

doc = nlp("El cielo es azul.")
print(doc[3]._.is_color, "-", doc[3].text)


# Respuesta: True - azul

def get_has_color(span):
    colors = ["rojo", "amarillo", "azul"]
    return any(token.text in colors for token in span)

# Añade una extensión en el Span con getter
Span.set_extension("has_color", getter=get_has_color)

doc = nlp("El cielo es azul.")
print(doc[1:4]._.has_color, "-", doc[1:4].text)
print(doc[0:2]._.has_color, "-", doc[0:2].text)