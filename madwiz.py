import pywinauto
from pywinauto.application import Application
import data-coords as data
import time
# //Set resolution to 1280x720
# //Standard timed run, dumb version. Uses 3 familiars clicking on board and one on clicker upgrade. Also manually clicks Deekin (upgrade mode) every 5 seconds to max speed.

def gameWindowHook():
    # Find game window.
    app = app = Application().connect(title='Idle Champions')
    win = app.window(title='Idle Champions')
    # Bring game window to foreground
    win.SetFocus()
    #Start main

# Select Town/MW Adventure
def MWSelect():
    # Neverwinter Woods Town
    pywinauto.mouse.click(button='left',coords=(data.NeverWinterWoods))
    time.sleep(.1)
    # Selecting Mad Wizard
    pywinauto.mouse.click(button='left', coords=(1125, 750))

    # Load time pause
    time.sleep(5)
    formationSelectStart()

# Opens formation selection screen
def formationSelectStart():
    # Formation Selection Screen
    pywinauto.mouse.click(button='left', coords=(345, 800))
    time.sleep(.01)
    # Formation Selection
    pywinauto.mouse.click(button='left', coords=(1034, 523))
    print('moving to deekin leveling')
    numberOfLevels = True
    while numberOfLevels != False:
        pywinauto.mouse.click(button='left', coords=(345, 800))
        time.sleep(10)
        while i < 50:
           i = 1
           pywinauto.mouse.click(button='left', coords=(345, 800))
           time.sleep(4)
           i += 1
        print(numberOfLevels)


def characterLeveling():
    #Deekin
    deekinLevel = 1
    while deekinLevel < 20:
        send_keys(data.LevelingSlot1)
        deekinLevel += 1
    clickerLevel = 1
    while clickerLevel < 130:
        pywinauto.mouse.press(button='left', coords=(500, 888))
        time.sleep(2)

isRunning = True

while True:
    MWSelect()
