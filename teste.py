import cv2 as cv
import numpy as np

org = cv.imread('a2.png')
img = org.copy()

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
threshold, img = cv.threshold(
    img, 110, 255, cv.THRESH_BINARY
)

# Algortimo do balde de tinta do paint (Ele mesmo, ao vivo e sem core)
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

rects = []
for i in range(len(img)):
    row = img[i]
    for k in range(len(row)):
        if row[k] == 0:
            rects.append(find(img, k, i))

mark = org.copy()
for rect in rects:
    mark = cv.rectangle(mark, rect[0], rect[1], (0, 255, 0), 2)

cv.imshow('image', mark)
cv.waitKey(0)