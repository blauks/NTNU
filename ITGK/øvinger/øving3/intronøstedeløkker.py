antallStudenter = int(input("Hvor mange studenter? "))
antallEmner = int(input("Hvor mange emner? "))

for x in range(antallStudenter):
    for y in range(antallEmner):
        print("Student", x + 1, "elsker Emne", y + 1, end=" ; ")
    print("\n")

for timer in range(24):
    for minutter in range(60):
        if len(str(minutter)) > 1:
            print(str(timer) + ":" + str(minutter))
        else:
            print(str(timer) + ":0" + str(minutter))

for tall1 in range(11):
    for tall2 in range(11):
        print(tall1*tall2, end=" ")
    print()