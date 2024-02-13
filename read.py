import cv2 as cv

# # reading image
# # takes path to image and returns matrix of pixels
# img = cv.imread("Photos/cat.jpg")
#
# # displays the image as a new window: title of window and the actual matrix of pixels
# cv.imshow('Cat', img)
#
# # keyboard binding function waits for a key to be pressed
# cv.waitKey(0)

# if large images then it would go off-screen

# *****************************************************

# reading video
# parameter is integer variable of using webcam or use path to video
# for webcam
# capture = cv.VideoCapture(0)



capture = cv.VideoCapture('Videos/dog.mp4')
# use while loop for videos using while loop video is read frame by frame

while True:
    isTrue, frame = capture.read()

    # we can display the individual frames
    cv.imshow('Video', frame)

    # to stop video from playing indefinitely, break out of loop if letter d is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()