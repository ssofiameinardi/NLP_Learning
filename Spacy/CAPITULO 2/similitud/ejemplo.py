import spacy
# Carga uno de los modelos más grandes que contiene vectores
nlp = spacy.load("es_core_news_md")

# Compara dos documentos
doc1 = nlp("Me gusta la comida rápida")
doc2 = nlp("Me gusta la pizza")
print(doc1.similarity(doc2))

# Compara dos tokens
doc = nlp("Me gustan la pizza y las hamburguesas")
token1 = doc[3]
token2 = doc[6]
print(token1.similarity(token2))

# Compara un documento con un token
doc = nlp("Me gusta la pizza")
token = nlp("jabón")[0]

print(doc.similarity(token))

# Compara un span con un documento
span = nlp("Me gustan los perros calientes")[3:5]
doc = nlp("McDonalds vende hamburguesas")

print(span.similarity(doc))