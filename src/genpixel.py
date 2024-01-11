from cv2 import cv2
import numpy as np


class PixelConverter:
    """
     Generating pixel from binary strings or vice versa.

    example:
    0101 -> img([0,0,0][255,255,255],[0,0,0],[255,255,255])
    """

    def __init__(self, width, height):
        self.width = None
        self.height = None
        self.frame = None
