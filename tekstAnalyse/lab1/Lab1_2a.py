import nltk
from nltk.corpus import brown

categories = ["government", "news", "humor"]

governmentWords = brown.words(categories=categories[0])
newsWords = brown.words(categories=categories[1])
humorWords = brown.words(categories=categories[2])

governmentFD = nltk.FreqDist(governmentWords)
newsFD = nltk.FreqDist(newsWords)
humorFD = nltk.FreqDist(humorWords)

print("--- Government top 5 words ---")
print(governmentFD.most_common (5))
print("--- News top 5 words ---")
print(newsFD.most_common (5))
print("--- Humor top 5 words ---")
print(humorFD.most_common (5))