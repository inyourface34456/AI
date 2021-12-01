import os
os.system('/opt/virtualenvs/python3/bin/python3 -m pip install --upgrade pip')
os.system('pip install webbot')
os.system('pip install getkey')
import webbot
import time
import random
from getkey import *
os.system('pip3 install pyautogui')
driver = webbot.Browser()
driver.go_to('google.com')

while True: 
	key = getkey()
	if key == '!':
		driver.type("!")
	driver.go_to('medium.com/@FGrante/how-to-install-a-chrome-extension-without-using-the-chrome-web-store-31902c780034')