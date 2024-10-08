from skimage.io import imread 
from skimage.io import imsave

def read_image(image_path, is_gray=False):
    return imread(image_path, as_gray=is_gray)
def save_image(image, image_path):
    imsave(image_path, image)