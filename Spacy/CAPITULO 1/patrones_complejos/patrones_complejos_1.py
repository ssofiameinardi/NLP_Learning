#Escribe un patrón que únicamente encuentre menciones de las versiones completas de iOS: “iOS 7”, “iOS 11” and “iOS 10”.

import spacy
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "Después de hacer la actualización de iOS no notarás un rediseño "
    "radical del sistema: no se compara con los cambios estéticos que "
    "tuvimos con el iOS 7. La mayoría de las funcionalidades del iOS 11 "
    "siguen iguales en el iOS 10."
)

# Escribe un patrón para las versiones de iOS completas
# ("iOS 7", "iOS 11", "iOS 10")
pattern = [{"TEXT": "iOS"}, {"IS_DIGIT": True}]

# Añade el patrón al matcher y usa el matcher sobre el documento
matcher.add("IOS_VERSION_PATTERN", [pattern])
matches = matcher(doc)
print("Total matches found:", len(matches))

# Itera sobre los resultados e imprime el texto del span
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)