import json
import spacy

nlp = spacy.load("es_core_news_sm")

with open("exercises/es/tweets.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

#FORMA NO OPTIMA:
# Procesa los textos e imprime las entidades en pantalla
# docs = [nlp(text) for text in TEXTS]
# entities = [doc.ents for doc in docs]
# print(*entities)

#FORMA OPTIMA:
docs = list(nlp.pipe(TEXTS))
entities = [doc.ents for doc in docs]
print(*entities)