from tkinter import *
from time import strftime


def timer(): 
    string = strftime("%H:%M:%S")
    label.config(text=string)
    label.after(1000,timer)

root = Tk()
root.title('Digital Clock')
label = Label(root,font=('ds-digital',80),bg='black',fg='white')
label.pack(anchor='center')
timer()
root.mainloop()