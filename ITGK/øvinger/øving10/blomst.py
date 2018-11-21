import time
from turtle import *
 
pensize(2)
pencolor("orange")
bgcolor("green")
fillcolor("blue")
 
def halfPetal():
    forward(50)
    left(30)
    forward(75)
    left(30)
    forward(50)
    left(120)
 
def petal():
    for i in range(2):
        halfPetal()
     
def flower(num, i=1):
    if i==1:
        begin_fill()
 
    petal()
    left(60)


    if i==1:
        end_fill()

    if num > 0:
        flower(num - 1)
 
flower(12)
time.sleep(10)