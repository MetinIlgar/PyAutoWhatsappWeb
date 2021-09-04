import wp
import check

check.windowCheck()

while True:
	a = input("Please choose an option:\n1-I will send my message to many people.\n2-I will send my message to 1 person.")
	if a == "1":
		phoneNumberData = check.phoneListCheck()
		phoneNumberData = wp.contacts_df_edit(phoneNumberData)
		message = check.messageCheck()
		a = check.timerCheck()
		print(phoneNumberData)
		if a == True:
			tz = list(map(wp.differentCountryTimer,phoneNumberData["Phone Number"]))
			print(tz)

			phoneNumberData["tz"] = tz
			phoneNumberData = phoneNumberData.groupby(["tz", "Phone Number"])
			print(phoneNumberData.first())


		elif a == False:
			wp.sendMultipleMessage(phoneNumberData,message)




		break
	elif a == "2":
		message = check.messageCheck()
		phoneNumber = check.phoneNumberCheck()
		wp.sendMessage(str(phoneNumber),message)
		print("Message sent.")
		break
	else:
		print("Please select a valid option. 1 or 2")




