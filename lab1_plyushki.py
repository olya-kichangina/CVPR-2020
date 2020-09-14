import time
import numpy as np
import cv2
import matplotlib.pyplot as plt

#блок записи видео в реальном времени
cap0 = cv2.VideoCapture(0)
width = int(cap0.get(3))
height = int(cap0.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('our_video.avi', fourcc, 20.0, (width, height))
while cap0.isOpened():

    ret, image = cap0.read()
    degradation = cv2.GaussianBlur(image, (51, 51), 0)  # размытие для того,чтобы сохранить анонимнсть:)
    if ret == True:
        out.write(degradation)

        cv2.imshow('video', degradation)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap0.release()
out.release()

#блок отображения записанного видео в сером цвете с линией и прямоугольником
cap1 = cv2.VideoCapture('our_video.avi')
while cap1.isOpened():
    ret, image = cap1.read()
    if ret == True:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(gray, cv2.cv2.COLOR_GRAY2BGR)
        gray = cv2.line(gray, (130, 400), (13, 200), (0, 125, 0), 7)
        gray = cv2.rectangle(gray, (50, 50), (130, 140), (255, 0, 0), 7)
        cv2.imshow('gray', gray)

    if cv2.waitKey(1) == ord('q'):
        break
cap1.release()
cv2.destroyAllWindows()