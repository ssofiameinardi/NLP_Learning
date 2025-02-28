import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("es_core_news_md")

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("labrador dorado")
matcher.add("PERRO", [pattern])
doc = nlp("Tengo un labrador dorado")

# Itera sobre los resultados
for match_id, start, end in matcher(doc):
    # Obtén el span resultante
    span = doc[start:end]
    print("span resultante:", span.text)