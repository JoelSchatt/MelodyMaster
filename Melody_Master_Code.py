# This program was created in Arduino Lab for MicroPython
from modulino import ModulinoBuzzer
from modulino import ModulinoButtons
import sh1106
from machine import I2C
from time import sleep
import random

class Button:
  def __init__(self, tone):
    self.tone = tone

# Initialize Variables
check_index = 0
random_numbers = []
failed = False

# Create random sequence
for i in range(3):
  random_numbers.append(random.randint(1,3))

# Button class to append tone attribute to button

buttons = ModulinoButtons()
buzzer = ModulinoBuzzer()
display = sh1106.SH1106_I2C(128, 64, I2C(1))

# Functions to show LED and play tone on buzzer
def a_tone_light():
  buttons.set_led_status(True, False, False)
  buzzer.tone(button_a.tone)
  sleep(0.4)
  buzzer.no_tone()
  buttons.set_led_status(False, False, False)

def b_tone_light():
  buttons.set_led_status(False, True, False)
  buzzer.tone(button_b.tone)
  sleep(0.4)
  buzzer.no_tone()
  buttons.set_led_status(False, False, False)

def c_tone_light():
  buttons.set_led_status(False, False, True)
  buzzer.tone(button_c.tone)
  sleep(0.4)
  buzzer.no_tone()
  buttons.set_led_status(False, False, False)

# Functions to check if the right button is pressed
def on_a_release():
  a_tone_light()
  global check_index
  global failed
  if random_numbers[check_index] == 1:
    check_index += 1
  else:
    failed = True

def on_b_release():
  b_tone_light()
  global check_index
  global failed
  if random_numbers[check_index] == 2:
    check_index += 1
  else:
    failed = True

def on_c_release():
  c_tone_light()
  global check_index
  global failed
  if random_numbers[check_index] == 3:
    check_index += 1
  else:
    failed = True

def waitForRandomButtonPressed():
  buttons.update()
  while not buttons.button_a_pressed and not buttons.button_b_pressed and not buttons.button_c_pressed:
    buttons.update()
  return 
  

# Create object for each button
button_a = Button(ModulinoBuzzer.NOTES["C5"])
button_b = Button(ModulinoBuzzer.NOTES["E5"])
button_c = Button(ModulinoBuzzer.NOTES["G5"])

# Display welcome
display.fill(0)                   
display.text("Welcome to", 25, 17, 1)
display.text("melody master", 19, 27, 1)
display.text("XD", 55, 37, 1)
display.show()

sleep(2)

# Ersten Text löschen
display.fill(0)
display.show()

display.fill(0)                   
display.text("To start game:", 12, 15, 1)
display.text("press random", 17, 25, 1)
display.text("button", 40, 35, 1)
display.show()

waitForRandomButtonPressed()

display.fill(0)
display.show()

# TODO add countdown before Start
sleep(3)

# update button to reset random button input
buttons.update()


display.fill(0)
display.text("memorize this", 15, 20, 1)
display.text("melody!", 40, 30, 1)
display.show()

# Play random sequence to memorize
for i in random_numbers:
  if i == 1:
    a_tone_light()
  elif i == 2:
    b_tone_light()
  elif i == 3:
    c_tone_light()
  sleep(0.5)

# Create release events
buttons.on_button_a_release = on_a_release
buttons.on_button_b_release = on_b_release
buttons.on_button_c_release = on_c_release

display.fill(0)
display.show()

display.fill(0)
display.text("play back", 30, 20, 1)
display.text("the melody!", 25, 30, 1)
display.show()

while True:
  buttons.update()
  if failed == True:
    print("You failed!")
    display.fill(0)
    display.show()
    display.fill(0)
    display.text("!!WRONG!!", 30, 20, 1)
    display.text("try again", 30, 30, 1)
    display.text(";D", 55, 40, 1)
    display.show()
    buttons.set_led_status(True, True, True)
    buzzer.tone(ModulinoBuzzer.NOTES["CS4"])
    sleep(0.7)
    buzzer.no_tone()
    buttons.set_led_status(False, False, False)
    break
  elif check_index == len(random_numbers):
    display.fill(0)
    display.show()
    display.fill(0)
    display.text("CONGRATS", 35, 15, 1)
    display.text("you MASTERED", 20, 25, 1)
    display.text("the melody", 30, 35, 1)
    display.text(";D", 55, 45, 1)
    display.show()
    print("Congratulations, you won!")
    break
   