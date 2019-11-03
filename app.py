'Main Module'
#!/usr/bin/python
import os
#from \\D:\\Academics\\ICT-Sem3\\SignalsAndSystems\\Project\\jp2-python-master\\jp2-python-master\\src\\utils import *
#import src.compression as
import tests.modules.compression as comp
import utils as util
from PIL import Image
import numpy as np

FOLDER = 'data'
RIGHT_FILENAME = 'lena.png'

def run():
    img = util.load_img(os.path.join(FOLDER, RIGHT_FILENAME))

    coef = comp.extract_rgb_coeff(img)
    print ("moving forward")
    image = comp.img_from_dwt_coeff(coef)
    image.save("data.jpg")#change your path here
    image.show()
    print("Image formed")
    #image.save("data/data1.jpg")#change your path here as well

    im = Image.open('data.jpg')
    width, height = im.size


    # (It will not change orginal image)
    im1 = im.crop((0, 0, height/2, width/2))

    # Shows the image in image viewer
    im1.show()

if __name__ == '__main__':
    run()
