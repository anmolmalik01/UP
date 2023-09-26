import pyautogui
import time

# button7location = pyautogui.locateOnScreen('chrome.png')
# loc = pyautogui.locateOnScreen('chrome.png', grayscale=True, confidence=.5)
# print(button7location)
# print(loc)

time.sleep(5)
image = 'chrome.png'
loc = pyautogui.locateOnScreen(image, grayscale=True, confidence=.5)
print (loc)