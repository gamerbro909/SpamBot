# You could probably get your account auto banned for this, be careful
import pyautogui, time

WaitTime = 10 # How long until the bot begins spamming.
DoneMessage = 'true' # This will type 'Done!' when the script has finished. It won't send it, rather it will show typed in the text box
ChillZone = 'false' # For social medias which have a message cool down, mainly for Discord.
ChillZoneTime = 1 # If ChillZone is enabled, this is how long the cooldown is
SlashFix = 'true' # This is a potential fix for /'s breaking on certain platforms.
ShowDebug = 'false' # Shows Debug Messages in console

if ShowDebug == 'true':
    print("WaitTime =", WaitTime)
    print("DoneMessage =", DoneMessage)
    print("ChillZone =", ChillZone)
    print("ChillZoneTime =", ChillZoneTime)

time.sleep(WaitTime)
b = open("script", 'r')

for word in b:
    if ChillZone == 'true':
        time.sleep(ChillZoneTime)

    pyautogui.typewrite(word)
    pyautogui.press("enter")
    if ShowDebug == 'true':
        print("Sent:", word)

    if SlashFix == 'true':
        pyautogui.press("enter")

if DoneMessage == 'true':
    pyautogui.typewrite("Done!")
    print("Done!")
else: exit()
