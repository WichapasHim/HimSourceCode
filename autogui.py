import pyautogui as py
import time as t
    
    
t.sleep(5)

while(True):
    py.hotkey('ctrl','A')
    t.sleep(3)
    py.hotkey('del')
    t.sleep(3)
    py.write('I am working lol')
    t.sleep(3)