# Reescribe el código y usa los atributos nativos de los tokens en vez de listas de token_texts y pos_tags.
# Has un loop sobre cada token en el doc y revisa el atributo token.pos_.
# Usa doc[token.i + 1] para revisar el token siguiente y su atributo .pos_.
# Si encuentras un nombre propio antes de un verbo imprime en pantalla su token.text.

# MALA PRACTICA:
    
import spacy

nlp = spacy.load("es_core_news_sm")
doc = nlp("Por Berlín fluye el río Esprea.")

# Obtén todos los tokens y los part-of-speech tags
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # Revisa si el token actual es un nombre propio
    if pos == "PROPN":
        # Revisa si el siguiente token es un verbo
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Encontré un nombre propio antes de un verbo:", result)
            
# BUENA PRACTICA:
import spacy

nlp = spacy.load("es_core_news_sm")
doc = nlp("Por Berlín fluye el río Esprea.")

# Itera sobre los tokens
for token in doc:
    # Revisa si el token actual es un nombre propio
    if token.pos_ == "PROPN":
        # Revisa si el siguiente token es un verbo
        if doc[token.i + 1].pos_ == "VERB":
            print("Encontré un nombre propio antes de un verbo:", token.text)