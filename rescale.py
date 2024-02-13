import cv2 as cv

# img = cv.imread('Photos/dog_large.jpg')
# cv.imshow('Dog', img)

# works for images videos and live videos
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Videos/dog.mp4')
# use while loop for videos using while loop video is read frame by frame

# works only for Live video
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    # we can display the individual frames
    # cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    # to stop video from playing indefinitely, break out of loop if letter d is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()