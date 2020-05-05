import numpy as np
import cv2 as cv
import sys

# TODO Adicionar erro de tratamento

img = cv.imread('photo1.jpg')
if img is None:
    print("Image could not be loaded.")
    sys.exit()

def averaging_filter(img):
    # We could as well show the images on matplotlib
    useMatPlotLib = False

    # Extract dimensions of the photo
    h, w = img.shape[0:2]
    print(h,w)

    # kernel to apply convolution to the wished image
    kernel = np.ones((5,5),np.float32)/25

    # ddepth: desired depth of the output image. If it is negative, it will be the same as that of the input image.
    dst = cv.filter2D(img,-1,kernel)
    print(dst.shape)

    # Using the built in function from opencv to apply averaring filter
    # Note: using the 1/25 scalar on line 21 produces the same result as this method here!
    blur = cv.blur(img,(5,5))

    # if the image is too big we're gonna resize it, otherwise it will display two huges screens
    if h > 1280 or w > 1280:
        img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_LINEAR)
        dst = cv.resize(dst, None, fx=0.3, fy=0.3, interpolation=cv.INTER_LINEAR)
        print("Images have been resized:")
        print(img.shape)
        print(dst.shape)

    if useMatPlotLib:
        from matplotlib import pyplot as plt
        plt.subplot(121),plt.imshow(img),plt.title('Original')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
        plt.xticks([]), plt.yticks([])
        plt.show()
    
    if not useMatPlotLib:
        cv.imshow('original', img)
        cv.imshow('blurred with a manual 5x5 kernel', dst)
        cv.imshow('blurred with built in function', blur)
        cv.waitKey(0)
        cv.destroyAllWindows()


#def
   # p criar um kernel
    # If only sigmaX is specified, sigmaY is taken as the same as sigmaX. If both are given as zeros, they are calculated from the kernel size
    #cv.getGaussianKernel()
    #blur = cv.GaussianBlur(img,(5,5),0)
    #cv.boxFilter(normalize=False)


averaging_filter(img)

