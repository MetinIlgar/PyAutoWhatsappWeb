import pyautogui as pg
import webbrowser as web
import pandas as pd

import pytz
from pytz import timezone
from time import sleep
from datetime import datetime

def windowCheck():
	web.open("https://web.whatsapp.com/")
	pau.alert("Login to whatsapp web from your default browser and make the window full screen." + 
		"\nDon't forget to check the Keep me signed in option."+ 
		"\n(You can close the window after making it full screen.)")

def windowOpen(link,sleepTime = 8):
	web.open(link)
	sleep(4)
	
	screenSize = pau.size()
	width,height = screenSize[0]/2,screenSize[1]/2
	pau.click(x=width, y=height, clicks=1, button='left')
	
	sleep(sleepTime-5)

def windowClose():
	sleep(1)
	pau.hotkey("ctrl", "w")

