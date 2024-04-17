import os
import cv2 as cv
import numpy as np
from utils import find, resize2

org = cv.imread('imgTest/felipe.jpeg')
org = cv.cvtColor(org, cv.COLOR_BGR2GRAY)

width = 300
height = 400
org = cv.resize(org, (width, height))

blur = cv.GaussianBlur(org,(5,5),0)
ret3,img = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow('image', img)
cv.waitKey(0)