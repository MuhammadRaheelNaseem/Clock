from tkinter import *
from time import strftime

clock = Tk()
clock.title('Clock')
clock.geometry('370x60')

def time():
    string = strftime('%I:%M:%S %p')
    clock_lbl.config(text = string)
    clock_lbl.after(1000, time)

clock_lbl = Label(clock, font = ('calibri', 40, 'bold'),background ="black",foreground = 'white')
clock_lbl.pack(anchor = 'center')
time()

mainloop()
