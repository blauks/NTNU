import time
from turtle import *
# importerer funksjoner fra turtle
print("Hei, jeg kan tegne en trekant")
PeN = ""
OeN = input("Ønsker du at spissen på trekanten er opp eller ned? (O/N)")
if(OeN == "O"):
    PeN = 120
else:
    PeN = -120
pensize(7)          # sett pennen 7 piksler tykk
pencolor("pink")    # sett pennefargen til rosa
bgcolor("#00509e")     # sett bakgrunnsfargen grå
fillcolor("purple") # sett fyllfargen lilla
# Tegner en fylt trekant
begin_fill()
forward(200)        # gå 100 piksler framover
left(PeN)           # drei 120 grader venstre
forward(200)  
left(PeN) 
forward(200)
end_fill()
  
# Holder vinduet med tegningen åpent i 10 sekunder. Ha dette som siste linje i koden din
time.sleep(10)