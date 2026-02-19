import cv2
import numpy as np
from .utils import *

def filter_soft_skin(img):
    blur = cv2.bilateralFilter(img, 12, 80, 80)
    out = cv2.addWeighted(img, 0.3, blur, 0.7, 0)
    out = adjust_brightness_contrast(out, brightness=10, contrast=5)
    return out


