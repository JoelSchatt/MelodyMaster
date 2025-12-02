#-------------ARCADEBUTTONS_____________________

#Dieser Code: liest 10× pro Sekunde den Button aus, gibt den Wert (0/1) in der Konsole aus, lässt eine LED dauerhaft leuchten

from machine import Pin
from time import sleep_ms

btn = Pin("D8", Pin.IN, Pin.PULL_UP) #→ interner Pull-Up-Widerstand → der Pin ist HIGH, solange der Button nicht gedrückt ist → Beim Drücken wird er LOW (0)
led = Pin("D9", Pin.OUT)
led.on() #schaltet die LED sofort an

while True:
  print(btn.value()) #liest den aktuellen Button-Zustand (0 oder 1)
  sleep_ms(100)

#-------------DISPLAY ANZEIGE-------------------------

import sh1106
from machine import I2C
import time

display = sh1106.SH1106_I2C(128, 64, I2C(1))

display.fill(0)                   
display.text("Welcome to", 25, 17, 1)
display.text("melody master", 19, 27, 1)
display.text("XD", 55, 37, 1)
display.show()

# warten
time.sleep(1)

# Ersten Text löschen
display.fill(0)
display.show()

display.fill(0)                   
display.text("To start game:", 12, 15, 1)
display.text("press random", 17, 25, 1)
display.text("button", 40, 35, 1)
display.show()

# warten
time.sleep(1)

# Ersten Text löschen
display.fill(0)
display.show()

#Hier Code einfügen: wenn random button gedrückt wird, startet Level 1

display.fill(0)
display.text("memorize this", 15, 20, 1)
display.text("melody!", 40, 30, 1)
#display.text("NOTE einfügen", 40, 30, 1)
display.show()

#Hier Code einfügen: Melodie wird vorgespielt mit aufblinkender Hintergrundbelichtung

# warten
time.sleep(1)

# Ersten Text löschen
display.fill(0)
display.show()

display.fill(0)
display.text("play back", 30, 20, 1)
display.text("the melody!", 25, 30, 1)
#display.text("NOTE einfügen", 40, 30, 1)
display.show()

# warten
time.sleep(1)

# Ersten Text löschen
display.fill(0)
display.show()

#Code einfügen: Melodie wurde flasch nachgespielt.

display.fill(0)
display.text("!!WRONG!!", 30, 20, 1)
display.text("try again", 30, 30, 1)
display.text(";D", 55, 40, 1)
display.show()

# warten
time.sleep(1)

# Ersten Text löschen
display.fill(0)
display.show()

#Code einfügen: Melodie wurde richtig nachgespielt und man kommt ins nächste Level

display.fill(0)
display.text("CONGRATS", 35, 15, 1)
display.text("you MASTERED", 20, 25, 1)
display.text("the melody", 30, 35, 1)
display.text(";D", 55, 45, 1)
display.show()

# 4 Sekunden warten
time.sleep(1)

# Ersten Text löschen
display.fill(0)
display.show()

display.fill(0)
display.text("Level up!", 35, 25, 1)
display.text("next level:XY", 20, 35, 1)
display.show()

# 4 Sekunden warten
time.sleep(1)

# Ersten Text löschen
display.fill(0)
display.show()



