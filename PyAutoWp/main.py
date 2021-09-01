import pyautogui as pg
import webbrowser as web
import pandas as pd

import pytz
from pytz import timezone
from time import sleep
from datetime import datetime

def windowCheck():
	web.open("https://web.whatsapp.com/")
	pg.alert("Login to whatsapp web from your default browser and make the window full screen." + 
		"\nDon't forget to check the Keep me signed in option."+ 
		"\n(You can close the window after making it full screen.)")

def windowOpen(link,sleepTime = 8):
	web.open(link)
	sleep(4)
	
	screenSize = pg.size()
	width,height = screenSize[0]/2,screenSize[1]/2
	pg.click(x=width, y=height, clicks=1, button='left')
	
	sleep(sleepTime-5)

def windowClose():
	sleep(1)
	pg.hotkey("ctrl", "w")

def differentCountryTimer():
	t = input("Enter the date and time to send the message (example: day.month.year 21:00): ")

	tz = input("Country Abbreviations (example: tr, us etc.): ")
	tz_list = pytz.country_timezones[tz]
	num = 1
	tz_dic = {}
	for i in tz_list:
		tz_dic[num] = i
		print(str(num) + " - " + str(tz_dic[num]))
		num = num+1

	tz_val = int(input("Please enter the location number to which you will send the message (example: 1, 2, 3 etc.): "))

	format = "%d-%m-%Y %H:%M"
	 
	while True:
		# Current time in UTC
		now_utc = datetime.now(timezone('UTC'))

		# Convert to x time zone
		now_x = (now_utc.astimezone(timezone(tz_dic[tz_val]))).strftime(format)

		later_x = datetime.strptime(t,"%d.%m.%Y %H:%M").strftime(format)

		if now_x == later_x:
			return True

def sendMessage(phoneNumber, message, internationalTelephoneCodes = "90"):
	windowOpen(f"https://web.whatsapp.com/send?phone={internationalTelephoneCodes}{phoneNumber}&text={message}")
	
	pg.press('enter')

	windowClose()

def readPhoneNumber(path):
	phoneInfo = pd.read_excel(path)
	return phoneInfo

def sendMultipleMessage(path, message):

	phoneInfo=readPhoneNumber(path)

	for i in range(0, int(phoneInfo.size/3)):
		phone_data = phoneInfo.loc[i]

		name = phone_data["Name"]
		phoneNumber = phone_data["Phone Number"]
		internationalTelephoneCodes = 90 if phone_data["Country Phone Codes"] !=  phone_data["Country Phone Codes"] else int(phone_data["Country Phone Codes"])
		
		sendMessage(phoneNumber, message, internationalTelephoneCodes)
	