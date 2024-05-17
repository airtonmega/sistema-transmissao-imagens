import cv2
import numpy as np

def decode_image(file):
    np_array = np.frombuffer(file, np.uint8)
    return cv2.imdecode(np_array, cv2.IMREAD_COLOR)
