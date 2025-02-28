import spacy

nlp = spacy.load("es_core_news_md")

doc1 = nlp("Es un cálido día de verano")
doc2 = nlp("Hay sol afuera")

# Obtén la similitud entre el doc1 y el doc2
similarity = doc1.similarity(doc2)
print(similarity)

#************************************************************************************************

doc = nlp("TV y libros")
token1, token2 = doc[0], doc[2]

# Obtén la similitud entre los tokens "TV" y "libros"
similarity = token1.similarity(token2)
print(similarity)

#************************************************************************************************

doc_span = nlp(
    "Estuvimos en un restaurante genial. Luego, fuimos a un bar muy divertido."
)

# Crea los spans para "restaurante genial" y "bar muy divertido"
span1 = doc_span[3:5]
span2 = doc_span[11:14]

# Obtén la similitud entre los dos spans
similarity = span1.similarity(span2)
print(similarity)

