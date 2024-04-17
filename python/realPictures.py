import os
import cv2 as cv
import numpy as np
from utils import find, resize2
from tensorflow.keras import models, layers, activations, \
    optimizers, utils, losses, initializers, metrics, callbacks

org = cv.imread('screen.png')

if os.path.exists('uploaded.png'):
    org = cv.imread('uploaded.png')

img = org.copy()
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

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
    pred_img = mark[rect[0][1] : rect[1][1], rect[0][0] : rect[1][0]]
    pred_img = resize2(pred_img, 128)
    pred_img = pred_img.reshape((1, 128, 128, 3))
    results.append(model.predict(pred_img))

str2 = ''

for result in results:
    str2 = str2 + valor_para_caractere(np.argmax(result) + 1)

print(str2)