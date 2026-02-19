import cv2
import numpy as np
from .utils import *

def filter_sepia(img):
    img = sepia(img, strength=0.9)
    img = fade(img, 0.07)
    return img

def filter_polaroid(img):
    img = adjust_brightness_contrast(img, brightness=10, contrast=15)
    img = adjust_saturation(img, 1.2)
    img = add_warmth(img, 12)
    img = add_grain(img, 15)
    img = fade(img, 0.1)
    h, w = img.shape[:2]
    border = np.full_like(img, 255)
    mask = np.zeros((h, w), dtype=np.uint8)
    mask[10:-10, 10:-10] = 255
    img = np.where(mask[:, :, None] > 0, img, border)
    return img



def filter_lomo(img):
    img = adjust_saturation(img, 1.45)
    img = adjust_brightness_contrast(img, brightness=0, contrast=30)
    img = vignette(img, 0.30)
    return img

def filter_vintage(img):
    img = adjust_brightness_contrast(img, brightness=5, contrast=-10)
    img = add_warmth(img, 20)
    img = adjust_saturation(img, 0.8)
    img = vignette(img, 0.4)
    img = add_grain(img, 10)
    img = fade(img, 0.15)
    return img

def filter_retro(img):
    img = adjust_brightness_contrast(img, brightness=5, contrast=18)
    img = adjust_saturation(img, 1.45)
    img = color_shift(img, b=10, g=-5, r=20)
    img = add_grain(img, 12)
    img = vignette(img, 0.35)
    return img

def filter_glitch(img):
    h, w = img.shape[:2]
    
    b, g, r = cv2.split(img)
    shift = 5
    b_shifted = np.roll(b, shift, axis=1)
    r_shifted = np.roll(r, -shift, axis=1)
    img = cv2.merge([b_shifted, g, r_shifted])
    
    rows = np.random.randint(0, h-10, 3)
    for r in rows:
        h_slice = np.random.randint(5, 30)
        offset = np.random.randint(-20, 20)
        if r+h_slice < h:
            img[r:r+h_slice, :] = np.roll(img[r:r+h_slice, :], offset, axis=1)
            
    return img



def filter_digital_corrupt(img):
    h, w = img.shape[:2]
    out = img.copy()
    
    num_blocks = np.random.randint(5, 15)
    for _ in range(num_blocks):
        bh = np.random.randint(10, 50)
        bw = np.random.randint(30, 100)
        y = np.random.randint(0, max(1, h - bh))
        x = np.random.randint(0, max(1, w - bw))
        
        effect = np.random.randint(0, 3)
        if effect == 0:
            shift = np.random.randint(-50, 50)
            out[y:y+bh, x:x+bw] = np.roll(out[y:y+bh, x:x+bw], shift, axis=1)
        elif effect == 1:
            out[y:y+bh, x:x+bw] = 255 - out[y:y+bh, x:x+bw]
        else:
            src_y = np.random.randint(0, max(1, h - bh))
            out[y:y+bh, x:x+bw] = out[src_y:src_y+bh, x:x+bw]
    
    return out

def filter_pixelate(img, blocks=64):
    h, w = img.shape[:2]
    small = cv2.resize(img, (blocks, int(blocks * h / w)), interpolation=cv2.INTER_LINEAR)
    out = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
    return out

def filter_tv_static(img):
    h, w = img.shape[:2]
    noise = np.random.randint(0, 255, (h, w, 3)).astype(np.uint8)
    
    img = cv2.addWeighted(img, 0.85, noise, 0.15, 0)
    
    scanline_mask = np.zeros((h, w, 3), dtype=np.uint8)
    scanline_mask[::2, :] = 50
    img = cv2.subtract(img, scanline_mask)
    
    img = adjust_brightness_contrast(img, brightness=10, contrast=25)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

def filter_rgb_split(img):
    b, g, r = cv2.split(img)
    shift = 12
    
    b_shifted = np.roll(b, shift, axis=1)
    r_shifted = np.roll(r, -shift, axis=1)
    g_shifted = np.roll(g, 3, axis=0)
    
    img = cv2.merge([b_shifted, g_shifted, r_shifted])
    img = adjust_brightness_contrast(img, brightness=5, contrast=15)
    return img

def filter_film_dust_scratches(img):
    out = img.copy()
    h, w = img.shape[:2]
    
    num_specks = 100
    for _ in range(num_specks):
        y = np.random.randint(0, h)
        x = np.random.randint(0, w)
        cv2.circle(out, (x, y), 1, (200, 200, 200), -1)
        
    num_scratches = 5
    for _ in range(num_scratches):
        x = np.random.randint(0, w)
        cv2.line(out, (x, 0), (x, h), (180, 180, 180), 1)
        
    return out


def filter_negative(img):
    return cv2.bitwise_not(img)

def filter_posterize(img):
    n = 64
    return (img // n) * n
