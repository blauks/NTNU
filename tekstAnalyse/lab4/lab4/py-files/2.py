import nltk

"""
# Exercise 2 - Making use of chunks

## 2a)
With the following grammar rules:
```
1. proper noun singular
2. determiner followed by an adjective, followed by any noun
3. two consecutive nouns
```
Create a `RegexpParser` chunker
"""

grammar = None
# TODO: set up a parser using the grammar you defined
chunk_parser = None

"""
## 2b)

Read the file `starlink.txt` and perform the following operations on the text:
- sentence tokenize
- word tokenize
- pos tag

"""
import os

"""
TODO:
- read the file "starlink.txt"
- tokenize and tag the words of each sentence

the below function is just an idea of generalization to any file.
you can delete this and write your own code.
"""
def get_pos_tags_from_file(filename):
    pass
    
starlink_tagged = get_pos_tags_from_file("starlink.txt")

"""
## 2c)
From all found subtrees in the text, print out the text from all the leaves on the form of `DT -> JJ -> NN` (i.e. the CONSECUTIVE chunk you defined above)
"""

"""
TODO:
write a function to retrieve the DT-JJ-NN sequences
from the grammar you defined in 2a)
"""
def get_descriptive_nouns(tagged_sents):
    pass

get_descriptive_nouns(starlink_tagged)

"""
## 2d)
Create a custom rule for a combination of 3 or more tags, similarly to task c).

Do you see any practical uses for chunking with this rule, or in general?
"""
