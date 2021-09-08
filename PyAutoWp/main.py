import pyautogui as pg
import webbrowser as web
import pandas as pd
import quopri
import pytz
from pytz import timezone
from time import sleep
from datetime import datetime
import phonenumbers
from phonenumbers import timezone as tiz

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

def differentCountryTimer(phoneNumber):
	try : 
		phoneNumber = phonenumbers.parse(phoneNumber)
		time_Zone = tiz.time_zones_for_number(phoneNumber)
		if len(time_Zone) != 1:
			x = 1
			for i in time_Zone:
				print(f"{x}{i}")
				x = x + 1
			live_in = int(input("Please enter the location number to which you will send the message (example: 1, 2 etc.): ")) - 1
			return str(time_Zone[live_in])		
		else:
			return str(time_Zone[0])

	except:
		tz = input("Country Abbreviations (example: tr, us etc.): ")
		tz_list = pytz.country_timezones[tz]
		num = 1
		tz_dic = {}
		for i in tz_list:
			tz_dic[num] = i
			print(str(num) + " - " + str(tz_dic[num]))
			num = num+1

		tz_val = int(input("Please enter the location number to which you will send the message (example: 1, 2, 3 etc.): "))

		return str(tz_dic[tz_val])

def timer(tz,t):
	format = "%d-%m-%Y %H:%M"
	while True:
		# Current time in UTC
		now_utc = datetime.now(timezone('UTC'))

		# Convert to x time zone
		now_x = (now_utc.astimezone(timezone(tz))).strftime(format)

		later_x = datetime.strptime(t,"%d.%m.%Y %H:%M").strftime(format)

		if now_x == later_x:
			break		

def sendMessage(phoneNumber, message):
	windowOpen(f"https://web.whatsapp.com/send?phone={phoneNumber}&text={message}")
	
	pg.press('enter')

	windowClose()

def readPhoneNumber(path):
	phoneInfo = pd.read_excel(path)
	return phoneInfo

def sendMultipleMessage(PhoneNumberData, message):

	for i in PhoneNumberData.index:
		phone_data = PhoneNumberData.loc[i]

		name = phone_data["Name"]
		phoneNumber = phone_data["Phone Number"]
		
		sendMessage(phoneNumber, message)
	
def vcfReader(path, fileName):
	contacts = {}
	with open(path, "r") as f:
		numPerson = 0

		while True:
			numPerson = 1 + numPerson
			contacts[numPerson] = {}
			while True:
				i = f.readline()
				
				if "FN" in i:
					_ ,val= i.split(":")
					key = "Name"
					val = val.replace("\n", "")

					if "=" in val: val = quopri.decodestring(val).decode('utf-8')

					contacts[numPerson][key] = val

				elif "TEL" in i:
					_ ,val= i.split(":")
					key = "Phone Number"

					val = val.replace("\n", "")
					val = val.replace("-", "")

					contacts[numPerson][key] = val

					if "+" in val:
						contacts[numPerson]["Country Phone Codes"] = str(phonenumbers.parse(val).country_code)

					break

				elif i == "":
					contacts.pop(numPerson)
					contacts_df = pd.DataFrame(contacts).T

					contacts_df.to_excel(fileName, index = False)
					return contacts_df

def contacts_df_edit(contacts_df):
	print(contacts_df)
	k=input("Is there a phone number you want to remove from the list? (Y/N): ")
	print("_______________________________________________________________________")
	if k == "Y" or k == "y":
		delete_num=input("Write the sequence numbers of the phone numbers you want to remove from the list, separating them with commas (eg 1,2,3):")
		print("_______________________________________________________________________")
		delete_list=delete_num.split(",")
		for m in delete_list:
			print(contacts_df.loc[int(m)]["Name"]," has been deleted.")
			contacts_df.drop(int(m), axis = 0, inplace = True)
		print("_______________________________________________________________________")

	if contacts_df.isnull().values.any() == True:
		NANdata= contacts_df.isnull().sum()
		if NANdata["Name"] != 0:
			print(f"There are {str(NANdata['Name'])}  missing names in the list of names.")

		if NANdata["Phone Number"] != 0:
			print(f"There are {str(NANdata['Phone Number'])} missing numbers in the phone list.")

		if NANdata["Country Phone Codes"] != 0:
			print(f"There are {NANdata['Country Phone Codes']} missing country phone codes in the country phone codes list.")
			print("_______________________________________________________________________")
			x=input("Enter 1 if you want to assign collectively, \nenter 2 if you want to assign one by one, \nand 0 if you do not want to assign. \n(If you do not assign, your message will not be forwarded to those people.): ")
			print("_______________________________________________________________________")
			isnullList=contacts_df['Country Phone Codes'].isnull()
			index_list = (isnullList[isnullList==True].index)
			if x == "1":
				cc = input("Enter the country code you want to bulk assign. (eg 90.):")
				contacts_df['Country Phone Codes'].fillna(cc, inplace = True)
				print("_______________________________________________________________________")

			if x == "2":
				for i in index_list:
					print(contacts_df.loc[i]["Name"]+": "+contacts_df.loc[i]["Phone Number"])
					n = input("Country Phone Codes for this contact: ")
					contacts_df.loc[i]['Country Phone Codes'] = n
					print("-------------------------------")
			if x == "0":
				contacts_df.dropna(inplace = True)
	
	for i in index_list:
		  contacts_df.loc[i]["Phone Number"] = "+" + contacts_df.loc[i]["Country Phone Codes"] + contacts_df.loc[i]["Phone Number"]
	
	contacts_df.drop("Country Phone Codes", inplace=True, axis=1)

	return contacts_df		