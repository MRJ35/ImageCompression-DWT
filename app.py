import os
import get_coeff as comp
import utils as util
import numpy as np
from PIL import Image, ImageEnhance
import pywt
import tkinter as tk
import tkinter.filedialog as tf
from resizeimage import resizeimage
import math
from output import run as go


def running(file, file_comp, file_ext):
    img = util.load_img(file)                       # Loads the image selected
    coef = comp.extract_rgb_coeff(img)              # Extracts the RBG Coefficients from the image 
    image = comp.img_from_dwt_coeff(coef)           # Forms the new image using the dwt coeeficients
    comp_file = "compress"+file_ext
    image.save(comp_file)                           # Saves the image

    '''
    Below lines of the code are to resize and enhance the images
    '''
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(2)
   
    file_enh = "enhanced"+file_ext
    image.save(file_enh)
    im = Image.open(file_enh)
    size = get_image_dimensions(file)
    im_resized = im.resize(size, Image.
                           ANTIALIAS)
    im_resized.save(file_comp)
    
    os.remove(comp_file)
    os.remove(file_enh)
    return os.path.getsize(file)/os.path.getsize(file_comp)


def get_image_dimensions(imagefile):             # Function to get the dimensions of the image
    with Image.open(imagefile) as img:
        width, height = img.size
    return int(width), int(height)              # returns the width and height of the image in terms of pixels


def create_folder():
    path = "Compressed_Images"                  # Creates the folder and in order to save the image in this folder
    os.rmdir(path)
    os.mkdir(path)


def run():  
    '''
    Main Function to run the compression
    '''
    tk.Tk().withdraw()                          # Window for choosing the images
    file = tf.askopenfilenames(title="Choose Images", filetypes=(
        ("jpeg files", "*.jpg"), ("png files", "*.png")))               # Select two type of iamges : jpg and png
    files = list(file)
    # create_folder()
    ans = 0
    mini = math.inf
    maxi = -math.inf
    for i in range(len(file)):
        x = list(file[i])
        ind = 0
        for j in range(len(x)):
            if x[j] == '/':
                ind = j
        ext = str(file[i][len(x)-4:len(x)])
        file2 = "Compressed_Images/"+file[i][ind+1:len(x)-4]+"_compressed"+ext    # create the path inorder to save the  compressed image in the created folder
        ans1 = running(file[i], file2, ext)                                       # The function to compress the image which returns the compression ratio
    
        '''
        Finds the maximum compression and minimum compression ratio when multiple images are selected
        '''
        mini = min(mini, ans1)
        maxi = max(maxi, ans1)                                                        
        ans += ans1
    
    print("\nCompression Ratio : %.2f" % (ans/len(file)))
    print("\nMax : "+str(maxi) + "\nMin : " + str(mini))
    go(files)


if __name__ == "__main__":
    run()
