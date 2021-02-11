# You could probably get your account auto banned for this, be careful // Discord: ryann#7322
import pyautogui
import time

WaitTime = 7  # How long until the bot begins spamming. Default = 7
DoneMessage = 'true'  # This will type 'Done!' when the script has finished. Default = 'true'
ChillZone = 'true'  # For social medias which have a message cool down, mainly for Discord. Default = 'true'
ChillZoneTime = 1  # If ChillZone is enabled, this is how long the cool down is. Default = 1

time.sleep(WaitTime)
b = open("script", 'r')

for word in b:
    if ChillZone == 'true':
        time.sleep(ChillZoneTime)

    pyautogui.typewrite(word)
    pyautogui.press("enter")
    pyautogui.press("enter")

    if DoneMessage == 'true':
        pyautogui.typewrite("Done!")
        print("Done!")

exit()
