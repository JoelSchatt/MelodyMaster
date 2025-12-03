# MelodyMaster
from modulino import ModulinoBuzzer
from modulino import ModulinoButtons
import sh1106
from machine import I2C
from time import sleep
import random

# Button class to append tone attribute to button
class Button:
  def __init__(self, tone):
    self.tone = tone
    
class Level:
  def __init__(self, levelNumber, speed, toneCount):
    self.levelNumber = levelNumber
    self.speed = speed
    self.toneCount = toneCount

running = True
buttons = ModulinoButtons()
buzzer = ModulinoBuzzer()
display = sh1106.SH1106_I2C(128, 64, I2C(1))
currentLevel = None

# Kurze Victory Melodie
short_victory = [
    (ModulinoBuzzer.NOTES["C5"], 100),
    (ModulinoBuzzer.NOTES["E5"], 100),
    (ModulinoBuzzer.NOTES["G5"], 100),
    (ModulinoBuzzer.NOTES["C6"], 300)
]

# Lange Victory Melodie
long_victory = [
    (ModulinoBuzzer.NOTES["G4"], 150),
    (ModulinoBuzzer.NOTES["C5"], 150),
    (ModulinoBuzzer.NOTES["E5"], 150),
    (ModulinoBuzzer.NOTES["G5"], 300),
    (ModulinoBuzzer.NOTES["REST"], 50),
    (ModulinoBuzzer.NOTES["E5"], 150),
    (ModulinoBuzzer.NOTES["G5"], 300),
    (ModulinoBuzzer.NOTES["REST"], 50),
    (ModulinoBuzzer.NOTES["C5"], 150),
    (ModulinoBuzzer.NOTES["E5"], 150),
    (ModulinoBuzzer.NOTES["G5"], 150),
    (ModulinoBuzzer.NOTES["C6"], 450)
]

# Kurze Lose Melodie
short_lose = [
    (ModulinoBuzzer.NOTES["CS4"], 800)
]
  
# Functions to show LED and play tone on buzzer
def a_tone_light():
  buttons.set_led_status(True, False, False)
  buzzer.tone(button_a.tone)
  sleep(currentLevel.speed)
  buzzer.no_tone()
  buttons.set_led_status(False, False, False)

def b_tone_light():
  buttons.set_led_status(False, True, False)
  buzzer.tone(button_b.tone)
  sleep(currentLevel.speed)
  buzzer.no_tone()
  buttons.set_led_status(False, False, False)

def c_tone_light():
  buttons.set_led_status(False, False, True)
  buzzer.tone(button_c.tone)
  sleep(currentLevel.speed)
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

def playMelody(melody):
  for note, duration in melody:
    buzzer.tone(note, duration, blocking=True)
  

level1 = Level(1, 0.4, 4)
level2 = Level(2, 0.4, 6)
level3 = Level(3, 0.2, 7)
level4 = Level(4, 0.4, 8)

levels = [level1, level2, level3, level4]

nextLevel = levels[0]

# Display welcome
display.fill(0)                   
display.text("Welcome to", 25, 17, 1)
display.text("melody master", 19, 27, 1)
display.text("XD", 55, 37, 1)
display.show()

sleep(2)

while running:
  # Initialize Variables
  check_index = 0
  random_numbers = []
  failed = False
  currentLevel = nextLevel

  # Remove callbacks
  buttons.on_button_a_release = None
  buttons.on_button_b_release = None
  buttons.on_button_c_release = None
  
  # Create random sequence
  for i in range(currentLevel.toneCount):
    random_numbers.append(random.randint(1,3))

  print(random_numbers) # TODO Remove
  
  # Create object for each button
  button_a = Button(ModulinoBuzzer.NOTES["C5"])
  button_b = Button(ModulinoBuzzer.NOTES["E5"])
  button_c = Button(ModulinoBuzzer.NOTES["G5"])
  
  display.fill(0)                   
  display.text(f"Level {currentLevel.levelNumber}", 30, 10, 1)
  display.text("press any", 23, 25, 1)
  display.text("button to", 23, 35, 1)
  display.text("start", 40, 45, 1)

  display.show()
  
  waitForRandomButtonPressed()
  
  # countdown before Start
  display.fill(0) 
  display.text("get ready!", 25, 17, 1)
  display.text("3", 55, 40, 1)
  display.show()
  sleep(1)
  
  display.fill(0) 
  display.text("get ready!", 25, 17, 1)
  display.text("2", 55, 40, 1)
  display.show()
  sleep(1)
  
  display.fill(0) 
  display.text("get ready!", 25, 17, 1)
  display.text("1", 55, 40, 1)
  display.show()
  sleep(1)
  
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
    sleep(currentLevel.speed)
  
  # Create release callbacks
  buttons.on_button_a_release = on_a_release
  buttons.on_button_b_release = on_b_release
  buttons.on_button_c_release = on_c_release
  
  display.fill(0)
  display.text("play back", 30, 20, 1)
  display.text("the melody!", 25, 30, 1)
  display.show()
  
  while running:
    buttons.update()
    if failed == True:
      display.fill(0)
      display.text("!!WRONG!!", 30, 20, 1)
      display.text("try again", 30, 30, 1)
      display.text(";D", 55, 40, 1)
      display.show()
      buttons.set_led_status(True, True, True)
      playMelody(short_lose)
      sleep(2)
      buttons.set_led_status(False, False, False)
      nextLevel = currentLevel
      break
    elif check_index == len(random_numbers):
      # reset last button press
      buttons.update();
      if currentLevel.levelNumber < len(levels):
        display.fill(0)
        display.text(f"Level {currentLevel.levelNumber}", 38, 15, 1)
        display.text("MASTERED", 35, 25, 1)
        display.text(";D", 55, 45, 1)
        display.show()
        sleep(0.5)
        playMelody(short_victory)
        sleep(2)
        nextLevel = levels[currentLevel.levelNumber]
      else:
        display.fill(0)
        display.text("CONGRATS", 35, 15, 1)
        display.text("you MASTERED", 20, 25, 1)
        display.text("the melody", 30, 35, 1)
        display.text(";D", 55, 45, 1)
        display.show()
        sleep(0.5)
        playMelody(long_victory)
        sleep(10)
        # TODO Play again?
        # ends the program
        running = False
      break

      
     