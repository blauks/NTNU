import nltk
# the following can be of use when identifying tags:
# nltk.help.upenn_tagset()

# Let's use the familiar brown corpus to begin with. Get the POS-tagged sentences.
sents = None # TODO: tagged sentences from the brown corpus

"""
# Exercise 1 - Introduction to chunking

## 1a)
Make your own noun phrase (NP) chunker, detecting noun phrases and a clause, for which verbs (VB) are followed by a preposition (IN) and/or a noun phrase.
"""

grammar = None

# TODO: set up a parser using the grammar you defined
chunk_parser = None 

# test your parser!
test_sentence = sents[400][:10]  # just an example sentence, using the first 10 words
chunks = chunk_parser.parse(test_sentence)
print(chunks)

"""
## 1b)
Convert a POS tagged text to a list of tuples, where each tuple consists of a verb followed by a sequence of noun phrases and prepositions.
Example: “the little cat sat on the mat” becomes (‘sat’, ‘on’, ‘NP’) . . . 
"""
def chunks_to_verb_NP_tuples(tagged_sents):
    tuples = set()
    """
    iterate the trees and subtrees of your parser.
    add all chunks starting with a verb (CLAUSE) to the set of tuples
    """
    return list(tuples)

# check your output :-)
import random

vb_np = chunks_to_verb_NP_tuples(sents)
random.shuffle(vb_np)
print(vb_np[:20])

"""
## 1c)
Using the pre-annotated test set from wall street journal data (conll2000 in nltk), experiment with different grammars to get the highest possible F-measure. There is no evaluation of this task, but rather a motivator to learn something about grammars.
"""
wsj = nltk.corpus.conll2000
test_sents = wsj.chunked_sents('test.txt', chunk_types=['NP'])

chunk_parser = None #TODO: your parser
print(chunk_parser.accuracy(test_sents))