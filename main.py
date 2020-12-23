import time, os
from datetime import datetime
import time
import pyautogui
import win32api, win32con
from discord_webhook import DiscordWebhook



def doubleclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click_image(image):
    start = pyautogui.locateCenterOnScreen(image)
    pyautogui.moveTo(start)
    doubleclick()

now = datetime.now()

jointime = input("What time do you want to join? (24 hour time, HOUR:MINUTE ex. 22:37): ")

while True:
    current_time = now.strftime("%H:%M")

    if current_time == jointime:
        def follow(thefile):
            thefile.seek(0,2)
            while True:
                line = thefile.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                yield line

        if __name__ == "__main__":
            logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
            loglines = follow(logfile)
            for line in loglines:
                if "[Client thread/INFO]: [CHAT]" in line:
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/791062578259820554/iQf1YuL4QAPogIPiL6cVnjOafCUOQuT190WnMLaVqSGMLOoR63cjGarVTO0M0brctep9', content=line)
                    webhook.execute()
    time.sleep(10)