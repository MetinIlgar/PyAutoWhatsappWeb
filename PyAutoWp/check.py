import wp

def windowCheck():
	wp.web.open("https://web.whatsapp.com/")
	wp.pg.alert("Login to whatsapp web from your default browser and make the window full screen." + 
		"\nDon't forget to check the Keep me signed in option."+ 
		"\n(You can close the window after making it full screen.)")

def phoneNumberCheck():
	while True:
		while True:
			try:
				phoneNumber = input("Please enter the phone number you want to send (eg: +905123456789): ")
				phone_number = wp.phonenumbers.parse(phoneNumber)
				break
			except:
				print("Please enter a valid phone number.")


		valid = wp.phonenumbers.is_valid_number(phone_number)
		possible = wp.phonenumbers.is_possible_number(phone_number)

		if valid == False or possible == False:
	  		print("Please enter a valid phone number.")
		else:
	  		break
	return  (str(phone_number.country_code) + str(phone_number.national_number))
def messageCheck():
	while True:
		message = input("Please enter the message you want to send: ")
		if message == "":
			print("Please enter a valid message.")
		else:
			break
	return message


def phoneListCheck():
	while True:
		a = input("Select option to import phone list:\n1-From Excel\n2-From vCard: ")
		if a == "1":
			n = input("Enter the file path:")
			phoneNumberData = wp.readPhoneNumber(n)
			break
		elif a == "2":
			n = input("Enter the file path:: ")
			phoneNumberData = wp.vcfReader(n,"Phone_Number_Data.xlsx")
			break
		else:
			print("Please select a valid option. 1 or 2")
		

	return phoneNumberData

def timerCheck():
	while True:
		a = input("Do you want to use a timer? (Y/N):")
		if a == "y" or a == "Y":
			return True
			break

		elif a == "n" or a == "N":
			return False
			break

		else:
			print("Please select a valid option. Y(es) or N(o)")
