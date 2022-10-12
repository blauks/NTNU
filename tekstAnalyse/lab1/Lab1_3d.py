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

print(nltk.FreqDist(allTextBodyWords).most_common(10))