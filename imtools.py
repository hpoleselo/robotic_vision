from PIL import Image
from pylab import *

# Needs another function about path and so on...

def imresize(im,sz):
    """ Resizes an image array using PIL. Takes the size as argument """
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))