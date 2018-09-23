import time
from turtle import *
# importerer funksjoner fra turtle
print("Hei, jeg kan tegne en trekant")

pennefarge = input("Velg pennefarge, NTNU-rosa (R) eller NTNU-turkis (T): ")
if pennefarge == "R":
    pennefarge = "#ad208e"
else:
    pennefarge = "#5cbec9"

fyllfarge = input("Fyllfarge, NTNU-gul (G), -oransj (O) eller -lilla (L): ")
if fyllfarge == "G":
    fyllfarge = "#d5d10e"
elif fyllfarge == "O":
    fyllfarge = "#f58025"
else:
    fyllfarge = "#552988"

PeN = ""
OeN = input("Ønsker du at spissen på trekanten er opp eller ned? (O/N) ")
if(OeN == "O"):
    PeN = 120
else:
    PeN = -120

pensize(7)          # sett pennen 7 piksler tykk
pencolor(pennefarge)    # sett pennefargen til rosa
bgcolor("#00509e")     # sett bakgrunnsfargen grå
fillcolor(fyllfarge) # sett fyllfargen lilla
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