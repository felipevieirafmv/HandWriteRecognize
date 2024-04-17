import os
import cv2 as cv
import numpy as np
from utils import find, resize2


def transform_image():
    img = cv.imread('uploaded.png')

    width = 400
    height = 300
    img = cv.resize(img, (width, height))

    blue_value = 180
    mult_color = 1.7

    for k in range(len(img)):
        row = img[k]
        for l in range(len(row)):
            b, g, r = row[l]
            b *= mult_color
            g *= mult_color
            r *= mult_color
            if b > 255:
                b = 255
            if g > 255:
                g = 255
            if r > 255:
                r = 255
            row[l] = (b, g, r)

    for j in range(len(img)):
        row = img[j]
        for i in range(len(row)):
            b, g, r = row[i]
            if r < blue_value and g < blue_value and b > blue_value:
                row[i] = (0, 0, 0)
            else:
                row[i] = (255, 255, 255)

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # blur = cv.GaussianBlur(img,(5,5),0)
    img = cv.erode(img, np.ones((10, 10)))
    img = cv.dilate(img, np.ones((7, 7)))
    # ret3,img2 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

    cv.imwrite("filtered.png", img)
