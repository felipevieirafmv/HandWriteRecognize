import os
import random
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def find(img, x, y):
    x0 = x
    xf = x
    y0 = y
    yf = y

    queue = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]

    while len(queue) > 0:
        x, y = queue.pop()
        
        if y < 0 or y >= len(img):
            continue
        row = img[y]

        if x < 0 or x >= len(row):
            continue
        pixel = row[x]

        if pixel == 255:
            continue
        img[y][x] = 255

        x0 = min(x0, x)
        xf = max(xf, x)
        y0 = min(y0, y)
        yf = max(yf, y)

        queue.append((x + 1, y))
        queue.append((x - 1, y))
        queue.append((x, y + 1))
        queue.append((x, y - 1))

    return ((x0, y0), (xf, yf))


def crop_images(origin):

    image_dir = f"./Img/{origin}"
    images = os.listdir(image_dir)

    for img_name in images:
        img_path = os.path.join(image_dir, img_name)
        org = cv.imread(img_path)
        img = org.copy()

        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        threshold, img = cv.threshold(
            img, 110, 255, cv.THRESH_BINARY
        )        

        rects = []
        for i in range(len(img)):
            row = img[i]
            for k in range(len(row)):
                if row[k] == 0:
                    rects.append(find(img, k, i))

        if(len(rects) > 1):
            continue

        mark = org.copy()
        for rect in rects:
            mark = cv.rectangle(mark, rect[0], rect[1], (255, 255, 255), 0)

        x0 = rects[0][0][0]
        y0 = rects[0][0][1]
        x1 = rects[0][1][0]
        y1 = rects[0][1][1]

        mark = mark[y0:y1, x0:x1]
        cv.imwrite(f"./Img/{origin}/{img_name}", mark)


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

    
def resize2(img, size):
    heigth, width = img.shape[:2]
    nheigth = size
    nwidth = size
    
    new_img = np.ones((nheigth, nwidth, 3), dtype=np.uint8) * 255
    
    scale = min(nheigth/heigth, nwidth/width)

    swidth = int(width * scale)
    sheight = int(heigth * scale)

    y = (nheigth - sheight) // 2
    x = (nwidth - swidth) // 2

    img = cv.resize(img, (swidth, sheight))
    
    new_img[y:y+sheight, x:x+swidth] = img

    return new_img