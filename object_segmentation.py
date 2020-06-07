import cv2 as cv
import numpy as np

def nothing(x):
    pass

cap = cv.VideoCapture(0)

cv.namedWindow('Trackbars')

cv.createTrackbar('l-h', 'Trackbars', 22, 180, nothing)
cv.createTrackbar('l-s', 'Trackbars', 95, 255, nothing)
cv.createTrackbar('l-v', 'Trackbars', 152, 255, nothing)
cv.createTrackbar('U-h', 'Trackbars', 27, 180, nothing)
cv.createTrackbar('U-s', 'Trackbars', 255, 255, nothing)
cv.createTrackbar('U-v', 'Trackbars', 255, 255, nothing)

while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos('l-h', 'Trackbars')
    l_s = cv.getTrackbarPos('l-s', 'Trackbars')
    l_v = cv.getTrackbarPos('l-v', 'Trackbars')
    U_h = cv.getTrackbarPos('U-h', 'Trackbars')
    U_s = cv.getTrackbarPos('U-s', 'Trackbars')
    U_v = cv.getTrackbarPos('U-v', 'Trackbars')

    lower_color = np.array([l_h, l_s, l_v])
    upper_color = np.array([U_h, U_s, U_v])

    mask = cv.inRange(hsv, lower_color, upper_color)

    result = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('mask', mask)
    cv.imshow('frame', frame)
    cv.imshow('result', result)

    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()