# pylint: disable=C0103,E0401,W0631
'Compression methods'
import pywt
import numpy
from PIL import Image
import utils as util


def rgb_to_yuv(img):
    """
    Returns yuv image
    Parameters
    ----------
    img: PIL Image
    Returns
    -------
    PIL Image:
        image converted to yuv
    """
    yuv_img = img.convert('RGB')
    (width, height) = img.size
    for x in range(width):
        for y in range(height):
            (r, g, b) = yuv_img.getpixel((x, y))
        Y = 0.299 * r + 0.587 * g + 0.114 * b
        CB = - 0.168935 * r + - 0.331665 * g + 0.50059 * b + 128
        CR = 0.499813 * r - 0.4187 * g + - 0.081282 * b + 128
        Y = 255 if (Y >= 255) else Y
        Y = 0 if (Y <= 0) else Y
        CB = 255 if (CB >= 255) else CB
        CB = 0 if (CB <= 0) else CB
        CR = 255 if (CR >= 255) else CR
        CR = 0 if (CR <= 0) else CR
        yuv_img.putpixel((x, y), (int(Y), int(CB), int(CR)))
    return yuv_img

def yuv_to_rgb(img):
    """
    Returns rgb image
    Parameters
    ----------
    img: PIL Image
    Returns
    -------
    PIL Image:
        image converted to rgb
    """
    (width, height) = img.size
    rgb_img = img.copy()
    for x in range(width):
        for y in range(height):
            (Y, CB, CR) = img.getpixel((x, y))
        R = Y + 1.402 * (CR - 128)
        G = Y - 0.34414 * (CB - 128) - 0.71414 * (CR - 128)
        B = Y + 1.772 * (CB -128)
        R = 255 if (R >= 255) else R
        R = 0 if (R <= 0) else R
        G = 255 if (G >= 255) else G
        G = 0 if (G <= 0) else G
        B = 255 if (B >= 255) else B
        B = 0 if (B <= 0) else B
        rgb_img.putpixel((x, y), (int(R), int(G), int(B)))
    return  rgb_img

def rgb_to_grayscale(img):
    """
    Returns greyscale image
    Parameters
    ----------
    img: PIL Image
    Returns
    -------
    PIL Image:
        image converted to greyscale
    """
    width, height = img.size
    res = img.copy()
    for i in range(width):
        for j in range(height):
            (r, g, b) = img.getpixel((i, j))
            gs = int((r + g + b) / 3)
            res.putpixel((i, j), (gs, gs, gs))
    return res

def extract_rgb_coeff(img):
    """
    Returns RGB dwt applied coefficients tuple
    Parameters
    ----------
    img: PIL Image
    Returns
    -------
    (coeffs_r, coeffs_g, coeffs_b):
        RGB coefficients with Discrete Wavelet Transform Applied
    """
    (width, height) = img.size
    img = img.copy()

    mat_r = numpy.empty((width, height))
    mat_g = numpy.empty((width, height))
    mat_b = numpy.empty((width, height))

    for i in range(width):
        for j in range(height):
            (r, g, b) = img.getpixel((i, j))
            mat_r[i, j] = r
            mat_g[i, j] = g
            mat_b[i, j] = b

    # coeffs_r: cA,(cH,cV,cD)
    print("Mat_r : ")
    print(mat_r)
    print("\nMat_g : ")
    print(mat_g)
    print("\nMat_b : ")
    print(mat_b)
    coeffs_r = pywt.dwt2(mat_r, 'haar')
    # coeffs_g: cA,(cH,cV,cD)
    coeffs_g = pywt.dwt2(mat_g, 'haar')
    # coeffs_b: cA,(cH,cV,cD)
    coeffs_b = pywt.dwt2(mat_b, 'haar')
    print("Coeff : \ncoeff_r ")
    print(coeffs_r,"\ncoeff_g ",coeffs_g,"\ncoeff_b ",coeffs_b)
    return (coeffs_r, coeffs_g, coeffs_b)

