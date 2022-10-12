"""
# Lab 3
"""
import nltk
from sklearn.model_selection import train_test_split
# feel free to import from modules of sklearn and nltk later
# e.g., from sklearn.model_selection import train_test_split


"""
## Exercise 1 - Gender detection of names
In NLTK you'll find the corpus `corpus.names`. A set of 5000 male and 3000 female names.
1) Select a ratio of train/test data (based on experiences from previous labs perhaps?)
2) Build a feature extractor function
3) Build two classifiers:
    - Decision tree
    - Naïve bayes
    
Finally, write code to evaluate the classifiers. Explain your results, and what do you think would change if you altered your feature extractor?
"""

class GenderDataset:
    def __init__(self):
        self.names = nltk.corpus.names
        self.data = None
        self.build()

    def make_labels(self, gender):
        """
        this function is to help you get started
        based on the passed gender, as you can fetch from the file ids,
        we return a tuple of (name, gender) for each name
        
        use this in `build` below, or do your own thing completely :)
        """
        return [(n, gender) for n in self.names.words(gender + ".txt")]
    
    def build(self):
        """ TODO
        combine the data in "male" and "female" into one
        remember to randomize the order
        """
        pass
    
    def split(self, ratio):
        return train_test_split(self.data, test_size=ratio)

class Classifier:
    def __init__(self, classifier):
        self.classifier = classifier
        self.model = None
    
    def train(self, data):
        # TODO: train classifier and store model
        pass
        
    def test(self, data):
        # TODO: return accuracy for the model on input data
        pass
    
    def train_and_evaluate(self, train, test):
        self.train(train)
        return self.test(test)
        
    def show_features(self):
        # OPTIONAL
        pass

                                 
class FeatureExtractor:
    def __init__(self, data):
        self.data = data
        self.features = []  
        
        self.build()
                 
    @staticmethod
    def text_to_features(name):
        # TODO: create a dict of features from a name
        return {
            "name": name
        }
    
    def build(self):
        # TODO: populate your features with the above function
        pass


split_ratio = 0.01  # TODO: modify
train, test = GenderDataset().split(ratio=split_ratio)

classifiers = {
    "decision_tree": Classifier(None), # TODO
    "naive_bayes": Classifier(None), # TODO
}

train_set = FeatureExtractor(train).features
test_set = FeatureExtractor(test).features

for name, classifier in classifiers.items():
    acc = classifier.train_and_evaluate(train_set, test_set)
    print("Model: {}\tAccuracy: {}".format(name, acc))