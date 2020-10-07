# To run this code, open Google Drive and go into
# folder of items to be invoiced.
# Open Wave in another browser tab and go to Create New Invoice
# Maximise browser window
import pyautogui
import time

# print(pyautogui.size())
pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

# first item to click at x=480, y=290

found = True
y_grid = 290
i = 1

while found != None:
    time.sleep(0.5)
    pyautogui.moveTo(480, y_grid)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(4)
    # pyautogui.moveRel(85, 265, duration=0.5)
    found = pyautogui.locateCenterOnScreen(
        'ren.png', region=(480, y_grid, 100, 310), confidence=0.6)

    if found != None:
        pyautogui.click(pyautogui.locateCenterOnScreen(
            'ren.png', region=(480, y_grid, 100, 310), confidence=0.6))
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        # pyautogui.press('c')
        # pyautogui.keyUp('ctrl')
        # time.sleep(1)
        pyautogui.press('esc')
        y_grid = y_grid + 48

        # switch window
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(2)

        # wave window operation
        pyautogui.click(pyautogui.locateCenterOnScreen(
            'wave_add.png', region=(1000, 450, 100, 600), confidence=0.8))
        time.sleep(1)
        pyautogui.press(['a', 'enter'])
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        if i % 3 != 0:
            i = i + 1
        else:
            pyautogui.scroll(-9)
            i = i + 1

        # switch window
        pyautogui.hotkey('ctrl', 'tab')

pyautogui.press('esc')

# switch window
pyautogui.hotkey('ctrl', 'tab')
time.sleep(0.5)
pyautogui.scroll(20)
pyautogui.click(pyautogui.locateCenterOnScreen(
    'add_customer.png', confidence=0.8))
pyautogui.write('Redhill')
pyautogui.press('enter')
pyautogui.click(pyautogui.locateCenterOnScreen(
    'save_invoice.png', confidence=0.8))
