import os
import time
from datetime import datetime
import time
import pyautogui
import win32api, win32con
from discord_webhook import DiscordWebhook
import random

title = """
   ___                  _ _     _  _                       
  / _ \                (_) |   | || |                      
 | | | | __      ____ _ _| |_  | || |_   _   _  ___  _   _ 
 | | | | \ \ /\ / / _` | | __| |__   _| | | | |/ _ \| | | |
 | |_| |  \ V  V / (_| | | |_     | |   | |_| | (_) | |_| |
  \___/    \_/\_/ \__,_|_|\__|    |_|    \__, |\___/ \__,_|
                                          __/ |            
                                         |___/             
                    By smokeytube
"""
print(title)


with open('preferences.txt') as infile:
    words = 0
    characters = 0
    lineno = 0
    for lineno, line in enumerate(infile, 1):
        wordslist = line.split()
        words += len(wordslist)
        characters += sum(len(word) for word in wordslist)

if characters < 110:
    print ("preferences.txt is likely empty or partially empty. Please fill it out.")
    override = input ("Manual override (if it is filled out) (y/n): ")
    if override == 'n' or override == 'no':
        print ("Please close the program and fill out preferences.txt")
        time.sleep(69420) #😎👉👉
    else:
        pass


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
        start = pyautogui.locateOnScreen(image, confidence=0.8)
        pyautogui.moveTo(start)
        return start

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


jointime =  ("16:59")
distag = ("<@773984010049028096>")
diswebhook = ("Bruh get your own damn webhook")
timeoutprompt = ('n')
warningpos = 50
timeoutprompt = 'y'
soundwarning = 'n'
timeoutpos = 5
reconnect = 'y'
timesleep = 30

with open('preferences.txt', 'r') as infer:
    for inferreed in infer:
        if "jointime: " in inferreed:
            inferreedplit = inferreed.split('jointime: ')
            jointime = inferreedplit[1].rstrip('\n')
        if "distag: " in inferreed:
            inferreedplit = inferreed.split('distag: ')
            distag = inferreedplit[1].rstrip('\n')
        if "diswebhook: " in inferreed:
            inferreedplit = inferreed.split('diswebhook: ')
            diswebhook = inferreedplit[1].rstrip('\n')
        if "timeoutprompt: " in inferreed:
            inferreedplit = inferreed.split('timeoutprompt: ')
            timeoutprompt = inferreedplit[1].rstrip('\n')
        if "soundwarning: " in inferreed:
            inferreedplit = inferreed.split('soundwarning: ')
            soundwarning = inferreedplit[1].rstrip('\n')
        if "warningpos: " in inferreed:
            inferreedplit = inferreed.split('warningpos: ')
            warningpos = inferreedplit[1].rstrip('\n')
        if "timeoutpos: " in inferreed:
            inferreedplit = inferreed.split('timeoutpos: ')
            timeoutpos = inferreedplit[1].rstrip('\n')
        if "reconnect: " in inferreed:
            inferreedplit = inferreed.split('reconnect: ')
            reconnect = inferreedplit[1].rstrip('\n')
        if "timesleep: " in inferreed:
            inferreedplit = inferreed.split('timesleep: ')
            reconnect = inferreedplit[1].rstrip('\n')

warningpos = int(warningpos)
timeoutpos = int(timeoutpos)
timesleep = int(timesleep)

print ("Will join 2b2t at " + jointime)
print ("Starting...")
repit = 1
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print ("Checking time...")
    if current_time == jointime:
        while True:
            logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
            loglines = follow(logfile)
            print ("Started at " + current_time)
            try:
                webhook = DiscordWebhook(url=diswebhook, content=("Started at " + current_time))
                webhook.execute()
            except:
                print ("Could not reach discord")
            if processImage('assets/2b2tlogo/2b2tlogoauto.png'):
                doubleclick_image('assets/2b2tlogo/2b2tlogoauto.png')
            elif processImage('assets/2b2tlogo/2b2tlogolarge.png'):
                doubleclick_image('assets/2b2tlogo/2b2tlogolarge.png')
            elif processImage('assets/2b2tlogo/2b2tlogonormal.png'):
                doubleclick_image('assets/2b2tlogo/2b2tlogonormal.png')
            elif processImage('assets/2b2tlogo/2b2tlogosmall.png'):
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
                        time.sleep(timesleep)
                        if reconnect == 'n' or reconnect == 'no':
                            while True:
                                time.sleep(69420)
                        else:
                            break
                    elif queuepos1 < warningpos:
                        try:
                            webhook = DiscordWebhook(url=diswebhook, content=linechat[1] + ' ' + distag)
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
                            webhook = DiscordWebhook(url=diswebhook, content=linechat[1])
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
                        try:
                            webhook = DiscordWebhook(url=diswebhook, content=("Uh oh! Something went wrong. Attempting to reconnect..."))
                            webhook.execute()
                        except:
                            pass
                        time.sleep(timesleep)
                        break
                    elif processImage('assets/backtoserverlist/btsllarge.png'):
                        click_image('assets/backtoserverlist/btsllarge.png')
                        try:
                            webhook = DiscordWebhook(url=diswebhook, content=("Uh oh! Something went wrong. Attempting to reconnect..."))
                            webhook.execute()
                        except:
                            pass
                        time.sleep(timesleep)
                        break
                    elif processImage('assets/backtoserverlist/btslnormal.png'):
                        click_image('assets/backtoserverlist/btslnormal.png')
                        try:
                            webhook = DiscordWebhook(url=diswebhook, content=("Uh oh! Something went wrong. Attempting to reconnect..."))
                            webhook.execute()
                        except:
                            pass
                        time.sleep(timesleep)
                        break
                    elif processImage('assets/backtoserverlist/btslsmall.png'):
                        click_image('assets/backtoserverlist/btslsmall.png')
                        try:
                            webhook = DiscordWebhook(url=diswebhook, content=("Uh oh! Something went wrong. Attempting to reconnect..."))
                            webhook.execute()
                        except:
                            pass
                        time.sleep(timesleep)
                        break
                    else:
                        pass
    time.sleep(10)