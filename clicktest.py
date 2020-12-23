import pyautogui
import win32api, win32con

def click_image(image):
    start = pyautogui.locateCenterOnScreen(image, confidence=0.5)
    print(start)
    pyautogui.moveTo(start)
    pyautogui.displayMousePosition()
    