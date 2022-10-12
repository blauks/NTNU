"""
## Exercise 3 - Word features
Word features can be very useful for performing document classification, since the words that appear in a document give a strong indication of what its semantic content is. However, many words occur very infrequently, and some of the most informative words in a document may never have occurred in our training data. One solution is to make use of a lexicon, which describes how different words relate to each other.

Your task:
- Use the WordNet lexicon and augment the movie review document classifier (See NLTK book, Ch. 6, section 1.3) to use features that generalize the words that appear in a document, making it more likely that they will match words found in the training data.
"""
import nltk
from sklearn.model_selection import train_test_split

nltk.download('wordnet')
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
import random

# TODO: implement 
def word_to_syn(word) -> list:
    pass

"""
this is from Ch. 6, sec. 1.3, with slight modifications
note that word_to_syn(word) (from the above implementation)
is in the beginning of the following function
"""
documents = [([word_to_syn(word) for word in list(movie_reviews.words(fileid))], category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
n_most_freq = 2000
word_features = list(all_words)[:n_most_freq]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

""" end nltk snippets """

featuresets = [(document_features(d), c) for (d, c) in documents]

split_ratio = 0.01 # TODO: modify
train_set, test_set = train_test_split(featuresets, test_size=split_ratio)

# TODO: select a suitable classifier
classifier = None
model = classifier.train(train_set)

# TODO: return a flattened list of input words and their lemmas
def synset_expansion(words) -> list:
    pass

expanded_word_features = synset_expansion(word_features)

# some assertions to test your code :-)
assert sorted(synset_expansion(["pc"])) == ["microcomputer", "pc", "personal_computer"]
assert sorted(synset_expansion(["programming", "coder"])) == [
    'coder',
    'computer_programing',
    'computer_programmer',
    'computer_programming',
    'program',
    'programing',
    'programme',
    'programmer',
    'programming',
    'scheduling',
    'software_engineer'
]

doc_featuresets = [(document_features(d), c) for (d, c) in documents]
doc_train_set, doc_test_set = train_test_split(doc_featuresets, test_size=0.1)

doc_model = model.train(doc_train_set)
doc_model.show_most_informative_features(5)
print("Accuracy: ", nltk.classify.accuracy(doc_model, doc_test_set))

def lexicon_features(reviews):
    review_words = set(reviews)
    features = {}
    for word in expanded_word_features:
        if word not in word_features:
            features['synset({})'.format(word)] = (word in review_words)
        features['contains({})'.format(word)] = (word in review_words)

    return features

"""
Question: do you see any issues with including the synsets?
Experiment a bit with different words and verify your ideas.
"""

# warning: this may take some time to run
lex_featuresets = [(lexicon_features(d), c) for (d, c) in documents]
lex_train_set, lex_test_set = train_test_split(lex_featuresets, test_size=0.1)
lex_model = model.train(lex_train_set)  # the same classifier as you defined above
lex_model.show_most_informative_features()
print("Accuracy: ", nltk.classify.accuracy(lex_model, lex_test_set))