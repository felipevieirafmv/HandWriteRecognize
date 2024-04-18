import os
import cv2 as cv
import numpy as np
from utils import find, resize2
from test import transform_image

def prediction(model):
    if os.path.exists('uploaded.png'):
        transform_image()
        org = cv.imread('filtered.png')
    else:
        org = cv.imread('screen.png')

    gray_img = cv.cvtColor(org, cv.COLOR_BGR2GRAY)

    def valor_para_caractere(valor):
        if 1 <= valor <= 10:
            return str(valor - 1)
        elif 11 <= valor <= 36:
            return chr(valor + 54)
        elif 37 <= valor <= 62:
            return chr(valor + 60)
        else:
            return None

    rects = []
    for i in range(len(gray_img)):
        row = gray_img[i]
        for k in range(len(row)):
            if row[k] == 0:
                rects.append(find(gray_img, k, i))

    rects = sorted(rects, key=lambda x: x[0][0])

    results = []

    mark = org.copy()
    for rect in rects:
        x0, y0 = rect[0]
        x1, y1 = rect[1]
        pred_img = mark[y0:y1, x0:x1].copy()
        pred_img = resize2(pred_img, 128)
        pred_img = pred_img.reshape((1, 128, 128, 3))
        results.append(model.predict(pred_img))

    str2 = ''.join(valor_para_caractere(np.argmax(result) + 1) for result in results)

    return str2