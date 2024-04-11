import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import random

def show(img):
    plt.imshow(img, cmap='gray')
    plt.show()
    return img


def change_thickness(origin):
    image_dir = f"./Img/{origin}"
    images = os.listdir(image_dir)
    i = 0
    for img_name in images:
        rand = random.randint(-1, 3)
        thick = random.randint(1, 50)
        img_path = os.path.join(image_dir, img_name)
        img = cv.imread(img_path, cv.COLOR_BGRA2GRAY)
        if rand >= 0:
            img = cv.dilate(img, np.ones((thick, thick)))
            cv.imwrite(f"./Img/{origin}/dil{origin}-{i}.png", img)
        else:
            img = cv.erode(img, np.ones((thick, thick)))
            cv.imwrite(f"./Img/{origin}/ero{origin}-{i}.png", img)
        i += 1

for j in range(1, 63):
    if(j < 10):
        j = f"0{j}"
    change_thickness(j)