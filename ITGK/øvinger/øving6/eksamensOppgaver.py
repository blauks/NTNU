fasit = ["A", "C", "B", "D", "A", "A", "B", "A", "C", "A", "D", "A", "C", "C", "B", "A", "B", "A", "C", "D"]

def sjekkSvar(eS):
    poeng = 0
    for x in range(20):
        if eS[x] == fasit[x]:
            poeng = poeng + 1
    
    poeng = poeng/20
    poeng = poeng * 100
    return poeng

print(sjekkSvar(['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']))
