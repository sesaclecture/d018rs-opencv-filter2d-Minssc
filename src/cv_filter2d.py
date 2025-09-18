import cv2
import sys
import numpy as np

def identity_kernel() -> np.array:
    arr = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]
    kernel = np.array(arr, dtype=np.float32)
    return kernel

def ones_kernel() -> np.array:
    arr = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]
    kernel = np.array(arr, dtype=np.float32)
    return kernel

def original_kernel() -> np.array:
    arr = [[0, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]
    kernel = np.array(arr, dtype=np.float32)
    return kernel

def doubling_kernel() -> np.array:
    arr = [[0, 0, 0],
           [0, 2, 0],
           [0, 0, 0]]
    kernel = np.array(arr, dtype=np.float32)
    return kernel
