# To run this code, open Paint app first.
# Run the code at Terminal: python3 draw_in_paint.py
# Move mouse in the draw region of Paint app within 2 seconds
import pyautogui
import time
time.sleep(2)
pyautogui.click()
distance = 400
gap = 10
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance = distance - gap
    pyautogui.dragRel(0, distance, duration=0.2)
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance = distance - gap
    pyautogui.dragRel(0, -distance, duration=0.2)
