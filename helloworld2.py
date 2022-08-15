import pyautogui
print(pyautogui.size())
a = ((0,0),(1920,0), (0,1080),(1920,1080))
pyautogui.center(a)
print(a)