def seqSearch(lst, item):
    for el in lst:
        if el == item:
            return True
    
    return False

print(seqSearch(["a","b","c","d"],"x"))