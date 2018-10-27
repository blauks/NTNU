def itererStreng(s):
    for x in s:
        print(x)

itererStreng("HELLO")

def tredjeBokstav(s):
    try:
        if s[2] != None:
            return s[2]
    except IndexError:
            return "q"

print(tredjeBokstav("hello"))

def størsteIndex(s):
    return len(s)-1

print(størsteIndex("HALLO"))