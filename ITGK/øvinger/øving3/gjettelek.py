import random

nedreTall = int(input("Gi en nedre grense for det tilfeldige tallet: "))
øvreTall = int(input("Gi en øvre grense for det tilfeldige tallet: "))

tilfeldigTall = random.randint(nedreTall,øvreTall)
print(tilfeldigTall)
brukerTall = -99191919

while brukerTall != tilfeldigTall:
    brukerTall = int(input("Gjett et tall: "))
    if brukerTall > tilfeldigTall:
        print("Lavere")
    elif brukerTall < tilfeldigTall:
        print("Høyere")
    else:
        print("Du klarte det! Tallet var", tilfeldigTall)
        break