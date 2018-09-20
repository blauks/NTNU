Pizza = 750
Studentrabatt = 0.80
Tips = 1.08

Totalt = (Pizza*Studentrabatt)*Tips

HvorMange = int(input("Hvor mange spiste middag? "))

print("Ettersom dere var", HvorMange, "personer, så må hver person betale", Totalt/HvorMange, "kroner")