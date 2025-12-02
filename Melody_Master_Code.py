# This program was created in Arduino Lab for MicroPython
from modulino import ModulinoBuzzer
from modulino import ModulinoButtons
from time import sleep
import random

check_index = 0
random_numbers = []
failed = False

for i in range(3):
  random_numbers.append(random.randint(1,3))

class Button:
  def __init__(self, tone):
    self.tone = tone

buttons = ModulinoButtons()
buzzer = ModulinoBuzzer()

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


button_a = Button(ModulinoBuzzer.NOTES["C5"])
button_b = Button(ModulinoBuzzer.NOTES["E5"])
button_c = Button(ModulinoBuzzer.NOTES["G5"])

for i in random_numbers:
  if i == 1:
    a_tone_light()
  elif i == 2:
    b_tone_light()
  elif i == 3:
    c_tone_light()
  sleep(0.5)

buttons.on_button_a_release = on_a_release
buttons.on_button_b_release = on_b_release
buttons.on_button_c_release = on_c_release

while True:
  buttons.update()
  if failed == True:
    print("You failed!")
    buttons.set_led_status(True, True, True)
    buzzer.tone(ModulinoBuzzer.NOTES["CS4"])
    sleep(0.7)
    buzzer.no_tone()
    buttons.set_led_status(False, False, False)
    break
  elif check_index == len(random_numbers):
    print("Congratulations, you won!")
    break
   