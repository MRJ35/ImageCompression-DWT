'Main Module'
import os
import tests.modules.compression as comp
import utils as util
from PIL import ImageEnhance
from PIL import Image

FOLDER = 'data'
RIGHT_FILENAME = 'lena.png'

def run():
    img = util.load_img(os.path.join(FOLDER, RIGHT_FILENAME))

    coef = comp.extract_rgb_coeff(img)
    print ("moving forward")
    image = comp.img_from_dwt_coeff(coef)

    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(2)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.1)

    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(1.1)

    image.show()
    image.save("data/final.jpg")

    size = 256, 256
    im = Image.open("data/final.jpg")
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save("data/resized_image.png", "PNG")


if __name__ == '__main__':
    run()
