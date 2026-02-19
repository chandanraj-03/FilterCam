import cv2
import numpy as np
from .utils import *

def filter_mirror_horizontal(img):
    h, w = img.shape[:2]
    left = img[:, :w//2]
    mirrored = cv2.flip(left, 1)
    img[:, w//2:] = mirrored[:, :w-w//2]
    return img



def filter_fisheye(img):
    h, w = img.shape[:2]
    
    map_x = np.zeros((h, w), dtype=np.float32)
    map_y = np.zeros((h, w), dtype=np.float32)
    
    cx, cy = w / 2, h / 2
    
    for y in range(h):
        for x in range(w):
            dx = (x - cx) / cx
            dy = (y - cy) / cy
            r = np.sqrt(dx**2 + dy**2)
            
            if r <= 1:
                theta = np.arctan2(dy, dx)
                r2 = r ** 1.5  
                
                map_x[y, x] = cx + r2 * cx * np.cos(theta)
                map_y[y, x] = cy + r2 * cy * np.sin(theta)
    
    result = cv2.remap(img, map_x, map_y, cv2.INTER_LINEAR)
    return result

def filter_swirl(img):
    h, w = img.shape[:2]
    cy, cx = h // 2, w // 2
    
    Y, X = np.ogrid[:h, :w]
    dx = X - cx
    dy = Y - cy
    
    r = np.sqrt(dx**2 + dy**2)
    theta = np.arctan2(dy, dx)
    
    theta_new = theta + r / 50.0
    
    map_x = (cx + r * np.cos(theta_new)).astype(np.float32)
    map_y = (cy + r * np.sin(theta_new)).astype(np.float32)
    
    return cv2.remap(img, map_x, map_y, cv2.INTER_LINEAR)

def filter_bulge(img):
    h, w = img.shape[:2]
    K = np.array([[w/2, 0, w/2], [0, h/2, h/2], [0, 0, 1]])
    D = np.array([0.5, 0.5, 0, 0]) 
    return cv2.undistort(img, K, D)

def filter_pinch(img):
    h, w = img.shape[:2]
    K = np.array([[w/2, 0, w/2], [0, h/2, h/2], [0, 0, 1]])
    D = np.array([-0.5, -0.5, 0, 0]) 
    return cv2.undistort(img, K, D)

def filter_ripple(img):
    h, w = img.shape[:2]
    img_out = np.zeros(img.shape, dtype=img.dtype)
    
    map_x = np.zeros((h, w), dtype=np.float32)
    map_y = np.zeros((h, w), dtype=np.float32)
    
    for y in range(h):
        for x in range(w):
            map_x[y, x] = x + 10 * np.sin(y / 10.0)
            map_y[y, x] = y + 10 * np.sin(x / 10.0)
            
    return cv2.remap(img, map_x, map_y, cv2.INTER_LINEAR)

def filter_twist(img):
    h, w = img.shape[:2]
    cy, cx = h / 2.0, w / 2.0
    
    y_indices, x_indices = np.indices((h, w), dtype=np.float32)
    
    dx = x_indices - cx
    dy = y_indices - cy
    r = np.sqrt(dx**2 + dy**2)
    theta = np.arctan2(dy, dx)
    
    twist_amount = 0.005
    theta_new = theta + r * twist_amount
    
    map_x = cx + r * np.cos(theta_new)
    map_y = cy + r * np.sin(theta_new)
    
    return cv2.remap(img, map_x.astype(np.float32), map_y.astype(np.float32), cv2.INTER_LINEAR)

def filter_perspective_tilt(img):
    h, w = img.shape[:2]
    src_pts = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    dst_pts = np.float32([[w*0.2, h*0.1], [w*0.8, h*0.1], [0, h], [w, h]])
    
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    return cv2.warpPerspective(img, M, (w, h))
