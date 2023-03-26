
# importing all the required libraries available in python to build alaram clock with mentioned requirements
from tkinter import *
import datetime
from threading import *
import winsound
import time


# Creating the Object
myalarm= Tk()

# Setting geometry 
myalarm.geometry("500x250")

# defing the MyThreading
def MyThreading():
	my_thread=Thread(target=myalarm)
	my_thread.start()

def alarm_clock():
	# Here it is a Infinite Loop
	while True:
		# Now  set the  Alarm
		alarms_time = f"{hour.get()}:{minute.get()}:{second.get()}"

		# Let us wait for one seconds
		time.sleep(1)

		# Now  Get current time
		present_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(present_time,alarms_time)

		# Now Check whether set alarm is equal to present time or not
		if present_time == alarms_time:
			print("Its Time to Wake up!!!!")
			# It will play the  ringing alarm  sound
			winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

# Adding Frame, Labels,  Optionmenus and  Button
Label(myalarm,text="My Alarm Clock",font=("Helvetica 23 bold"),fg="blue").pack(pady=10)
Label(myalarm,text="Set The  Time",font=("Helvetica 17 bold")).pack()

frame = Frame(myalarm)
frame.pack()

hour = StringVar(myalarm)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(myalarm)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(myalarm)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=RIGHT)

Button(myalarm,text="Set Now",font=("Helvetica 17"),command=MyThreading).pack(pady=25)

# Executing Tkinter
myalarm.mainloop()

