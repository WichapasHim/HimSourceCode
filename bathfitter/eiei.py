import pyautogui as pyg
import time

pyg.hotkey('win','d')
time.sleep(3)
pyg.hotkey('win')
time.sleep(2)
pyg.write('notepad')
time.sleep(1)
pyg.press('enter')
time.sleep(2)
pyg.write('I love sab sanit')
