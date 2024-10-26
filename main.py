from idlelib.colorizer import color_config
from tkinter import *
import random
a = [random.randint(0, 10)]
print(a[0])
def guess_func():
    user = int(spinbox.get())
    if user == a[0]:
        result.delete(0.0, END)
        result.insert(END, f"Congratulations! You guess the correct number.")
    elif user<a[0]:
        result.delete(0.0, END)
        result.insert(END, f"Please increase the number. You are very close enough.")
    elif user>a[0]:
        result.delete(0.0, END)
        result.insert(END, f"Please decrease the number. You are very close enough.")

window = Tk()
window.geometry('800x500')
window.title("Hi-Lo Number Game")

progName = Label(window,font=("The Font",25,"bold"),text="Guess The Number!",fg="RoyalBlue",justify=CENTER)
progName.place(relx=0.30,rely=0.07)

spinbox = Spinbox(window, from_=0, to=10, width=5,bd=0,font=("The Font",40,"bold"),justify=CENTER,fg='RoyalBlue',bg="LightSkyBlue")
spinbox.place(relx=0.4,rely=0.25)
spinbox.config(state="readonly")

guess = Button(window,text="Guess Now!",font=("The Font",15,"bold"),fg="RoyalBlue",command=guess_func)
guess.place(relx=0.415,rely=0.5)

result = Text(window,height=6,width=65,font=("The Font",15,"bold"),fg="Chocolate",bg="NavajoWhite")
result.place(relx=0.05,rely=0.65)

window.mainloop()
