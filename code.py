# Importation des bibliothèques nécessaires
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Chargement des données depuis le fichier CSV
data = pd.read_csv("Word Cloud\datasheet.csv")

# Préparation du texte pour le nuage de mots
text = " ".join(i for i in data.text)

# Définition des mots vides (stopwords)
stopwords = set(STOPWORDS)

# Génération du nuage de mots
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

# Affichage du nuage de mots
plt.figure( figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()