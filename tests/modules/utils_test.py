'Test Definition for Utility methods'
import unittest
import os
import numpy as np
import utils as util
FOLDER = 'data'
RIGHT_FILENAME = 'lena.png'
WRONG_FILENAME = 'dummy_file.png'

class UtilTest(unittest.TestCase):
    'Units test for utility methods'
    def test_load_png_file(self):
        'it should return an Image Type if file exists and is an Image file'
        # case 1 (it should return PngImageFile):
        img = util.load_img(os.path.join(FOLDER, RIGHT_FILENAME))
        self.assertEqual(type(img).__name__, 'PngImageFile')
        # case 2 (it should return NoneType):
        img = util.load_img(os.path.join(FOLDER, WRONG_FILENAME))
        self.assertEqual(type(img).__name__, 'NoneType')

    def test_max_ndarray(self):
        'it should return an Integer, max if matrix is valid, 0 otherwise'
        # case 1 (it should return 6):
        tmp_array = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
        max_value = util.max_ndarray(tmp_array)
        self.assertEqual(type(max_value).__name__, 'int32')
        self.assertEqual(max_value, 6)
        # case 2 (it should return 0):
        max_none = util.max_ndarray(None)
        self.assertEqual(type(max_none).__name__, 'int')
        self.assertEqual(max_none, 0)
