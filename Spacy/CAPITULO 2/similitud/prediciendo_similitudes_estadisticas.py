import spacy
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_md")

matcher = Matcher(nlp.vocab)
matcher.add("PERRO", [[{"LOWER": "labrador"}, {"LOWER": "dorado"}]])
doc = nlp("Tengo un labrador dorado")

for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print("span encontrado:", span.text)
    # Obtén el token raíz del span y el token raíz cabeza (head)
    print("Token raíz:", span.root.text)
    print("Token raíz cabeza:", span.root.head.text)
    # Obtén el token anterior y su POS tag
    print("Token anterior:", doc[start - 1].text, doc[start - 1].pos_)