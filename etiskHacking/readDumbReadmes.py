maks = 18278
fnm = "README"

tmp = ""

for x in range(maks):
    f = open("dumbfiles/files/"+fnm+("0"*(5-len(str(x))))+str(x))
    for l in f.readlines():
        tmp += l
    if len(tmp) >= 2800:
        print(tmp)
        tmp = ""
    f.close()

