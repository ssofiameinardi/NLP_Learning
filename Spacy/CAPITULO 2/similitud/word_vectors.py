import spacy
# Carga uno de los modelos más grandes que contiene vectores
nlp = spacy.load("es_core_news_md")

doc = nlp("Tengo una manzana")
# Accede al vector a través del atributo token.vector
print(doc[2].vector)

#La salida por consola parece una matriz
