from skimage.transform import resize

def resize_image(image, new_shape):
    assert 0<= new_shape<=1, "Dimensão deve ser entre 0 e 1"
    height=round(image.shape[0]*new_shape)
    width=round(image.shape[1]*new_shape)
    return resize(image, (height, width), anti_aliasing=True)
