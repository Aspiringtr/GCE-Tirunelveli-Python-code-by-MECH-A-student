from pyautogui import *
import pyautogui
import keyboard
import random,time
import win32con, win32api
import numpy as np

time.sleep(5)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
"""while keyboard.is_pressed("q")==False:
    if pyautogui.pixel(736,512)[0]!= 254 and pyautogui.pixel(36,512)[1]!= 253 and pyautogui.pixel(36,512)[2]!= 243:
       click(736,512)
       break"""
"""while keyboard.is_pressed("q")==False:
    click(700,400)"""

while keyboard.is_pressed("q")==False :
    b,c=pyautogui.position()
    a=pyautogui.pixel(b,c)
    if pyautogui.pixel(b,c) != a:
        click(b,c)
        break
    

