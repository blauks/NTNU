import nltk
from nltk.corpus import brown, stopwords

categories = ["government", "news", "humor"]

stops = stopwords.words()

governmentWords = [x for x in brown.words(categories=categories[0]) 
                    if x not in stops]
newsWords = [x for x in brown.words(categories=categories[1]) 
                if x not in stops]
humorWords = [x for x in brown.words(categories=categories[2]) 
                if x not in stops]

governmentFD = nltk.FreqDist(governmentWords)
newsFD = nltk.FreqDist(newsWords)
humorFD = nltk.FreqDist(humorWords)

print("--- Government top 5 words ---")
print(governmentFD.most_common(5))

print("--- News top 5 words ---")
print(newsFD.most_common(5))

print("--- Humor top 5 words ---")
print(humorFD.most_common(5))
