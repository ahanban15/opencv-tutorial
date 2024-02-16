import cv2 as cv

img = cv.imread("Photos/cat.jpg")

cv.imshow('Cat', img)

# AVERAGING: average of nearby pixel intensities
average = cv.blur(img, (7,7))
# cv.imshow('Average Blur', average)

# GAUSSIAN
gauss = cv.GaussianBlur(img, (7,7), 0)
# cv.imshow('Gaussian blur', gauss)

# MEDIAN BLUR
median = cv.medianBlur(img, 3)
# cv.imshow('Median blur', median)

# BILATERAL BLUR
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral blur', median)

cv.waitKey(0)