from tkinter import *
from PIL import Image
import ntpath
import os
import math

def hspace(col,root):
    space = Label(root,text = "    ",bg = '#3ed8ea')
    space.grid(row=2,column=col)

def vspace(row,root):
    space = Label(root,text = "  ",bg = '#3ed8ea')
    space.grid(row=row)

def rightClick(event,x):
    im = Image.open(x)
    im.show()

def run(fileList):
    root = Tk()
    root.title("Image Compression")
    root.geometry('472x200')
    root.configure(background='#3ed8ea')
    root.resizable(False,False)
    vspace(0,root)
    #compressed_file_name =  "Compressed_Images/"+name[:len(name)-4]+"_compressed"+name[len(name)-4:]
    image_name = Label(root,text="Image Name",borderwidth=2, relief="groove",bg = '#3ed8ea',fg='#1c1c6c')
    image_name.grid(row=2,column = 0)
    vspace(3,root) 
    hspace(1,root)
    oi = Label(root,text="Original Image Size",borderwidth=2, relief="groove",bg = '#3ed8ea',fg='#1c1c6c')
    oi.grid(row=2,column=2)
    hspace(3,root)
    ci = Label(root,text="Compressed Image Size",borderwidth=2, relief="groove",bg = '#3ed8ea',fg='#1c1c6c')
    ci.grid(row=2,column=4)
    hspace(5,root)
    cr = Label(root,text="Compression Ratio",borderwidth=2, relief="groove",bg = '#3ed8ea',fg='#1c1c6c')
    cr.grid(row=2,column=6)

    rows = 4
    for i in range(len(fileList)):
        name = ntpath.basename(fileList[i])
        compressed_file_name =  "Compressed_Images/"+name[:len(name)-4]+"_compressed"+name[len(name)-4:]
        create_table(root,name,fileList[i],compressed_file_name,rows)
        rows = rows+1
    mainloop()

def extract_ratio(str1,str2):
    s1 = int(str1[:len(str1)-3])
    s2 = int(str2[:len(str2)-3])
    return "%.2f"%(s1/s2)
    
def create_table(root,name,file,file2,row):
    image = Label(root,text=name,bg = '#3ed8ea',fg='#1c1c6c')
    image.grid(row=row,column = 0)
    image1 = Label(root,text = meta_data(file),bg = '#3ed8ea',fg='#1c1c6c')
    image1.grid(row=row,column = 2)
    image1.bind("<Button-1>",lambda event:rightClick(event,file))
    image1 = Label(root,text = meta_data(file2),bg = '#3ed8ea',fg='#1c1c6c')
    image1.grid(row=row,column = 4)
    image1.bind("<Button-1>",lambda event:rightClick(event,file2))
    image1 = Label(root,text = extract_ratio(meta_data(file),meta_data(file2)),bg = '#3ed8ea',fg='#1c1c6c')
    image1.grid(row=row,column = 6)

def meta_data(filen):
    return str(math.ceil(int(os.path.getsize(filen))/1024)) + " Kb"