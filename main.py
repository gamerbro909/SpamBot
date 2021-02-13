# You could probably get your account banned or reported for this, be careful // Discord: ryann#7322
import pyautogui
import time
from ruamel.yaml import YAML

yaml = YAML()

with open("./config.yml", "r", encoding="utf-8") as file:
    config = yaml.load(file)


time.sleep(config['WaitTime'])
sb = open("script.txt", 'r')

for word in sb:
    if config['ChillZone'] == 'true':
        time.sleep(1.7)

    time.sleep(config['MessageDelay'])
    pyautogui.typewrite(word)
    pyautogui.press("enter")

if config['DoneMessage'] == 'true':
    pyautogui.typewrite("Done!")
