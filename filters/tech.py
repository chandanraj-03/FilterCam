import cv2
import numpy as np
from .utils import *

def filter_cyberpunk(img):
    img = adjust_brightness_contrast(img, brightness=5, contrast=30)
    img = adjust_saturation(img, 1.6)
    img = color_shift(img, b=15, g=0, r=20)
    img = neon_edges(img)
    return img

def filter_thermal(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thermal = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
    return thermal

def filter_infrared(img):
    b, g, r = cv2.split(img)
    r_new = 255 - b
    b_new = 255 - r
    img = cv2.merge([b_new, g, r_new])
    img = adjust_brightness_contrast(img, brightness=10, contrast=15)
    return img

def filter_night_vision(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    out = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    out = color_shift(out, g=80)
    out = add_grain(out, 20)
    return out
