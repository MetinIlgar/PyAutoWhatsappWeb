import main

def windowCheck():
	main.web.open("https://web.whatsapp.com/")
	main.pg.alert("Login to whatsapp web from your default browser and make the window full screen." + 
		"\nDon't forget to check the Keep me signed in option."+ 
		"\n(You can close the window after making it full screen.)")

def phoneNumberCheck():
	while True:
		while True:
			try:
				phoneNumber = main.wcb("Please enter the phone number you want to send.","(eg: +905123456789): ")
				phone_number = main.phonenumbers.parse(phoneNumber)
				break
			except:
				print(main.Fore.WHITE + main.Back.RED + main.Style.BRIGHT + "Please enter a valid phone number.")
				print(main.Style.RESET_ALL)

		valid = main.phonenumbers.is_valid_number(phone_number)
		possible = main.phonenumbers.is_possible_number(phone_number)

		if valid == False or possible == False:
			print(main.Fore.WHITE + main.Back.RED + main.Style.BRIGHT + "Please enter a valid phone number.")
			print(main.Style.RESET_ALL)
		else:
	  		break
	return  (str(phone_number.country_code) + str(phone_number.national_number))
def messageCheck():
	while True:
		message = main.wcb("Please enter the message you want to send","Message: ")
		if message == "":
			print(main.Fore.WHITE + main.Back.RED + main.Style.BRIGHT + "Please enter a valid phone message.")
			print(main.Style.RESET_ALL)
		else:
			break
	return message


def phoneListCheck():
	while True:
		a = main.wcbo("Select option to import phone list:\n1-From Excel\n2-From vCard", "1 or 2: ", ["1","2"])
		try:
			n = main.wcb("Enter the file path." , "Path: ")
			if a == "1":
				phoneNumberData = main.readPhoneNumber(n)
				break
			elif a == "2":
				phoneNumberData = main.vcfReader(n,"Phone_Number_Data.xlsx")
				break
		except:
			print(main.Fore.WHITE + main.Back.RED + main.Style.BRIGHT + "There is no such file in this path.")
			print(main.Style.RESET_ALL)

	return phoneNumberData

def timerCheck():
	while True:
		a = main.wcbo("Do you want to use a timer?,", "(Y/N): ", ["Y","y","N","n"])
		if a == "y" or a == "Y":
			return True
			break

		elif a == "n" or a == "N":
			return False
			break
