import os
import cv2 as cv

img = cv.imread('imgTest\cadernoHD2.jpeg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

width = 300
height = 400
img = cv.resize(img, (width, height), interpolation= cv.INTER_AREA)

threshold, img = cv.threshold(
    img, 0, 255, cv.THRESH_OTSU
)

cv.imshow('image', img)
cv.waitKey(0)