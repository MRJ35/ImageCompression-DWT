'Main Module'
#!/usr/bin/python
import os
#from \\D:\\Academics\\ICT-Sem3\\SignalsAndSystems\\Project\\jp2-python-master\\jp2-python-master\\src\\utils import *
#import src.compression as
import tests.modules.compression as comp
import utils as util
import numpy as np

FOLDER = 'data'
RIGHT_FILENAME = 'images.jpg'

def run():
    img = util.load_img(os.path.join(FOLDER, RIGHT_FILENAME))

    coef = comp.extract_rgb_coeff(img)
    #print (coef)
    image = comp.img_from_dwt_coeff(coef)
    image.save("D:\Academics\ICT-Sem3\SignalsAndSystems\Project\helloAll.jpg")
    image.show()
    print("Image formed")
    


if __name__ == '__main__':
    run()
