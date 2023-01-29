import cv2 as cv
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow 
from skimage import img_as_ubyte
from skimage.color import rgb2gray
from skimage.exposure import histogram, cumulative_distribution
from scipy.stats import cauchy, logistic
def corrector(oimg):
    # img = imread(r"C:\Users\kumar\Desktop\20230128_163424.jpg")
    img = oimg
    plt.imshow(img)
    plt.title('Manila Cathedral')
    cathedral_gray = rgb2gray(img)
    freq_h, bins_h = histogram(cathedral_gray)
    freq_c, bins_c = cumulative_distribution(cathedral_gray)
    
    image_intensity = img_as_ubyte(cathedral_gray)
    freq, bins = cumulative_distribution(image_intensity)
    target_bins = np.arange(255)
    target_freq = np.linspace(0, 1, len(target_bins))
    new_vals = np.interp(freq, target_freq, target_bins)
    
    def show_linear_cdf(image, channel, name, ax):
        image_intensity = img_as_ubyte(image[:,:,channel])
        freq, bins = cumulative_distribution(image_intensity)
        target_bins = np.arange(255)
        target_freq = np.linspace(0, 1, len(target_bins))
        ax.step(bins, freq, c='b', label='Actual CDF')
        ax.plot(target_bins, target_freq, c='r', label='Target CDF')
        ax.legend()
        ax.set_title('{} Channel: Actual vs. '
                    'Target Cumulative Distribution'.format(name))
    def linear_distribution(image, channel):
        image_intensity = img_as_ubyte(image[:,:,channel])
        freq, bins = cumulative_distribution(image_intensity)
        target_bins = np.arange(255)
        target_freq = np.linspace(0, 1, len(target_bins))
        new_vals = np.interp(freq, target_freq, target_bins)
        return new_vals[image_intensity].astype(np.uint8)
    
    red_channel = linear_distribution(img, 0)
    green_channel = linear_distribution(img, 1)
    blue_channel = linear_distribution(img, 2)
    
    return np.dstack([red_channel, green_channel, blue_channel])
