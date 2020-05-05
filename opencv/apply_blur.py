import numpy as np
import cv2 as cv
import sys

img = cv.imread('photo1.jpg')
if img is None:
    print("Image could not be loaded.")
    sys.exit()

def blurring_filter(img):
    # We could as well show the images on matplotlib
    useMatPlotLib = False

    # Extract dimensions of the photo
    h, w = img.shape[0:2]
    print(h,w)

    # ----- Mean/Box Filter -----

    # Mean-filter, a.k.a box-filter, just average the pixel values of all neighboring pixels. This is equivalent to giving an equal weight to all pixels around the center regardless of the distance from the center pixel.

    # kernel to apply convolution to the wished image
    kernel = np.ones((5,5),np.float32)/25

    # ddepth: desired depth of the output image. If it is negative, it will be the same as that of the input image.
    dst = cv.filter2D(img,-1,kernel)
    print(dst.shape)

    # Using the built in function from opencv to apply averaring filter
    # Note: using the 1/25 scalar on line 21 produces the same result as this method here!ls
    blur = cv.blur(img,(5,5))



    # ----- Gaussian Filter ------

    # Gaussian filters weigh pixels a bell-curve around the center pixel. This means that farther pixels get lower weights.
    # If only sigmaX is specified, sigmaY is taken as the same as sigmaX. If both are given as zeros, they are calculated from the kernel size
    gaus = cv.gaussianBlur(img,(5,5),0)



    # ----- Median Blur -------
    # Takes the median of all the pixels under the kernel area and the central element is replaced with this median value. This is highly effective against salt-and-pepper noise in an image
    # add image with noise and then use this filter to see the perfomance
    median = cv.medianBlur(img,5)




    # ----- Bilateral Filter -------
    bilateral = cv.bilateralFilter(img,9,75,75)


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
        cv.imshow('using gaussian filter', gaus)
        cv.imshow('using gaussian filter', median)
        cv.imshow('using gaussian filter', bilateral)
        
        cv.waitKey(0)
        cv.destroyAllWindows()


blurring_effect(img)

