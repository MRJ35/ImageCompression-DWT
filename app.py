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
from image import show_output


def running(file, file_comp, file_ext):
    img = util.load_img(file)
    coef = comp.extract_rgb_coeff(img)
    image = comp.img_from_dwt_coeff(coef)
    comp_file = "compress"+file_ext
    image.save(comp_file)
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(2)
    # enhancer = ImageEnhance.Color(image)
    # image = enhancer.enhance(1.1)
    file_enh = "enhanced"+file_ext
    image.save(file_enh)
    im = Image.open(file_enh)
    size = get_image_dimensions(file)
    im_resized = im.resize(size, Image.
                           ANTIALIAS)
    im_resized.save(file_comp)
    #print(str(os.path.getsize(file))+" " + str(os.path.getsize(file_comp)))
    os.remove(comp_file)
    os.remove(file_enh)
    return os.path.getsize(file)/os.path.getsize(file_comp)


def get_image_dimensions(imagefile):
    with Image.open(imagefile) as img:
        width, height = img.size
    return int(width), int(height)


def create_folder():
    path = "Compressed_Images"
    os.rmdir(path)
    os.mkdir(path)


def run():
    root = tk.Tk()
    file = tf.askopenfilenames(parent=root, title="Choose", filetypes=(
        ("jpeg files", "*.jpg"), ("png files", "*.png")))
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
        file2 = "Compressed_Images/"+file[i][ind+1:len(x)-4]+"_compressed"+ext
        ans1 = running(file[i], file2, ext)
        show_output(file2,file[i])
        mini = min(mini, ans1)
        maxi = max(maxi, ans1)
        ans += ans1
    print("\nCompression Ratio : %.2f" % (ans/len(file)))
    print("\nMax : "+str(maxi) + "\nMin : " + str(mini))


if __name__ == "__main__":
    run()
