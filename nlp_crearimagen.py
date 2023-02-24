#procesamiento en lenguaje natural con TextBlob
from textblob import TextBlob
#para leer un archivo
from pathlib import Path

texto=Path('RomeoAndJuliet.txt').read_text()
blob = TextBlob(texto)
print( blob.word_counts['romeo'])
print( blob.word_counts['juliet'])

#crear una mascara de imagen
import imageio.v3 as iio
mask_image = iio.imread('mask_heart.png')

#para crear la nube de palabras
from wordcloud import WordCloud 
wordcloud = WordCloud(colormap='prism', mask=mask_image, background_color='white')

wordcloud = wordcloud.generate(texto)
wordcloud = wordcloud.to_file('RomeoAndJulietHeart.png')
