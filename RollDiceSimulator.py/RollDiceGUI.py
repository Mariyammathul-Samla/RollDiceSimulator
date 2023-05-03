import tkinter as tk
from PIL import Image,ImageTk
import random

window=tk.Tk()
window.geometry("5000x3600")
window.title("Dice-Roll")
window['bg']='plum'
dice=["dice1.jpeg","dice2.jpeg","dice3.jpeg","dice4.jpeg","dice5.jpeg","dice6.jpeg"]
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1=tk.Label(window,image=image1)
label2=tk.Label(window,image=image2)

label1.image=image1
label2.image=image2

label1.place(x=50,y=100)
label2.place(x=700,y=100)

def roll_dice():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image=image1
    image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image=image2
    
button=tk.Button(window,text="Roll The Dice!",bg="purple",fg="white",width="20",height="1",font="Calibri 20 bold",command=roll_dice)
button.place(x=490,y=0)
window.mainloop()
