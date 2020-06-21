import cv2
import numpy as np
import imutils
import datetime

gun = cv2.CascadeClassifier('cascade.xml')
videocapture = cv2.VideoCapture(0)

firstFrame = None
gun_exit = False

while True:
    ret, frame = videocapture.read()
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gun1 = gun.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    if len(gun1) > 0:
        gun_exit = True

    for (x, y, w, h) in gun1:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi = gray[y:y + h, x:x + w]
        color = frame[y:y + h, x:x + w]

    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.putText(frame, datetime.datetime.now().strftime("% A % d % B % Y % I: % M : % S % P"), (10, frame.shape[0] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    cv2.imshow("security feed", frame)
    key = cv2.waitKey(1) & 0xff

    if key == ord('q'):
        break

    if gun_exit:
        print("gun Dectected")

    else:
        print("not dectected")

videocapture.release()
cv2.destroyAllWindows()
