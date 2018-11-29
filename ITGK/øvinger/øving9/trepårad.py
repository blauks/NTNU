brikker = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]


def makeBoard():
    print()
    for x in range(3):
        print("-------------------")
        for y in range(3):
            print("| ",brikker[x][y]," ", end="")
        print("|")

    print("-------------------")
    print()


def checkWin():
    for x in range(3):
        if brikker[x][0] == brikker[x][1] == brikker[x][2] and brikker[x][0] != " ":
            return True, brikker[x][0]
        elif brikker[0][x] == brikker[1][x] == brikker[2][x] and brikker[0][x] != " ":
            return True, brikker[0][x]
        elif brikker[0][0] == brikker[1][1] == brikker[2][2] and brikker[0][0] != " ":
            return True, brikker[0][0]
        elif brikker[0][2] == brikker[1][1] == brikker[2][2] and brikker[0][2] != " ":
            return True, brikker[0][2]
        
    return False, "no"

def checkIfTaken(p):
    if p == " ":
        return True
    return False

def makeAPlay(x,y,p):
    if p == 0:
        brikker[x][y] = "x"
    else:
        brikker[x][y] = "o"
    


makeBoard()

player1 = input("Hva heter spiller en? ")
player2 = input("Hva heter spiller to? ")

playerTurn = 0

while True: 
    print()
    plasser = input("Skriv inn hvor du vil plassere brikken din f.eks. 0,0 for å plassere den øverst i venstre hjørnet. ")
    plass = plasser.split(",")
    try:
        if checkIfTaken(brikker[int(plass[0])][int(plass[1])]):
            if playerTurn == 0:
                makeAPlay(int(plass[0]),int(plass[1]),playerTurn)
                playerTurn = 1
            else:
                makeAPlay(int(plass[0]),int(plass[1]),playerTurn)
                playerTurn = 0
            
            makeBoard()
            checkState, whoWon = checkWin()
            if checkState:
                if whoWon == "x":
                    print(player1, "wins the game!")
                else:
                    print(player2, "wins the game!")

        else:
            print()
            print("----------------")
            print("Skriv inn en gyldig plass")
            print("----------------")
        
    except IndexError:
        print("Skriv inn en gyldig plass")
