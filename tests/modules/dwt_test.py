'Test Definition for Compression methods'
import unittest
import os
#from utils import *
import utils as util
import tests.modules.compression as comp
FOLDER = 'data'
FILENAME = 'lena.png'

class CompressionTest(unittest.TestCase):
    'Units test for compression methods'
    def test_rgb_to_yuv(self):
        'it should return an Image Type after conversion'
        img = util.load_img(os.path.join(FOLDER, FILENAME))
        img_yuv = comp.rgb_to_yuv(img)
        self.assertEqual(type(img_yuv).__name__, 'Image')

    def test_yuv_to_rgb(self):
        'it should return an Image Type after conversion'
        img = util.load_img(os.path.join(FOLDER, FILENAME))
        img_yuv = comp.yuv_to_rgb(img)
        self.assertEqual(type(img_yuv).__name__, 'Image')

    def test_extract_rgb_coeff(self):
        'it should return a Tuple of coefficient per each channel (RGB)'
        img = util.load_img(os.path.join(FOLDER, FILENAME))
        (c_r, c_g, c_b) = comp.extract_rgb_coeff(img)
        self.assertTrue(c_r[0] is not None)
        self.assertTrue(c_r[1] is not None)
        self.assertTrue(c_g[0] is not None)
        self.assertTrue(c_g[1] is not None)
        self.assertTrue(c_b[0] is not None)
        self.assertTrue(c_b[1] is not None)
        image_formed = comp.img_from_dwt_coeff((c_r,c_g,c_b))
        print("Image should have been formed somewhere")
        image_formed.save('image_formed.png')
        image_formed.show()

    def test_img_from_dwt_coeff(self):
        'TODO'
        img = util.load_img(os.path.join(FOLDER, FILENAME))
        coeff = comp.extract_rgb_coeff(img)
        image_form = comp.img_from_dwt_coeff((c_r, c_g, c_b))
        print("Image formed somewhere")
        image_form.save('Image_formed.png')
        image_form.show()
        pass

    # Demo function
    def sum(self, a, b):
        return a + b

    def test_demo(self):
        self.assertEqual(self.sum(1,1), 2)
        self.assertEqual(self.sum(1,2), 3)
