# pyautogui
# pywinauto

import pyautogui
button7location = pyautogui.locateOnScreen('./images/chrome.png')
print(button7location)

# x, y = pyautogui.center(button7location)
# print(x, y)
# pyautogui.click(x, y)