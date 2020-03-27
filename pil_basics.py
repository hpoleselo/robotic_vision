from PIL import Image, ImageDraw, ImageFont

from pylab import *

def basics():
    """ Opening, converting to greyscale, cropping, rotating, pasting and resizing. """
    image = "empire.jpg"
    pil_obj = Image.open(image).convert('L')
    print(pil_obj)

    # --- Cropping ---
    # Needs a 4-tuple to crop, (left,upper,right,lower)
    box = (100,100,400,400)
    region = pil_obj.crop(box)
    print(region)
    rotated_region = region.transpose(Image.ROTATE_270)

    # Now we paste the cropped/rotated part on the original pil_obj
    pil_obj.paste(rotated_region, box)
    print(pil_obj)
    #pil_obj.show()

    # --- Resizing ---
    # We have to pass to tuple the new size that we wish
    resized = pil_obj.resize((128,128))

    # We can rotate that way as well, but we're rotating the whole object
    resized = resized.rotate(45)
    resized.show()

# --- Histograms and Image Contours ---
# Has to be in greyscale, because the contours has to take one single value for every coordinate x,y

def contours_histogram():
    img_array = array(Image.open('empire.jpg').convert('L'))
    print("Image array in grayscale:") 
    print("Check that the upper right values, they are almost 256 since they are representing the clouds (white)")
    print(img_array)
    print("Length: "), img_array.shape
    print("")
    flattened = img_array.flatten()
    print("Image array flattened:")
    print(flattened)
    print("Length:"), len(flattened)

    
    # These functions are from pylab, which is basically matplotlib
    figure()
    gray()
    contour(img_array, origin='image')
    axis('equal')
    axis('off')
    figure()
    # Takes the matrix and flattens into a 1d array of length 455200
    print("Check the histogram that it has the distribution of the bins (intensities) of the pixels!")
    print("The most predominant bins(intensities) are around 108")
    hist(img_array.flatten(),128)
    show()  


# -- Interactive annotion --
def interactive_annotation():
    img_array = array(Image.open('empire.jpg'))
    # Note: imshow is for matplotlib!
    imshow(img_array)
    print("Click 3 points on the picture!")
    points = ginput(3)
    print("You clicked: "), points
    show()


# -- Numpy basics -- 
def numpy_test():
    im = array(Image.open('empire.jpg'))
    print (im.shape, im.dtype)
    print("See that here we have number 3 because there are 3 channels (RGB) \n")

    # Forcing the array to be in format as float instead of uint8
    im = array(Image.open('empire.jpg').convert('L'),'f')
    print (im.shape, im.dtype)

    # im[i,:] = im[j,:]
    # im[:100,:50].sum() sum of the first 100 values from the row and 50 first values of the column
    # im[i].mean()  average of row i
    # im[:,-1]  last column, goes backwards
    # im[-2,:] or im[-2]  second to last row

# -- Grayscale transforms -
def grayscale_transformations():
    im = array(Image.open('empire.jpg').convert('L'))

    # Inverts the image grayscale colors
    im2 = 255 - im
    # Clamps the pixel intensities from 100, like a threshold
    im3 = (100.0/255)*im + 100
    # Squared, makes the darker pixels way darker
    im4 = (255.0)*(im/255.0)**2

    print("To see how each transformation affects the intervals, we use im.min and im.max:")
    print("First, identity transform: f(x) = x \n"), int(im.min()), int(im.max())
    print("Second, inverting the colors: f(x) = 255 - x \n"), int(im2.min()), int(im2.max())
    print("Third, clamping like a threshold: f(x) = 100/255*x + 100 \n"), int(im3.min()), int(im3.max())
    print("Fourth, parabolic, makes darker: f(x) = 255*(x/255)^2 \n"), int(im4.min()), int(im4.max())

    # Now, to see the applied transforms in practice we have to convert it back as a pil_object
    pil_im = Image.fromarray(uint8(im))
    pil_im2 = Image.fromarray(uint8(im2))
    pil_im3 = Image.fromarray(uint8(im3))
    pil_im4 = Image.fromarray(uint8(im4))

    # Add font to the plots so we can compare easier what is what
    font = ImageFont.truetype("Fonts/cardenio_modern_std.ttf", 26)
    draw1 = ImageDraw.Draw(pil_im)
    draw2 = ImageDraw.Draw(pil_im2)
    draw3 = ImageDraw.Draw(pil_im3)
    draw4 = ImageDraw.Draw(pil_im4)
    
    draw1.text((50,50),"Identity Transf.",(255,255,255),font=font)
    draw2.text((50,50),"Invert Colors",(255,255,255),font=font)
    draw3.text((50,50),"Clamping (threshold from 100 to 255)",(255,255,255),font=font)
    draw4.text((50,50),"Quadratic (makes pixels darker)",(255,255,255),font=font)

    pil_im.show()
    pil_im2.show()
    pil_im3.show()
    pil_im4.show()
    


#basics()
#contours_histogram()
#interactive_annotation()
#numpy_test()
grayscale_transformations()
