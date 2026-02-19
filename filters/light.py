import cv2
import numpy as np
from .utils import *

def filter_bloom(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    bright_mask = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    bright_only = cv2.bitwise_and(img, bright_mask)
    
    blur = cv2.GaussianBlur(bright_only, (21, 21), 0)
    
    return cv2.addWeighted(img, 1.0, blur, 0.8, 0)

def filter_light_leak(img):
    h, w = img.shape[:2]
    
    leak = np.zeros((h, w, 3), dtype=np.uint8)
    
    for x in range(w // 3):
        alpha = 1.0 - (x / (w/3))
        color = (50, 50, 255)
        leak[:, x] = [int(c * alpha) for c in color]
        
    return cv2.add(img, leak)
