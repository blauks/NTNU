import nltk
from nltk.corpus import brown, stopwords
from nltk.text import Text

stops = stopwords.words()

newsWords = [x for x in brown.words(categories="news") 
                if x.lower() not in stops and x.isalnum()]

newsFD = nltk.FreqDist(newsWords).most_common(5)

Text(brown.words()).dispersion_plot([x[0] for x in newsFD])
