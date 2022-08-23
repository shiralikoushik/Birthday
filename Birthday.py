import csv
import time
import tkinter
import os
os.chdir(r"c:\Users\sio2kor\Documents\Birthday")
root = tkinter.Tk()
root.title("Birthday Reminder")
root.geometry("550x200")
today = time.strftime('%m%d')
count = 0
with open("date_name.csv","r") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        if line[0] == today:
            dob = tkinter.Label(text= f"Yay! It's {line[1]}'s Birthday Today",font=("Lucida Calligraphy",16,"bold"))
            dob.pack()
            count = 1
if not count:
    dob = tkinter.Label(text="No Birthday today")
    dob.pack()
root.mainloop()

