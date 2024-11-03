from tkinter import *
from PIL import ImageTk,Image

# Root
root = Tk()
root.title("My Code")
root.iconbitmap('')

def open():
    global theImage
    top = Toplevel()
    top.title("Second Window")
    top.iconbitmap('')
    theImage = ImageTk.PhotoImage(Image.open("images/Elden_Ring.jpg"))
    aLabel = Label(top, image=theImage).pack()
    button2 = Button(top, text="Close", command=top.destroy).pack()

Button1 = Button(root, text = "Open Second Window", command=open).pack()


# Execution
root.mainloop()
