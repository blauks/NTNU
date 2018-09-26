import math

def areal_sirkel(r, pi):
    A = pi * r**2
    print("r =", r, ", A =", A)

areal_sirkel(float(input("Skriv inn radiusen til sirkelen: ")), math.pi)