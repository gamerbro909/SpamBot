# You could probably get your account banned or reported for this, be careful // Discord: ryann#7322
# Version 1.7 // Requires Config 1.1
import pyautogui
import time
from ruamel.yaml import YAML
import keyboard

yaml = YAML()

with open("./config.yml", "r", encoding="utf-8") as file:
    config = yaml.load(file)

time.sleep(config['WaitTime'])
if config['script_loop'] == True:
    while keyboard.is_pressed(config['stop_key']) == False:
        sb = open("script.txt", 'r')
        if config['ChillZone'] == 'true':
            time.sleep(1.2)
        
        for word in sb:
            time.sleep(config['MessageDelay'])
            pyautogui.typewrite(word)
            pyautogui.press("enter")
    else:
        exit("Finished Loop")

if config['script_loop'] == False:
    while keyboard.is_pressed(config['stop_key']) == False:
        sb = open("script.txt", 'r')
        if config['ChillZone'] == 'true':
            time.sleep(1.7)

        for word in sb:
            time.sleep(config['MessageDelay'])
            pyautogui.typewrite(word)
            pyautogui.press("enter")
        exit("Finished!")
