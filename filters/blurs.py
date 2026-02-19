import cv2
import numpy as np
from .utils import *

def filter_motion_blur(img):
    kernel_size = 30
    kernel = np.zeros((kernel_size, kernel_size))
    kernel[int((kernel_size-1)/2), :] = np.ones(kernel_size)
    kernel /= kernel_size
    return cv2.filter2D(img, -1, kernel)

def filter_radial_blur(img):
    h, w = img.shape[:2]
    center_x, center_y = w // 2, h // 2
    blur_strength = 20
    num_steps = 10
    
    output = img.astype(np.float32)
    for i in range(1, num_steps):
        scale = 1.0 + (i * 0.02) 
        M = cv2.getRotationMatrix2D((center_x, center_y), 0, scale)
        rotated = cv2.warpAffine(img, M, (w, h))
        output += rotated.astype(np.float32)
        
    output /= num_steps
    return clamp(output)

def filter_tilt_shift(img):
    h, w = img.shape[:2]
    
    blur = cv2.GaussianBlur(img, (15, 15), 0)
    
    mask = np.zeros((h, w), dtype=np.float32)
    center_y = h // 2
    focus_height = h // 4
    
    for y in range(h):
        dist = abs(y - center_y)
        if dist < focus_height:
            mask[y, :] = 0.0    
        else:
            val = (dist - focus_height) / (h/2 - focus_height)
            mask[y, :] = min(1.0, val)            
    mask = mask[:, :, None] 
    
    out = img * (1 - mask) + blur * mask
    return out.astype(np.uint8)

def filter_soft_focus(img):
    blur = cv2.GaussianBlur(img, (0, 0), 8)
    img = cv2.addWeighted(img, 0.6, blur, 0.4, 0)
    img = adjust_brightness_contrast(img, brightness=10, contrast=-10)
    img = glow_effect(img, strength=0.3, blur_sigma=10)
    return img
