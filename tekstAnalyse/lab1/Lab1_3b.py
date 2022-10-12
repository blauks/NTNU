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
attributesToClean = ["topic", "headline", "ingress", "textbody"]

for corp in corpus["articles"]:
    for attribute in attributesToClean:
        corp[attribute] = " ".join([w for w in corp[attribute].split(" ") 
                    if w.lower() not in stopwords and w.isalnum()])

