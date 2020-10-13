import os, sys, Crypto
from Crypto.PublicKey import RSA
from sympy import *
import gmpy2

pp = []
p = randprime(2**1019, 2**1020)
pp.append(p)
for i in range(1, 8):
    nextp = nextprime(2 * pp[-1])
    pp.append(nextp)

print(pp)

nn = []
for i in range(4):
    nn.append( pp[i] * pp[7 - i] )

print(nn)

n1 = prevprime(int(gmpy2.sqrt(nn[3]//2)))
print("-----")
print(n1)
print("-----")

tmpRSAkeys = []
for i in range(4):
    newd = Crypto.Util.number.inverse(65537, (pp[i] - 1)*(pp[7 - i] - 1))
    newkey = RSA.construct((nn[i], 65537, newd, pp[i], pp[7 - i]))
    tmpRSAkeys.append(newkey)
