import cv2
import numpy as np
from .utils import *

def filter_cinematic_teal_orange(img):
    img = adjust_brightness_contrast(img, brightness=0, contrast=20)
    img = split_tone(img, highlights=(0, 15, 35), shadows=(25, 0, 0), strength=0.25)
    img = adjust_saturation(img, 1.15)
    return img

def filter_chrome(img):
    img = adjust_brightness_contrast(img, brightness=0, contrast=30)
    img = adjust_saturation(img, 0.6)
    img = sharpen(img, 0.9)
    return img

def filter_summer(img):
    img = adjust_brightness_contrast(img, brightness=15, contrast=8)
    img = add_warmth(img, 18)
    img = adjust_saturation(img, 1.3)
    img = glow_effect(img, strength=0.2, blur_sigma=8)
    return img

def filter_autumn(img):
    img = adjust_brightness_contrast(img, brightness=5, contrast=12)
    img = add_warmth(img, 25)
    img = color_shift(img, b=-15, g=5, r=30)
    img = adjust_saturation(img, 1.2)
    return img

def filter_winter(img):
    img = adjust_brightness_contrast(img, brightness=12, contrast=10)
    img = add_cool(img, 20)
    img = adjust_saturation(img, 0.9)
    img = sharpen(img, 0.6)
    return img

def filter_spring(img):
    img = adjust_brightness_contrast(img, brightness=15, contrast=-5)
    img = adjust_saturation(img, 1.1)
    img = color_shift(img, b=5, g=10, r=5)
    img = glow_effect(img, strength=0.2, blur_sigma=10)
    return img
    
def filter_blue_hour(img):
    img = adjust_brightness_contrast(img, brightness=-8, contrast=18)
    img = add_cool(img, 25)
    img = adjust_saturation(img, 1.15)
    img = split_tone(img, highlights=(25, 10, 0), shadows=(0, 0, 30), strength=0.3)
    return img

def filter_noir(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = adjust_brightness_contrast(gray, brightness=-10, contrast=35)
    out = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    out = vignette(out, 0.3)
    return out

def filter_dramatic(img):
    img = adjust_brightness_contrast(img, brightness=0, contrast=35)
    img = adjust_saturation(img, 1.4)
    img = sharpen(img, 1.2)
    img = vignette(img, 0.4)
    return img

def filter_cross_process(img):
    img = adjust_brightness_contrast(img, brightness=5, contrast=25)
    img = adjust_saturation(img, 1.5)
    img = color_shift(img, b=15, g=-10, r=20)
    img = split_tone(img, highlights=(0, 30, 40), shadows=(40, 0, 30), strength=0.3)
    return img

def filter_bleach_bypass(img):
    img = adjust_brightness_contrast(img, brightness=0, contrast=28)
    img = adjust_saturation(img, 0.5)
    img = sharpen(img, 0.8)
    return img

def filter_pastel_dream(img):
    img = adjust_brightness_contrast(img, brightness=20, contrast=-20)
    img = adjust_saturation(img, 1.15)
    img = glow_effect(img, strength=0.3, blur_sigma=15)
    img = fade(img, 0.25)
    return img

def filter_sunset_vibes(img):
    img = adjust_brightness_contrast(img, brightness=8, contrast=12)
    img = color_shift(img, b=-25, g=5, r=35)
    img = add_warmth(img, 25)
    img = split_tone(img, highlights=(0, 20, 50), shadows=(40, 10, 0), strength=0.25)
    return img

def filter_cotton_candy(img):
    img = adjust_brightness_contrast(img, brightness=15, contrast=-10)
    img = adjust_saturation(img, 1.2)
    img = split_tone(img, highlights=(0, 25, 60), shadows=(60, 25, 60), strength=0.2)
    img = fade(img, 0.15)
    return img

def filter_neon_glow(img):
    img = adjust_brightness_contrast(img, brightness=10, contrast=25)
    img = adjust_saturation(img, 2.0)
    img = glow_effect(img, strength=0.5, blur_sigma=8)
    img = sharpen(img, 0.5)
    return img

def filter_arctic(img):
    img = adjust_brightness_contrast(img, brightness=18, contrast=5)
    img = add_cool(img, 30)
    img = adjust_saturation(img, 0.7)
    img = fade(img, 0.15)
    return img

def filter_desert(img):
    img = adjust_brightness_contrast(img, brightness=10, contrast=15)
    img = add_warmth(img, 30)
    img = color_shift(img, b=-20, g=10, r=25)
    img = adjust_saturation(img, 1.1)
    return img

def filter_forest(img):
    img = adjust_brightness_contrast(img, brightness=-5, contrast=15)
    img = color_shift(img, b=5, g=25, r=-5)
    img = adjust_saturation(img, 1.25)
    return img

def filter_fire(img):
    img = adjust_brightness_contrast(img, brightness=5, contrast=20)
    img = color_shift(img, b=-30, g=15, r=40)
    img = adjust_saturation(img, 1.5)
    return img

def filter_ice(img):
    img = adjust_brightness_contrast(img, brightness=15, contrast=10)
    img = add_cool(img, 35)
    img = adjust_saturation(img, 0.6)
    img = sharpen(img, 0.7)
    return img

def filter_lavender(img):
    img = adjust_brightness_contrast(img, brightness=12, contrast=-8)
    img = color_shift(img, b=20, g=5, r=15)
    img = adjust_saturation(img, 0.9)
    img = fade(img, 0.12)
    return img

def filter_mint(img):
    img = adjust_brightness_contrast(img, brightness=15, contrast=-5)
    img = color_shift(img, b=10, g=20, r=5)
    img = adjust_saturation(img, 0.95)
    img = fade(img, 0.1)
    return img

def filter_peach(img):
    img = adjust_brightness_contrast(img, brightness=12, contrast=-8)
    img = add_warmth(img, 20)
    img = color_shift(img, b=-10, g=10, r=20)
    img = fade(img, 0.15)
    return img

def filter_rose_gold(img):
    img = adjust_brightness_contrast(img, brightness=10, contrast=8)
    img = color_shift(img, b=-5, g=8, r=25)
    img = adjust_saturation(img, 1.1)
    img = glow_effect(img, strength=0.2, blur_sigma=10)
    return img

def filter_moody_blues(img):
    img = adjust_brightness_contrast(img, brightness=-12, contrast=22)
    img = add_cool(img, 25)
    img = adjust_saturation(img, 1.2)
    img = vignette(img, 0.35)
    return img
