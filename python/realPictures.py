import os
import cv2 as cv
import numpy as np
from python.utils import find, resize2
from tensorflow.keras import models, layers, activations, \
    optimizers, utils, losses, initializers, metrics, callbacks

org = cv.imread('imgTest/a2.png')

# width = 300
# height = 400
# org = cv.resize(org, (width, height))

img = org.copy()
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur = cv.GaussianBlur(img,(5,5),0)
# ret3,img = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

def valor_para_caractere(valor):
    if valor >= 1 and valor <= 10:
        return str(valor - 1)
    elif valor >= 11 and valor <= 36:
        return chr(valor + 54)
    elif valor >= 37 and valor <= 62:
        return chr(valor + 60)
    else:
        return None


def get_x0(square):
    return square[0][0]

model = models.load_model("checkpoints/crop-91-85.keras")

rects = []
for i in range(len(img)):
    row = img[i]
    for k in range(len(row)):
        if row[k] == 0:
            rects.append(find(img, k, i))

rects = sorted(rects, key = get_x0)

results = []

mark = org.copy()
for rect in rects:
    print(f"Y0: {rect[0][1]}, Y1: {rect[1][1]}")
    print(f"X0: {rect[0][0]}, X1: {rect[1][0]}")
    pred_img = mark[rect[0][1] : rect[1][1], rect[0][0] : rect[1][0]]
    pred_img = resize2(pred_img, 128)
    cv.imshow('image', pred_img)
    cv.waitKey(0)
    pred_img = pred_img.reshape((1, 128, 128, 3))
    results.append(model.predict(pred_img))
    # mark = cv.rectangle(mark, rect[0], rect[1], (0, 0, 255), 2)

for result in results:
    print(valor_para_caractere(np.argmax(result) + 1))