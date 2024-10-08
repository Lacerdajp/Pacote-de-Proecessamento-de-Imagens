
import numpy as np
from skimage.color import rgb2gray as gray
from skimage.exposure import match_histograms as match_hist
from skimage.metrics import structural_similarity as ssim

def combine_images(image1, image2):
    assert image1.shape == image2.shape, "Imagens diferentes"
    gray_image1 = gray(image1)
    gray_image2 = gray(image2)
    (score,diff_image) = ssim(gray_image1, gray_image2, full=True)
    print(f"SSIM:{score}")
    normalization_diff= (diff_image - np.min(diff_image))/(np.max(diff_image)-np.min(diff_image))
    return normalization_diff
def transfer_histogram(image1, image2):
    return match_hist(image1, image2, multichannel=True)