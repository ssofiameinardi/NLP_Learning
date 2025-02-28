import spacy
from spacy.language import Language
# Crea el objeto nlp
nlp = spacy.load("es_core_news_sm")

# Define un componente personalizado
@Language.component("custom_component")
def custom_component_function(doc):
    # Imprime la longitud del doc en pantalla
    print("longitud del Doc:", len(doc))
    # Devuelve el objeto doc
    return doc

# Añade el componente al primer lugar del pipeline
nlp.add_pipe("custom_component", first=True)

# Imprime los nombres de los componentes del pipeline
print("Pipeline:", nlp.pipe_names)


#**********************************************************************

# Crea el objeto nlp
nlp = spacy.load("es_core_news_sm")

# Define un componente personalizado
@Language.component("custom_component")
def custom_component_function(doc):
    # Imprime la longitud del doc en pantalla
    print("longitud del Doc:", len(doc))
    # Devuelve el objeto doc
    return doc

# Añade el componente al primer lugar del pipeline
nlp.add_pipe("custom_component", first=True)

# Procesa un texto
doc = nlp("¡Hola Mundo!")

