import nltk

"""
# Exercise 3 - Context-free grammar (CFG)

## 3a)
Create a cfg to handle sentences such as "she is programming", "they are coding" (look at the word forms and POS). The first verb should only handle present tense, while the second verb is flexible. Note that you need to specify the accepted words.
"""
cfg = nltk.CFG.fromstring("""
TODO
""")
cfg.productions()

#### A little function to visualize some possible outputs of the grammar
#### Do not change this
def generate_sample(grammar, start, tokens):        
    # iterate left hand and right hand side of the tree
    if start in grammar._lhs_index:
        derivation = random.choice(grammar._lhs_index[start])            
        for rhs in derivation._rhs:          
            generate_sample(grammar, rhs, tokens)
    elif start in grammar._rhs_index:
        tokens.append(str(start))
    return tokens

for _ in range(10):
    print(generate_sample(cfg, cfg.start(), []))
    
"""
## 3b)
Find some problems with the above CFG, any ideas how you would improve the results?
"""

"""
## 3c)
Initialize a `ChartParser` with the cfg from 3a).

Write a function to retrieve words not defined by your grammar.
"""

cfg_parser = None # TODO chartparser of cfg grammar above

"""
TODO
write a function that returns a list of missing tokens (not covered by your cfg)
Look up "lexical index" of a grammar.
"""

def parse(parser, cfg_grammar, sent):
    tokens = None # TODO word tokens
    missing = get_missing_words(cfg_grammar, tokens)
    if missing:
        print("Grammar does not cover: {}".format(missing))
        return
    trees = None # TODO: a list of parsed tokens
    for tree in trees:
        print(tree)
    if len(trees) > 0:
        return trees[0]
    else:
        print("Ungrammatical sentence.")
        
        
"""
## 3d)
output the tree of your parser for the sentence "they are programming"
"""
txt = "they are programming"
parse(cfg_parser, cfg, txt)