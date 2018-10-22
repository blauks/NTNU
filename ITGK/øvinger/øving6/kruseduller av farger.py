import turtle

oddeTall = [x for x in range(1,20,2)]
fargeList = []

farger = input("Skriv inn 10 farger, og separer hver farge med komma og mellomrom: ")
farger = farger.lower()
fargeList = farger.split(", ")
turtle.speed(200)

for x in range(len(oddeTall)):
    turtle.color(fargeList[x])
    turtle.setposition(0,0)
    for y in range(50):
        turtle.forward((50))
        turtle.left(123)



