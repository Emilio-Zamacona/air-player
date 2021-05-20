import cv2
import numpy as np

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cv2.namedWindow("TrackedBars")
cv2.resizeWindow("TrackedBars", 640, 240)

def on_trackbar(val):
    ret,img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue_min = cv2.getTrackbarPos("Hue Min", "TrackedBars")
    hue_max = cv2.getTrackbarPos("Hue Max", "TrackedBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackedBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackedBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackedBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackedBars")

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    imgMASK = cv2.inRange(imgHSV, lower, upper)

    cv2.imshow("Mask", imgMASK)
    cv2.imshow("img",img)
    print(str(hue_min)+" - "+str(hue_max)+" - "+str(sat_min)+" - "+str(sat_max)+" - "+str(val_min)+" - "+str(val_max))

cv2.createTrackbar("Hue Min", "TrackedBars", 0, 179, on_trackbar)
cv2.createTrackbar("Hue Max", "TrackedBars", 179, 179, on_trackbar)
cv2.createTrackbar("Sat Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Sat Max", "TrackedBars", 255, 255, on_trackbar)
cv2.createTrackbar("Val Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Val Max", "TrackedBars", 255, 255, on_trackbar)


while True:
    on_trackbar(1)   
    if cv2.waitKey(1) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
