import spacy

nlp = spacy.load("es_core_news_sm")

doc = nlp("El perro corre por el parque")

for token in doc:
    print(token.text, token.pos_)   # token.pos_ muestra la categoría gramatical
#El DET
#perro PROPN
#corre VERB
#por ADP
#el DET
#parque NOUN
    
    
for token in doc:
    print(token.text, token.lemma_)  # token.lemma_ muestra la forma base de la palabra
# El el
# perro perro
# corre correr
# por por
# el el
# parque parque

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)  # token.dep_ muestra la relación sintáctica con el token.head.text
# El DET det perro
# perro PROPN nsubj corre
# corre VERB ROOT corre
# por ADP case parque
# el DET det parque
# parque NOUN obl corre #


#*******************************************************************************************************************************************#

doc2 = nlp("Apple es la marca que màs satisfacciòn genera en EE.UU, pero el iphone fue superado por el Galaxy Note 9")

for ent in doc2.ents:
    print(ent.text, ent.label_)  # ent.label_ muestra la categoría de la entidad
# Apple ORG
# EE.UU LOC 
# Galaxy Note 9 MISC (Categoria miscelanea)

#*******************************************************************************************************************************************#

text = (
    "De acuerdo con la revista Fortune, Apple fue la empresa "
    "más admirada en el mundo entre 2008 y 2012."
)

# Procesa el texto
doc = nlp(text)

for token in doc:
    # Obtén el texto del token, el part-of-speech tag y el dependency label
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    # Esto es solo por formato
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")

# De          ADP       case      
#acuerdo     NOUN      fixed     
#con         ADP       fixed     
#la          DET       det       
#revista     NOUN      obl       
#Fortune     PROPN     appos     
#,           PUNCT     punct     
#Apple       PROPN     nsubj     
#fue         AUX       cop       
#la          DET       det       
#empresa     NOUN      ROOT      
#más         ADV       advmod    
#admirada    ADJ       amod      
#en          ADP       case      
#el          DET       det       
#mundo       NOUN      obl       
#entre       ADP       case      
#2008        NOUN      nmod      
#y           CCONJ     cc        
#2012        NOUN      conj      
#.           PUNCT     punct 

#*******************************************************************************************************************************************#

