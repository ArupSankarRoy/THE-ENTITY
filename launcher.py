import os
from tkinter import *
from PIL import Image, ImageTk

def launch():
    try:
        os.system("python app.py")
    except Exception as e:
        print(f"An exception occurred: {e}")
        root.destroy()  # Close Tkinter window on exception

root = Tk()

root.title('App launcher')
root.geometry("380x280")
root.config(bg='lightskyblue')

load = Image.open("assets/logo.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.pack()

launcher_button = Button(root, text='Launch',
                         height=1, width=5,
                         command=launch,
                         bg='deepskyblue', bd=4)

launcher_button.pack()
root.mainloop()
