### unblur
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# image = cv.imread(r'C:\Users\kumar\Desktop\hackdata\transimg.jpg')
def sharpen(image):
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv.filter2D(image, -1, sharpen_kernel)
    sharpen = cv.filter2D(image, -1, sharpen_kernel)
    sharpen=cv.COLOR_BGR2RGB()
    cv.imwrite('sharpen.jpg',sharpen)
    cv.imshow('sharpen',sharpen)
    cv.waitKey()
    return sharpen