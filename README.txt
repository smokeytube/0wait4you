How information.txt should be filled out:
-----------------------------------------

jointime: HOUR:MINUTE (what time to join. 24 hour time and for single digit hours you have to put a zero in front ex. 04:00 (4am) or 02:30 (2:30 am))
distag: <@YOUR_DISCORD_ID> (usersettings -> 3 dots next to your profile picture -> copy ID)
diswebhook: YOURWEBHOOK (yourchannel -> settings -> integrations -> create webhook)
timeoutprompt: y OR n (if you want to disconnect at a certian queue position for if you are afk)
warningpos: ANY NUMBER (what queue position to start pinging you at)
soundwarning: y OR n (play an alarm when at a certian queue position)
timeoutpos: ANY NUMBER (what queue position to disconnect at (ONLY WORKS IF timeoutprompt IS YES OR Y))
reconnect: y OR n (reconnect after you disconnect to be put back in the queue)
timesleep: ANY NUMBER (how long to sleep in seconds if you get disconnected from 2b2t or server restarts (reccomend 30-60 seconds))


Example:
---------

jointime: 04:00
distag: <@here>
diswebhook: https://discord.com/api/webhooks/YOURWEBHOOK/URL
timeoutprompt: y
warningpos: 50
soundwarning: y
timeoutpos: 5
reconnect: y
timesleep: 30