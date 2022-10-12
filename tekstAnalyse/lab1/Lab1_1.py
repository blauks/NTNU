import re

words = ["further", "Forward", "Foreign", "financE", "Forgive", "feature", "federal", "failurE", "Feeling", "finding ", "freedom", "Foundry" ]

def allWordsBeginningWithFo(list):
    for word in list:
        if re.search("^fo", word, re.IGNORECASE):
            print(word)

# allWordsBeginningWithFo(words)

def allWordsEndingWithE(list):
    for word in list:
        if re.search(".*e$", word, re.IGNORECASE):
            print(word)

allWordsEndingWithE(words)