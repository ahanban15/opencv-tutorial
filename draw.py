import cv2 as cv
import numpy as np

# black image
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# paint the image green
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# paint part of image to a certain colour
# blank[200:300, 300:400] = 255, 0, 0

# Rectangle
#cv.FILLED
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
# cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=cv.FILLED)
# cv.imshow('Partial', blank)

# cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
# cv.imshow('Partial', blank)

# Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
# cv.imshow('Circle', blank)

# Draw a Line
# cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255))
# cv.imshow('Line', blank)

# how to write text on image
cv.putText(blank, "Hello", (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

cv.waitKey(0)