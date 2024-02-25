"""
Nama    : Aryo Sheva Ramadhani
NIM     : 215150307111009
"""

from tkinter import *

window = Tk()

def convert():
    try:
        km = float(e1_value.get())*1.609
    
        t1.configure(state='normal')
        t1.delete("1.0", END)
        t1.insert(END, km)
        t1.configure(state='disabled')
    except:
        t1.configure(state='normal')
        t1.delete("1.0", END)
        t1.configure(state='disabled')

    try:
        meter = float(e2_value.get())*0.914
    
        t2.configure(state='normal')
        t2.delete("1.0", END)
        t2.insert(END, meter)
        t2.configure(state='disabled')
    except:
        t2.configure(state='normal')
        t2.delete("1.0", END)
        t2.configure(state='disabled')

    try:
        cm = float(e3_value.get())*2.54
    
        t3.configure(state='normal')
        t3.delete("1.0", END)
        t3.insert(END, cm)
        t3.configure(state='disabled')
    except:
        t3.configure(state='normal')
        t3.delete("1.0", END)
        t3.configure(state='disabled')

window.title("Length Converter")

l1=Label(window, text="Enter Miles: ")
l2=Label(window, text="Enter Yards: ")
l3=Label(window, text="Enter Inches: ")
l4=Label(window, text="Equal to: ")
l5=Label(window, text="Kilometer")
l6=Label(window, text="Equal to: ")
l7=Label(window, text="Meter")
l8=Label(window, text="Equal to: ")
l9=Label(window, text="Centimeter")

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3_value = StringVar()
e3 = Entry(window, textvariable=e3_value)

t1 = Text(window, height = 1, width = 20, state='disabled')
t2 = Text(window, height = 1, width = 20, state='disabled')
t3 = Text(window, height = 1, width = 20, state='disabled')

b1 = Button(window, text = "Convert", command = convert)

l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
l4.grid(row=1, column=0)
t1.grid(row=1, column=1)
l5.grid(row=1, column=2)
l2.grid(row=2, column=0)
e2.grid(row=2, column=1)
l6.grid(row=3, column=0)
t2.grid(row=3, column=1)
l7.grid(row=3, column=2)
l3.grid(row=4, column=0)
e3.grid(row=4, column=1)
l8.grid(row=5, column=0)
t3.grid(row=5, column=1)
l9.grid(row=5, column=2)
b1.grid(row=6, column=1)

window.mainloop()