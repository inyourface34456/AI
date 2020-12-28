import webbot
import os
import time
import random
from getkey import *
os.system('pip3 install pyautogui')
os.system('/opt/virtualenvs/python3/bin/python3 -m pip install --upgrade pip')
driver = webbot.Browser()
driver.go_to('google.com')

while True: 
	key = getkey()
	if key == '!':
		driver.type("!")
	driver.go_to('google.com')