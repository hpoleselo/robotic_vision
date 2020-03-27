from PIL import Image
from pylab import *

# Needs another function about path and so on...

def imresize(im,sz):
    """ Resizes an image array using PIL. Takes the size as argument """
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

def histeq(im,number_bins=256):
    """ Histogram equalization of a grayscale image. Gets  """

    imhist, bins = histogram(im.flatten(),number_bins,normed=True)
    # Cumulative distribution function
    cdf = imhist.cumsum()
    # Normalize
    cdf = 255*cdf/cdf[-1]

    # Use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(), bins[:-1], cdf)

    return (im2.reshape(im.shape),cdf)