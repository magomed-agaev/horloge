from tkinter import Tk
from tkinter import Label
import time
import sys
import time
import winsound

master = Tk()
master.title("Horloge Digitale")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    timeVar = time.strftime("%I:%M:%S %a")
    horloge.config(text=timeVar)
    horloge.after(200,get_time)
    
def set_alarm(alarm_time):
    while True:
        horloge = time.strftime("%H:%M:%S")
        if horloge == alarm_time:
            print("Alarm! It's", alarm_time)
            
            winsound.Beep(1000, 1000)  
            break
        time.sleep(1)  

alarm_time = "12:02:00"  
set_alarm(alarm_time)

horloge = Label(master, font=("Calibri",90),bg="green",fg="black")
horloge.pack()

get_time()

master.mainloop()



