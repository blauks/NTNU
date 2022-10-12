
"""
## Exercise 2 - Spam or ham
Spam or ham is referred to a mail being spam or regular ("ham"). Follow the instructions and implement the `TODOs`
"""
from sklearn.model_selection import train_test_split
import pandas as pd

spam = pd.read_csv(
    'spam.csv',
    usecols=["v1", "v2"],
    encoding="latin-1"
).rename(columns={"v1": "label", "v2": "text"})

print(spam.label.value_counts())
spam.head()

""" TODO: transform label to numerical
Expected output:
0    4825
1     747
Name: label, dtype: int64

hint: you can use "apply" or "replace" for a column in pandas
"""
spam.label = spam.label # your transformation goes here
spam.label.value_counts()

class TextCleaner:
    def __init__(self, text):
        self.text = [] # TODO: tokenize
        self.stemmer = None # TODO: incorporate a stemmer of your choice
        self.stopwords = None  # TODO: you've done this a few times
        self.lem = None  # TODO: lemmatizer
    
    """
    Create small functions to replace your tokens (self.text)
    iteratively. Such as a lowercase function.
    """
    def lowercase(self):
        self.text = [w.lower() for w in self.text]

    def clean(self):
        self.lowercase()
        """
        TODO: populate with your defined cleaning functions here
        perhaps you want some conditional values to
        control which functions to use?
        """
        
        # finally, return it as a text 
        return " ".join(self.text)

clean = lambda text: TextCleaner(text).clean()
spam.text = spam.text.apply(clean)
print(spam.head())

split_ratio = 0.01 # TODO: modify
X_train, X_test, y_train, y_test = train_test_split(
    spam.text, spam.label, test_size=split_ratio, random_state=4310)

# TODO: vectorize with sklearn
vectorizer = None
# TODO: fit the vectorizer to your training data
X_train = None

# TODO: set up a multinomial classifier
classifier = None
if classifier:
    classifier.fit(X_train, y_train)
    
vectorized = None

def predict(model, vectorizer, data, all_predictions=False):
    data = None # TODO apply the transformation from the vectorizer to test data 
    if all_predictions:
        return model.predict_proba(data)
    else:
        return model.predict(data)

def print_examples(data, probs, label1, label2, n=10):
    percent = lambda x: "{}%".format(round(x*100, 1))

    for text, pred in list(zip(data, probs))[:n]:
        print("{}\n{}: {} / {}: {}\n{}".format(
            text,
            label1,
            percent(pred[0]),
            label2,
            percent(pred[1]),
            "-" * 100  # to print a line
        ))
    
y_probas = predict(classifier, vectorizer, X_test, all_predictions=True)
print_examples(X_test, y_probas, "ham", "spam", n)

y_pred = predict(classifier, vectorizer, X_test)
# TODO display a confusion matrix on the test set vs predictions
confusion_mat = None
print(confusion_mat)

# show precision and recall in a confusion matrix
tn, fp, fn, tp = confusion_mat.ravel()
recall = tp / (tp + fn)
precision = tp / (tp + fp)

print("Recall={}\nPrecision={}".format(round(recall, 2), round(precision, 2)))