from PIL import Image

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
    hist(img_array.flatten(),128)
    show()  

contours_histogram()


