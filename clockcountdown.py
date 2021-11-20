# Python program to illustrate a stop watch
# using Tkinter
#importing the required libraries
import tkinter as Tkinter
from tkinter import *
from tkinter import font
from tkinter.ttk import *
from datetime import datetime
from time import strftime
counter = 66600
running = False

def counter_label(label):
	def count():
		if running:
			global counter

			# To manage the initial delay.
			if counter==66600:			
				display="Starting..."
			else:
				tt = datetime.fromtimestamp(counter)
				string = tt.strftime("%H:%M:%S")
				display=string

			label['text']=display # Or label.config(text=display)

			# label.after(arg1, arg2) delays by
			# first argument given in milliseconds
			# and then calls the function given as second argument.
			# Generally like here we need to call the
			# function in which it is present repeatedly.
			# Delays by 1000ms=1 seconds and call count again.
			label.after(1000, count)
			counter += 1

	# Triggering the start of the counter.
	count()	

# start function of the stopwatch
def Start(label):
	global running
	running=True
	counter_label(label)
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'

# Stop function of the stopwatch
def Stop():
	global running
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	running = False

# Reset function of the stopwatch
def Reset(label):
	global counter
	counter=66600

	# If rest is pressed after pressing stop.
	if running==False:	
		reset['state']='disabled'
		label['text']='Welcome!'

	# If reset is pressed while the stopwatch is running.
	else:			
		label['text']='Starting...'

def clock():
	tick = strftime('%H:%M:%S %p')

	clock_label .config(text =tick)

	clock_label .after(1000, clock)



root = Tkinter.Tk()
root.title("Countdown Clock And Timer")
root.iconphoto(False,PhotoImage(file='clock.png'))
root.geometry("800x500")

# Fixing the window size.
root.minsize(width=650, height=500)
Font_tuple = ("Calibri", 20, "bold")
label = Tkinter.Label(root, text="Countdown Clock And Timer", fg="black", font=Font_tuple)

label.pack(pady=50)
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))
stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=50)
#------------------------------------------------------------------
clock_label = Label(root, font=('sans', 80), background = 'white', foreground = 'brown')

clock_label.pack(anchor='center')

start.pack(side="left",padx=5)
stop.pack(side ="left",padx=5)
reset.pack(side="left",padx=5)
clock()
root.mainloop()
