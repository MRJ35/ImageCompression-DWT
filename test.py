from tkinter import *
from PIL import Image
import ntpath
import image as im

def hspace(col,root):
    space = Label(root,text = "    ",bg='black')
    space.grid(row=2,column=col)

def vspace(row,root):
    space = Label(root,text = "  ",bg = 'black')
    space.grid(row=row)

def rightClick(event,x):
    im = Image.open(x)
    im.show()

def run(fileList):
    root = Tk()
    root.title("Image Compression")
    root.geometry('472x200')
    root.configure(background='black')
    root.resizable(False,False)
    vspace(0,root)
    compressed_file_name =  "Compressed_Images/"+name[:len(name)-4]+"_compressed"+name[len(name)-4:]
    image_name = Label(root,text="Image Name",borderwidth=2, relief="groove",bg = 'black',fg='white')
    image_name.grid(row=2,column = 0)
    vspace(3,root) 
    hspace(1,root)
    oi = Label(root,text="Original Image Size",borderwidth=2, relief="groove",bg = 'black',fg='white')
    oi.grid(row=2,column=2)
    hspace(3,root)
    ci = Label(root,text="Compressed Image Size",borderwidth=2, relief="groove",bg = 'black',fg='white')
    ci.grid(row=2,column=4)
    hspace(5,root)
    cr = Label(root,text="Compression Ratio",borderwidth=2, relief="groove",bg = 'black',fg='white')
    cr.grid(row=2,column=6)

    rows = 4
    for i in range(len(fileList)):
        name = ntpath.basename(fileList[i])
        
    mainloop()

def extract_ratio(str1,str2):
    s1 = int(str1[:len(str1)-3])
    s2 = int(str2[:len(str2)-3])
    return str(s1/s2) + " %"
    
def create_table(root,file,file2,row):
    image = Label(root,text=file,bg = 'black',fg='white')
    image.grid(row=row,column = 0)
    image1 = Label(root,text = im.meta_data(file),bg = 'black',fg='white')
    image1.grid(row=row,column = 2)
    image1.bind("<Button-1>",lambda event:rightClick(event,file))
    image1 = Label(root,text = im.meta_data(file2),bg = 'black',fg='white')
    image1.grid(row=row,column = 4)
    image1.bind("<Button-1>",lambda event:rightClick(event,file2))
    image1 = Label(root,text = extract_ratio(im.meta_data(file),im.meta_data(file2)),bg = 'black',fg='white')
    image1.grid(row=row,column = 6)