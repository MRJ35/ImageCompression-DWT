'Main Module'
#!/usr/bin/python
import os
#from \\D:\\Academics\\ICT-Sem3\\SignalsAndSystems\\Project\\jp2-python-master\\jp2-python-master\\src\\utils import *
#import src.compression as
import tests.modules.compression as comp
import utils as util
import numpy as np
from PIL import ImageEnhance

FOLDER = 'data'
RIGHT_FILENAME = 'images.jpg'

def run():
    img = util.load_img(os.path.join(FOLDER, RIGHT_FILENAME))

    coef = comp.extract_rgb_coeff(img)
    print ("moving forward")
    image = comp.img_from_dwt_coeff(coef)
    #image.save("data.jpg")#change your path here

    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(2)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.1)

    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(1.1)

    image.save("data/final.jpg")



    # image.show()
    # print("Image formed")
    # image.save("data/compressed_image.jpg")#change your path here as well




if __name__ == '__main__':
    run()
