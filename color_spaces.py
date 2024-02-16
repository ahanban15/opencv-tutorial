import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/cat.jpg")

# cv.imshow('Cat', img)

# BGR TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# BGR TO HSV HUE SATURATION VALUE
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("Hsv", hsv)

# BGR TO LAB washed down version
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# OUTSIDE OF OPENCV WE USE RGB FORMAT SO
# USING DIFFERENT LIBRARY MAY LEAD TO INVERSION OF COLORS AS OPENCV USES BGR FORMAT

# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow("RGB", rgb)

# plt.imshow(img)
# plt.show()

# HSV TO BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow("HSV TO BGR", hsv_bgr)

# LAB TO BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LAB TO BGR", lab_bgr)

cv.waitKey(0)
