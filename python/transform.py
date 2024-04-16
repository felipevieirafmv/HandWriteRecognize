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
        thick = random.randint(1, 40)
        img_path = os.path.join(image_dir, img_name)
        img = cv.imread(img_path, cv.COLOR_BGRA2GRAY)
        if rand >= 0:
            img = cv.dilate(img, np.ones((thick, thick)))
            cv.imwrite(f"./Img/{origin}/dil{origin}-{i}.png", img)
        else:
            img = cv.erode(img, np.ones((thick, thick)))
            cv.imwrite(f"./Img/{origin}/ero{origin}-{i}.png", img)
        i += 1


def crop_128(origin):
    image_dir = f"./Img/{origin}"
    images = os.listdir(image_dir)
    x0 = 150
    y0 = 0
    x1 = 1050
    y1 = 900
    for img_name in images:
        img_path = os.path.join(image_dir, img_name)
        img = cv.imread(img_path, cv.COLOR_BGRA2GRAY)
        cropped_image = img[y0:y1, x0:x1]
        cv.imwrite(f"./Img/{origin}/{img_name}", cropped_image)

def resize_images(origin):
    image_dir = f"./Img/{origin}"
    images = os.listdir(image_dir)
    width = 128
    height = 128
    for img_name in images:
        img_path = os.path.join(image_dir, img_name)
        img = cv.imread(img_path, cv.COLOR_BGRA2GRAY)
        resized_image = cv.resize(img, (width, height), interpolation= cv.INTER_AREA)
        cv.imwrite(f"./Img/{origin}/{img_name}", resized_image)


for j in range(1, 63):
    perc = j / 62 * 100
    perc = round(perc, 2)
    if(j < 10):
        j = f"0{j}"
    change_thickness(j)
    resize_images(j)
    crop_images(j)
    print(f"{j}/62, {perc}% concluded.")
