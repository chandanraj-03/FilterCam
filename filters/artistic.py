import cv2
import numpy as np
from .utils import *

def filter_sketch(img):
    return edge_sketch(img)

def filter_cartoon(img):
    return cartoonify(img)

def filter_pop_art(img):
    img = adjust_brightness_contrast(img, brightness=5, contrast=30)
    img = adjust_saturation(img, 2.0)
    img = (img // 40) * 40
    return img

def filter_emboss(img):
    kernel = np.array([[-2, -1, 0],
                       [-1,  1, 1],
                       [ 0,  1, 2]])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    embossed = cv2.filter2D(gray, -1, kernel)
    embossed = cv2.cvtColor(embossed, cv2.COLOR_GRAY2BGR)
    embossed = adjust_brightness_contrast(embossed, brightness=128, contrast=0)
    return embossed