def img_from_dwt_coeff(coeff_dwt):
    """
    Returns Image recreated from dwt coefficients
    Parameters
    ----------
    (coeffs_r, coeffs_g, coeffs_b):
        RGB coefficients with Discrete Wavelet Transform Applied
    Returns
    -------
    Image from dwt coefficients
    """
    #Channel Red
    (coeffs_r, coeffs_g, coeffs_b) = coeff_dwt
    cARed = numpy.array(coeffs_r[0])
    cc = numpy.array((coeffs_r, coeffs_g, coeffs_b))

    (width, height) = (len(coeffs_r[0]),len(coeffs_r[0][0]))
    print("width : ",width," height : ",height)
    print("test : ",numpy.ndim(cc)," tt : ",len(coeffs_r[0][0]))
    cHRed = numpy.array(coeffs_r[1][0])
    cVRed = numpy.array(coeffs_r[1][1])
    cDRed = numpy.array(coeffs_r[1][2])
    #Channel Green
    cAGreen = numpy.array(coeffs_g[0])
    cHGreen = numpy.array(coeffs_g[1][0])
    cVGreen = numpy.array(coeffs_g[1][1])
    cDGreen = numpy.array(coeffs_g[1][2])
    #Channel Blue
    cABlue = numpy.array(coeffs_b[0])
    cHBlue = numpy.array(coeffs_b[1][0])
    cVBlue = numpy.array(coeffs_b[1][1])
    cDBlue = numpy.array(coeffs_b[1][2])

    # maxValue per channel par matrix
    cAMaxRed = util.max_ndarray(cARed)
    cAMaxGreen = util.max_ndarray(cAGreen)
    cAMaxBlue = util.max_ndarray(cABlue)

    cHMaxRed = util.max_ndarray(cHRed)
    cHMaxGreen = util.max_ndarray(cHGreen)
    cHMaxBlue = util.max_ndarray(cHBlue)

    cVMaxRed = util.max_ndarray(cVRed)
    cVMaxGreen = util.max_ndarray(cVGreen)
    cVMaxBlue = util.max_ndarray(cVBlue)

    cDMaxRed = util.max_ndarray(cDRed)
    cDMaxGreen = util.max_ndarray(cDGreen)
    cDMaxBlue = util.max_ndarray(cDBlue)

    # Image object init
    dwt_img = Image.new('RGB', (width*2, height*2), (0, 0, 20))
    #cA reconstruction
    for i in range(width):
        for j in range(height):
            R = cARed[i][j]
            R = (R/cAMaxRed)*160.0
            G = cAGreen[i][j]
            G = (G/cAMaxGreen)*85.0
            B = cABlue[i][j]
            B = (B/cAMaxBlue)*100.0
            new_value = (int(R), int(G), int(B))
            dwt_img.putpixel((i, j), new_value)
    #cH reconstruction
    for i in range(width):
        for j in range(height):
            R = cHRed[i][j]
            R = (R/cHMaxRed)*160.0
            G = cHGreen[i][j]
            G = (G/cHMaxGreen)*85.0
            B = cHBlue[i][j]
            B = (B/cHMaxBlue)*100.0
            new_value = (int(R), int(G), int(B))
            dwt_img.putpixel((i+width, j), new_value)
    #cV reconstruction
    for i in range(width):
        for j in range(height):
            R = cVRed[i][j]
            R = (R/cVMaxRed)*160.0
            G = cVGreen[i][j]
            G = (G/cVMaxGreen)*85.0
            B = cVBlue[i][j]
            B = (B/cVMaxBlue)*100.0
            new_value = (int(R), int(G), int(B))
            dwt_img.putpixel((i, j+height), new_value)
    #cD reconstruction
    for i in range(width):
        for j in range(height):
            R = cDRed[i][j]
            R = (R/cDMaxRed)*160.0
            G = cDGreen[i][j]
            G = (G/cDMaxGreen)*85.0
            B = cDBlue[i][j]
            B = (B/cDMaxBlue)*100.0
            new_value = (int(R), int(G), int(B))
            dwt_img.putpixel((i+width, j+height), new_value)
    return dwt_img

def quantization(mat):
    pass
