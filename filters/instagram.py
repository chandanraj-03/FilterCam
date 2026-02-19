import cv2
from .utils import *

def filter_original(img):
    return img

def filter_reyes(img):
    img = adjust_brightness_contrast(img, brightness=12, contrast=-15)
    img = add_warmth(img, 8)
    img = adjust_saturation(img, 0.85)
    img = fade(img, 0.18)
    return img

def filter_sutro(img):
    img = adjust_brightness_contrast(img, brightness=-15, contrast=20)
    img = vignette(img, 0.25)
    img = adjust_saturation(img, 0.9)
    return img

def filter_1977(img):
    img = adjust_brightness_contrast(img, brightness=10, contrast=10)
    img = color_shift(img, b=-5, g=0, r=15)
    img = adjust_saturation(img, 1.2)
    img = glow_effect(img, strength=0.35, blur_sigma=8)
    return img

def filter_kelvin(img):
    img = adjust_brightness_contrast(img, brightness=10, contrast=22)
    img = adjust_saturation(img, 1.55)
    img = add_warmth(img, 25)
    img = color_shift(img, b=-10, g=5, r=20)
    return img

def filter_slumber(img):
    img = adjust_brightness_contrast(img, brightness=8, contrast=-18)
    img = adjust_saturation(img, 0.75)
    img = glow_effect(img, strength=0.25, blur_sigma=12)
    return img

def filter_perpetua(img):
    img = adjust_brightness_contrast(img, brightness=18, contrast=8)
    img = add_cool(img, 12)
    img = adjust_saturation(img, 1.1)
    return img

def filter_clarendon(img):
    img = adjust_brightness_contrast(img, brightness=5, contrast=25)
    img = adjust_saturation(img, 1.25)
    img = add_cool(img, 6)
    img = sharpen(img, 0.7)
    return img

def filter_juno(img):
    img = adjust_brightness_contrast(img, brightness=8, contrast=18)
    img = adjust_saturation(img, 1.35)
    img = add_warmth(img, 10)
    img = split_tone(img, highlights=(0, 10, 30), shadows=(20, 0, 20), strength=0.18)
    return img

def filter_gingham(img):
    img = adjust_brightness_contrast(img, brightness=8, contrast=-5)
    img = adjust_saturation(img, 0.92)
    b, g, r = cv2.split(img)
    g = clamp(g + 10)
    img = cv2.merge([b, g, r])
    img = fade(img, 0.12)
    return img

def filter_aden(img):
    img = adjust_brightness_contrast(img, brightness=12, contrast=-8)
    img = adjust_saturation(img, 0.75)
    img = add_cool(img, 15)
    img = fade(img, 0.1)
    return img

def filter_brooklyn(img):
    img = adjust_brightness_contrast(img, brightness=8, contrast=15)
    img = add_warmth(img, 12)
    img = glow_effect(img, strength=0.3, blur_sigma=15)
    img = vignette(img, 0.45)
    return img

def filter_earlybird(img):
    img = sepia(img, strength=0.6)
    img = adjust_brightness_contrast(img, brightness=-5, contrast=20)
    img = add_warmth(img, 15)
    img = vignette(img, 0.25)
    return img

def filter_hudson(img):
    img = adjust_brightness_contrast(img, brightness=15, contrast=10)
    img = add_cool(img, 18)
    img = adjust_saturation(img, 1.2)
    img = split_tone(img, highlights=(0, 5, 25), shadows=(20, 10, 30), strength=0.2)
    return img

def filter_inkwell(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    out = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    out = adjust_brightness_contrast(out, brightness=5, contrast=30)
    return out

def filter_lofi(img):
    img = adjust_brightness_contrast(img, brightness=-10, contrast=25)
    img = adjust_saturation(img, 1.5)
    img = vignette(img, 0.3)
    return img

def filter_nashville(img):
    img = adjust_brightness_contrast(img, brightness=10, contrast=8)
    img = add_warmth(img, 18)
    img = color_shift(img, b=-10, g=5, r=25)
    img = fade(img, 0.15)
    return img

def filter_rise(img):
    img = adjust_brightness_contrast(img, brightness=15, contrast=5)
    img = add_warmth(img, 20)
    img = glow_effect(img, strength=0.4, blur_sigma=10)
    img = adjust_saturation(img, 1.15)
    return img

def filter_valencia(img):
    img = adjust_brightness_contrast(img, brightness=8, contrast=-10)
    img = add_warmth(img, 22)
    img = adjust_saturation(img, 1.1)
    img = fade(img, 0.12)
    return img

def filter_walden(img):
    img = adjust_brightness_contrast(img, brightness=12, contrast=8)
    img = add_cool(img, 10)
    img = adjust_saturation(img, 1.25)
    img = glow_effect(img, strength=0.25, blur_sigma=8)
    return img

def filter_amaro(img):
    img = adjust_brightness_contrast(img, brightness=10, contrast=18)
    img = adjust_saturation(img, 1.3)
    img = split_tone(img, highlights=(0, 15, 30), shadows=(30, 10, 0), strength=0.2)
    return img

def filter_brannan(img):
    img = adjust_brightness_contrast(img, brightness=0, contrast=28)
    img = adjust_saturation(img, 0.85)
    img = color_shift(img, b=5, g=-5, r=15)
    return img

def filter_hefe(img):
    img = adjust_brightness_contrast(img, brightness=5, contrast=25)
    img = adjust_saturation(img, 1.4)
    img = add_warmth(img, 10)
    img = vignette(img, 0.2)
    return img

def filter_toaster(img):
    img = adjust_brightness_contrast(img, brightness=-5, contrast=20)
    img = add_warmth(img, 25)
    img = color_shift(img, b=-15, g=0, r=30)
    img = vignette(img, 0.25)
    return img

def filter_tokyo(img):
    img = adjust_brightness_contrast(img, brightness=10, contrast=20)
    img = add_cool(img, 20)
    img = adjust_saturation(img, 1.2)
    img = sharpen(img, 0.8)
    return img

def filter_maven(img):
    img = adjust_brightness_contrast(img, brightness=5, contrast=12)
    img = adjust_saturation(img, 0.7)
    img = split_tone(img, highlights=(0, 20, 30), shadows=(30, 0, 30), strength=0.25)
    return img

def filter_vesper(img):
    img = adjust_brightness_contrast(img, brightness=-10, contrast=22)
    img = add_warmth(img, 15)
    img = adjust_saturation(img, 0.9)
    img = color_shift(img, b=-10, g=10, r=15)
    return img

def filter_moon(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    out = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    out = adjust_brightness_contrast(out, brightness=0, contrast=25)
    return out

def filter_xpro(img):
    img = adjust_brightness_contrast(img, brightness=5, contrast=28)
    img = adjust_saturation(img, 1.3)
    img = add_warmth(img, 14)
    img = vignette(img, 0.35)
    return img

def filter_mayfair(img):
    img = adjust_brightness_contrast(img, brightness=10, contrast=8)
    img = split_tone(img, highlights=(0, 20, 35), shadows=(0, 0, 10), strength=0.18)
    img = fade(img, 0.08)
    return img
