from tkinter import *
from datetime import datetime
from time import strftime
from tkinter.font import BOLD

WIN =  Tk()
WIN.maxsize(480, 120)
WIN.resizable(False, False)
WIN.configure(bg="black")
WIN.title("DIGITAL CLOCK") 

def stay_on_top():
   WIN.lift()
   WIN.after(2000, stay_on_top)

a = datetime.today().strftime("%A")
b = (a.upper())
c = (b[0:2]) 

frame =  Frame(WIN, width=750, height=200, bg="black")
frame.pack(expand=True)

def time():

    a = strftime("%H : %M : %S")
    label.config(text= a)
    label.after(1000, time)

label = Label(frame, font=("Century Gothic", 50), bg="black", fg="white")

label.place(x= 32, y=15)
time()

label1 = Label(frame, font=('Century Gothic',50), bg='black', fg='white')
label1.config(text=c)
label1.place(x=358, y=15)

label1 = Label(frame, font=('Century Gothic',50), bg='black', fg='white', text='|')
label1.place(x=300, y=10)

def labels():

    l3=Label(frame, font=('Century Gothic',10),bg='#0e1013',fg='#7f7f7f',text='DAY')
    l3.place(x=378, y=80)

    l4=Label(frame, font=('Century Gothic',10),bg='#0e1013',fg='#7f7f7f',text='HOURS')
    l4.place(x=48, y=80)

    l5=Label(frame, font=('Century Gothic',10),bg='#0e1013',fg='#7f7f7f',text='MINUTES')
    l5.place(x=134, y=80)
 
    l3=Label(frame, font=('Century Gothic',10),bg='#0e1013',fg='#7f7f7f',text='SECONDS')
    l3.place(x=230, y=80)

labels()

WIN.mainloop()