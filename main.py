# You could probably get your account auto banned for this, be careful

import pyautogui, time

# How long until the bot begins spamming.
WaitTime = 10
# This will type 'Done!' when the script has finished. It won't send it, rather it will show typed in the text box
DoneMessage = 'true'
# For social medias which have a message cool down, mainly for Discord.
ChillZone = 'false'

time.sleep(WaitTime)
b = open("script", 'r')

for word in b:
    if ChillZone == 'true':
        time.sleep(3)

    pyautogui.typewrite(word)
    pyautogui.press("enter")

if DoneMessage == 'true':
    pyautogui.typewrite("Done!")
else: exit()
