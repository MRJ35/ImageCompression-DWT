from tkinter import *
from PIL import Image


def hspace(col):
    space = Label(root,text = "    ",bg='black')
    space.grid(row=2,column=col)

def vspace(row):
    space = Label(root,text = "  ",bg = 'black')
    space.grid(row=row)

def rightClick(event,x):
    im = Image.open(x)
    im.show()

root = Tk()
root.title("Image Compression")
root.geometry('472x200')
root.configure(background='black')
root.resizable(False,False)
vspace(0)

image_name = Label(root,text="Image Name",borderwidth=2, relief="groove",bg = 'black',fg='white')
image_name.grid(row=2,column = 0)

vspace(3)

image = Label(root,text="abc",bg = 'black',fg='white')
image.grid(row=4,column = 0)

image1 = Label(root,text = "2160 KB",bg = 'black',fg='white')
image1.grid(row=4,column = 2)
image1.bind("<Button-1>",lambda event:rightClick(event,"abc.png"))

image1 = Label(root,text = "265 KB",bg = 'black',fg='white')
image1.grid(row=4,column = 4)
image1.bind("<Button-1>",lambda event:rightClick(event,"abc.png"))

image1 = Label(root,text = "12.2 %",bg = 'black',fg='white')
image1.grid(row=4,column = 6)



hspace(1)

oi = Label(root,text="Original Image Size",borderwidth=2, relief="groove",bg = 'black',fg='white')
oi.grid(row=2,column=2)

hspace(3)

ci = Label(root,text="Compressed Image Size",borderwidth=2, relief="groove",bg = 'black',fg='white')
ci.grid(row=2,column=4)

hspace(5)

cr = Label(root,text="Compression Ratio",borderwidth=2, relief="groove",bg = 'black',fg='white')
cr.grid(row=2,column=6)


mainloop()

