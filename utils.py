import cv2
import numpy as np

def clamp(img):
    return np.clip(img, 0, 255).astype(np.uint8)

def adjust_brightness_contrast(img, brightness=0, contrast=0):
    b = brightness
    c = contrast

    if b != 0:
        shadow = b if b > 0 else 0
        highlight = 255 if b > 0 else 255 + b
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow
        img = cv2.addWeighted(img, alpha_b, img, 0, gamma_b)

    if c != 0:
        f = 131 * (c + 127) / (127 * (131 - c))
        alpha_c = f
        gamma_c = 127 * (1 - f)
        img = cv2.addWeighted(img, alpha_c, img, 0, gamma_c)

    return img

def gamma_correction(img, gamma=1.0):
    invGamma = 1.0 / max(gamma, 1e-6)
    table = np.array([(i / 255.0) ** invGamma * 255 for i in range(256)]).astype("uint8")
    return cv2.LUT(img, table)

def add_grain(img, amount=12):
    noise = np.random.normal(0, amount, img.shape).astype(np.float32)
    out = img.astype(np.float32) + noise
    return clamp(out)

def sepia(img, strength=1.0):
    img_f = img.astype(np.float32)
    kernel = np.array([
        [0.272, 0.534, 0.131],
        [0.349, 0.686, 0.168],
        [0.393, 0.769, 0.189]
    ], dtype=np.float32)

    sep = cv2.transform(img_f, kernel)
    out = (1 - strength) * img_f + strength * sep
    return clamp(out)

def glow_effect(img, strength=0.25, blur_sigma=10):
    blur = cv2.GaussianBlur(img, (0, 0), blur_sigma)
    out = cv2.addWeighted(img, 1.0, blur, strength, 0)
    return clamp(out)

def color_shift(img, b=0, g=0, r=0):
    B, G, R = cv2.split(img)
    B = B.astype(np.int16) + b
    G = G.astype(np.int16) + g
    R = R.astype(np.int16) + r
    B = np.clip(B, 0, 255).astype(np.uint8)
    G = np.clip(G, 0, 255).astype(np.uint8)
    R = np.clip(R, 0, 255).astype(np.uint8)
    return cv2.merge([B, G, R])

def edge_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(gray_blur, 50, 150)
    edges_inv = 255 - edges
    out = cv2.cvtColor(edges_inv, cv2.COLOR_GRAY2BGR)
    return out

def cartoonify(img):
    smooth = cv2.bilateralFilter(img, 9, 80, 80)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(gray, 255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 9, 2)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    out = cv2.bitwise_and(smooth, edges)
    return out

def neon_edges(img):
    edges = cv2.Canny(img, 80, 170)
    edges = cv2.GaussianBlur(edges, (5, 5), 0)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    out = cv2.addWeighted(img, 0.85, edges, 0.8, 0)
    return clamp(out)

def adjust_saturation(img, sat=1.0):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:, :, 1] *= sat
    hsv[:, :, 1] = np.clip(hsv[:, :, 1], 0, 255)
    return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

def add_warmth(img, strength=10):
    b, g, r = cv2.split(img)
    r = clamp(r + strength)
    g = clamp(g + strength * 0.5)
    return cv2.merge([b, g, r])

def add_cool(img, strength=10):
    b, g, r = cv2.split(img)
    b = clamp(b + strength)
    r = clamp(r - strength * 0.3)
    return cv2.merge([b, g, r])

def vignette(img, strength=0.6):
    h, w = img.shape[:2]
    x = cv2.getGaussianKernel(w, w * strength)
    y = cv2.getGaussianKernel(h, h * strength)
    mask = (y @ x.T)
    mask = mask / mask.max()
    out = img.astype(np.float32)
    out *= mask[:, :, None]
    return clamp(out)

def sharpen(img, amount=1.0):
    blur = cv2.GaussianBlur(img, (0, 0), 3)
    out = cv2.addWeighted(img, 1 + amount, blur, -amount, 0)
    return out

def fade(img, amount=0.12):
    img = adjust_brightness_contrast(img, brightness=10, contrast=-10)
    overlay = np.full_like(img, 255)
    return cv2.addWeighted(img, 1 - amount, overlay, amount, 0)

def split_tone(img, highlights=(0, 20, 40), shadows=(40, 0, 40), strength=0.25):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
    h_mask = (gray > 0.5).astype(np.float32)[:, :, None]
    s_mask = (gray <= 0.5).astype(np.float32)[:, :, None]

    tint_h = np.array(highlights, dtype=np.float32)
    tint_s = np.array(shadows, dtype=np.float32)

    out = img.astype(np.float32)
    out += strength * (h_mask * tint_h + s_mask * tint_s)
    return clamp(out)
