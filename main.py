import os
import Xlib.display
import pyautogui
# os.environ['DISPLAY'] = ':99'

pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
pyautogui.screenshot("Test.png")