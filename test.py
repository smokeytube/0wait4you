import time, os
from datetime import datetime
import time
import pyautogui
import win32api, win32con
from discord_webhook import DiscordWebhook


jointime = input("What time do you want to join? (24 hour time, HOUR:MINUTE ex. 22:37): ")

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    if current_time == jointime:
        print ("got here")
        def follow(thefile):
            thefile.seek(0,2)
            while True:
                line = thefile.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                yield line

            logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
            loglines = follow(logfile)
            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/791062578259820554/iQf1YuL4QAPogIPiL6cVnjOafCUOQuT190WnMLaVqSGMLOoR63cjGarVTO0M0brctep9', content=("Started at " + current_time))
            webhook.execute()
            x = 0
            for line in loglines:
                if "[Client thread/INFO]: [CHAT]" in line and x == 5:
                    try:
                        linearr = line.split('[CHAT] ')
                        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/791062578259820554/iQf1YuL4QAPogIPiL6cVnjOafCUOQuT190WnMLaVqSGMLOoR63cjGarVTO0M0brctep9', content=linearr[1])
                        webhook.execute()
                        x = 0
                    except:
                        pass
                else:
                    x = x + 1
    time.sleep(10)