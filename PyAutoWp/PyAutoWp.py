import wp
import check
from threading import Thread

check.windowCheck()

while True:
	a = input("Please choose an option:\n1-I will send my message to many people.\n2-I will send my message to 1 person.")
	if a == "1":
		phoneNumberData = check.phoneListCheck()
		phoneNumberData = wp.contacts_df_edit(phoneNumberData)
		message = check.messageCheck()
		a = check.timerCheck()
		if a == True:
			t = input("Enter the date and time to send the message (example: day.month.year 21:00): ")
			tz = list(map(wp.differentCountryTimer,phoneNumberData["Phone Number"]))
			phoneNumberData["tz"] = tz

			tz_list = list(set(tz))
			th_list = []
			pnd = []

			for i in tz_list:
				if i == "Etc/Unknown":
					continue
				pnd.append(phoneNumberData[phoneNumberData.tz == i])
				th_list.append(Thread(target = wp.timer, args = (i,t)))
			for i in range(len(th_list)):
				th_list[i].start()
			print(pnd)

			tfl = [None] * len(th_list)
			x = 0
			while True:
				if x == len(th_list):
					x = 0
				if len(th_list) == 0:
					break

				tfl[x] = (th_list[x].is_alive())
    			
				print(tfl)

				if False in tfl:
					wp.sendMultipleMessage(pnd[x],message)
					th_list.pop(x)
					tfl.pop(x)
					pnd.pop(x)

				x = x +1

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




