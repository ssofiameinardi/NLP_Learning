import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
import json

with open("exercises/es/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())
with open("exercises/es/country_text.txt", encoding="utf8") as f:
    TEXT = f.read()

nlp = spacy.load("es_core_news_sm")
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# Crea un doc y restablece las entidades existentes
doc = nlp(TEXT)
doc.ents = []

# Itera sobre los resultados
for match_id, start, end in matcher(doc):
    # Crea un Span con la etiqueta para "LOC"
    span = Span(doc, start, end, label="LOC")

    # Sobrescribe el doc.ents y añade el span
    doc.ents = list(doc.ents) + [span]

    # Obtén el token cabeza de la raíz del span
    span_root_head = span.root.head
    # Imprime en pantalla el texto del token cabeza de
    # la raíz del span y el texto del span
    print(span_root_head.text, "-->", span.text)

# Imprime en pantalla las entidades del documento
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "LOC"])

#RESPUESTA:
# Brasil --> Brasil
# Brasil --> Alemania
# Brasil --> India
#Brasil --> Japón
#segundos --> Japón
#Japón --> Alemania
#dos --> Brasil
#Brasil --> India
#incluir --> Brasil
#Brasil --> Alemania
#Brasil --> India
#Brasil --> Japón
#habitualmente --> Egipto
#Egipto --> Nigeria
#apoyado --> Estados Unidos
#membresía --> Japón
#apoyo --> India
#apoyan --> Reino Unido
#Reino --> Francia
#acceso --> Alemania
#Alemania --> Brasil
#Alemania --> India
#Alemania --> Japón
#apoyado --> China
#membresía --> Japón
#puja --> India
#apoyo --> Francia
#Francia --> Rusia
#Francia --> Reino Unido
#Francia --> Estados Unidos
#adquirido --> India
#expresó --> China
#expresado --> China
#candidatura --> India
#revoca --> India
#[('Brasil', 'LOC'), ('Alemania', 'LOC'), ('India', 'LOC'), ('Japón', 'LOC'), ('Japón', 'LOC'), ('Alemania', 'LOC'), 
# ('Brasil', 'LOC'), ('India', 'LOC'), ('Brasil', 'LOC'), ('Alemania', 'LOC'), ('India', 'LOC'), ('Japón', 'LOC'), ('Egipto', 'LOC'),
# ('Nigeria', 'LOC'), ('Estados Unidos', 'LOC'), ('Japón', 'LOC'), ('India', 'LOC'), ('Reino Unido', 'LOC'), ('Francia', 'LOC'), 
# ('Alemania', 'LOC'), ('Brasil', 'LOC'), ('India', 'LOC'), ('Japón', 'LOC'), ('China', 'LOC'), ('Japón', 'LOC'), ('India', 'LOC'),
# ('Francia', 'LOC'), ('Rusia', 'LOC'), ('Reino Unido', 'LOC'), ('Estados Unidos', 'LOC'), ('India', 'LOC'),
# ('China', 'LOC'), ('China', 'LOC'), ('India', 'LOC'), ('India', 'LOC')]