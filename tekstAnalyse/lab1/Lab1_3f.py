import nltk
import json

file = open("corpus.json", "r")
corpus = json.loads(file.read())
file.close()

stopwords = []
file = open("stoppord_no.txt")
for line in file.readlines():
    stopwords.append(line.strip("\n"))
file.close()


# Clean only the attributes with real words
attributesToClean = ["textbody"]

def removePunctuation(word):
    letters = [c for c in word]
    for letter in letters:
        if not letter.isalnum():
            letters.remove(letter)
    
    return "".join(letters)

for corp in corpus["articles"]:
    for attribute in attributesToClean:
        corp[attribute] = [removePunctuation(w) for w in corp[attribute].split(" ") 
                    if w.lower() not in stopwords and len(w) > 0 and not removePunctuation(w) == ""]

allTextBodyWords = []

for corp in corpus["articles"]:
    allTextBodyWords += corp["textbody"]

mostCommon = [w[0] for w in nltk.FreqDist(allTextBodyWords).most_common(50)]

bestHeadline = ("", 0)

for corp in corpus["articles"]:
    score = 0
    for word in corp["headline"].split(" "):
        if word in mostCommon:
            score += 1
    
    if score > bestHeadline[1]:
        bestHeadline = (corp["headline"], score)
    
    score = 0

print(bestHeadline)
