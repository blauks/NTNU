def hvorMye(tannListe):
    pengeListe = []
    for x in range(len(tannListe)):
        hvilkeMynter = [0,0,0,0]
        sumT = tannListe[x]
        tjue = sumT // 20
        sumT = sumT - (tjue*20)
        hvilkeMynter[0] = tjue
        if sumT != 0:
            ti = int(sumT/10)
            sumT = sumT - (ti*10)
            hvilkeMynter[1] = ti
            if sumT != 0:
                fem = int(sumT/5)
                sumT = sumT - (fem*5)
                hvilkeMynter[2] = fem
                if sumT != 0:
                    en = int(sumT/1)
                    sumT = sumT - en
                    hvilkeMynter[3] = en
        pengeListe.append(hvilkeMynter)

    return pengeListe

tenner = [53,28]
print(hvorMye(tenner))
