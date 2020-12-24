import os
import time
from datetime import datetime
import time
import pyautogui
import win32api, win32con
from discord_webhook import DiscordWebhook
import random


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def doubleclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def processImage(image):
        print ("Processing image...")
        return pyautogui.locateOnScreen(image, confidence=0.5)

def click_image(image):
    start = pyautogui.locateOnScreen(image, confidence=0.8)
    pyautogui.moveTo(start)
    click()

def doubleclick_image(image):
    start = pyautogui.locateOnScreen(image, confidence=0.8)
    pyautogui.moveTo(start)
    doubleclick()

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

# jointime = input("What time do you want to join? (24 hour time, HOUR:MINUTE ex. 22:37): ")
# distag = input("What is your discord tag? (ex. @UserName#0000): ")
# timeoutprompt = input("Timeout? (If you are AFK and do not want to enter 2b2t AFK) (y/n):")
# soundwarning = input("Play an alarm when at a high queue position? (y/n): ")
# warningpos = int(input("What position to warn you?: "))
# if timeoutprompt == 'y' or timeoutprompt == 'yes':
#     timeoutpos = int(input("What queue position to disconnect at?: "))
#     recconect = input("Reconnect after disconnecting? (y/n): ")
# else:
#     timeoutpos = 69420 # 😎👉👉
#     reconnect = 'y'

jointime = ("04:00")
distag = ("<@773984010049028096>")
timeoutprompt = ('n')
warningpos = 50
timeoutprompt = 'y'
soundwarning = 'n'
if timeoutprompt == 'y' or timeoutprompt == 'yes':
    timeoutpos = 5
    reconnect = 'y'
else:
    timeoutpos = 69420 # 😎👉👉
    reconnect = 'y'

repit = 1
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if current_time == jointime:
        while True:
            logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
            loglines = follow(logfile)
            try:
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/791062578259820554/iQf1YuL4QAPogIPiL6cVnjOafCUOQuT190WnMLaVqSGMLOoR63cjGarVTO0M0brctep9', content=("Started at " + current_time))
                webhook.execute()
            except:
                print ("Could not reach discord")
            doubleclick_image('assets/2b2tlogo/2b2tlogoauto.png')
            doubleclick_image('assets/2b2tlogo/2b2tlogolarge.png')
            doubleclick_image('assets/2b2tlogo/2b2tlogonormal.png')
            doubleclick_image('assets/2b2tlogo/2b2tlogosmall.png')
            now = datetime.now()
            current_timeintlast = now.strftime("%H%M")
            current_timeintlast1 = int(current_timeintlast)
            for line in loglines:
                print (line)
                now = datetime.now()
                current_timeint = now.strftime("%H%M")
                current_timeint1 = int(current_timeint)
                if "[Client thread/INFO]: [CHAT]" in line or "[main/INFO]: [CHAT]" in line:
                    linechat = line.split('[CHAT] ')
                    try:
                        queuepos = linechat[1].split(': ')
                    except:
                        queuepos = 69420360
                    try:
                        queuepos1 = int(queuepos[-1])
                    except:
                        queuepos1 = 69420360
                    if queuepos1 < timeoutpos and timeoutprompt == 'y' or timeoutprompt == 'yes':
                        pyautogui.press('esc')
                        time.sleep(0.3)
                        click_image('assets/disconnect/disconnectautogui.png')
                        click_image('assets/disconnect/disconnectlargegui.png')
                        click_image('assets/disconnect/disconnectnormalgui.png')
                        click_image('assets/disconnect/disconnectsmallgui.png')
                        now = datetime.now()
                        current_timeintlast = now.strftime("%H%M")
                        current_timeintlast1 = int(current_timeintlast)
                        time.sleep(30)
                        if reconnect == 'n' or 'no':
                            while True:
                                time.sleep(69420)
                        break
                    elif queuepos1 < warningpos:
                        try:
                            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/791062578259820554/iQf1YuL4QAPogIPiL6cVnjOafCUOQuT190WnMLaVqSGMLOoR63cjGarVTO0M0brctep9', content=linechat[1] + ' ' + distag)
                            webhook.execute()
                        except:
                            print ("Could not reach discord")
                        if soundwarning == 'yes' or soundwarning == 'y' and repit == 1:
                            randb = str(random.randint(1,5))
                            os.startfile('assets\\audio\\alarm'+ randb + '.mp3')
                            repit = repit + 1
                        now = datetime.now()
                        current_timeintlast = now.strftime("%H%M")
                        current_timeintlast1 = int(current_timeintlast)
                    elif ("Position in queue") in linechat[1] or ("2b2t is full") in linechat[1]:
                        try:
                            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/791062578259820554/iQf1YuL4QAPogIPiL6cVnjOafCUOQuT190WnMLaVqSGMLOoR63cjGarVTO0M0brctep9', content=linechat[1])
                            webhook.execute()
                        except:
                            print ("Could not reach discord")
                        now = datetime.now()
                        current_timeintlast = now.strftime("%H%M")
                        current_timeintlast1 = int(current_timeintlast)         
                    else:
                        pass
                else:
                    if processImage('assets/backtoserverlist/btslauto.png'):
                        click_image('assets/backtoserverlist/btslauto.png')
                        time.sleep(5)
                        break
                    elif processImage('assets/backtoserverlist/btsllarge.png'):
                        click_image('assets/backtoserverlist/btsllarge.png')
                        time.sleep(5)
                        break
                    elif processImage('assets/backtoserverlist/btslnormal.png'):
                        click_image('assets/backtoserverlist/btslnormal.png')
                        time.sleep(5)
                        break
                    elif processImage('assets/backtoserverlist/btslsmall.png'):
                        click_image('assets/backtoserverlist/btslsmall.png')
                        time.sleep(5)
                        break
                    else:
                        pass
    time.sleep(10)