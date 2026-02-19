import cv2
import numpy as np
from .utils import *

def filter_vertical_flip(img):
    return cv2.flip(img, 0)

def filter_quad_mirror(img):
    h, w = img.shape[:2]
    top_left = img[:h//2, :w//2]
    
    top = np.hstack([top_left, cv2.flip(top_left, 1)])
    bottom = cv2.flip(top, 0)
    
    return np.vstack([top, bottom])

def filter_glass_window(img):
    h, w = img.shape[:2]
    shift_x = 30
    
    src1 = img[:, :-shift_x]
    src2 = img[:, shift_x:]
    
    h_new, w_new = src1.shape[:2]
    overlay = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)
    
    return cv2.resize(overlay, (w, h))
