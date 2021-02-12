# You could probably get your account banned or reported for this, be careful // Discord: ryann#7322
import pyautogui
import time

WaitTime = 7  # How long until the bot begins spamming. Default = 7
DoneMessage = 'true'  # This will type 'Done!' when the script has finished. Default = 'true'
ChillZone = 'false'  # For social medias which have a message cool down, mainly for Discord. Default = 'false'
MessageDelay = 0  # How many seconds between each message. Default = 0

time.sleep(WaitTime)
sb = open("script.txt", 'r')

for word in sb:
    if ChillZone == 'true':
        time.sleep(1.7)

    time.sleep(MessageDelay)
    pyautogui.typewrite(word)
    pyautogui.press("enter")

if DoneMessage == 'true':
    pyautogui.typewrite("Done!")
