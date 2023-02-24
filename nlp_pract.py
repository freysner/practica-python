#procesamiento en lenguaje natural con TextBlob
from textblob import TextBlob

#frase en ingles
text='Today is beatiful day. Tomorrow looks like bad weather.'
#creamos el objetoTextBlob
blob=TextBlob(text)
print(blob.words) #palabras de la frase
print(blob.sentences) #sentencias de la frase
#traducción al españo
spanish = blob.translate(from_lang='en',to='es')
print(spanish)
