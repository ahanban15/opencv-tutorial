import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
# cv.imshow('Gray', gray)

# Blur : Gaussian blur
# kernel size should be odd
# blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge cascade
canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny', canny)

# blurred edge cascade
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

# dilating the image
# dilated = cv.dilate(canny, (3,3), iterations=5)
# cv.imshow('Dilated', dilated)

# eroded = cv.erode(dilated, (3,3), iterations=5)
# cv.imshow('Eroded', eroded)

# resize
# interpolation useful to shrink to smaller dimensions than original
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)