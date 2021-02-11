# You could probably get your account auto banned for this, be careful

import pyautogui, time

# How long until the bot begins spamming.
WaitTime = 10

time.sleep(WaitTime)
b = open("script", 'r')
for word in b:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
