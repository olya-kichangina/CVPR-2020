import numpy as np
import cv2
import matplotlib.pyplot as plt

capture = cv2.VideoCapture(0)

# блок считывания с вебки в реальном времени
while True:
    ret, image = capture.read()
    degradation = cv2.GaussianBlur(image, (51,51), 0) #размытие для того,чтобы сохранить анонимнсть:)
    cv2.imshow('image', degradation)
    key = cv2.waitKey(10)
    if key == 27: # выход при нажатии 'Esc'
        capture.release()
        break
    if key == 13: # скрин при нажатии 'Enter'
        cv2.imwrite('our_image.jpg', degradation)


# блок по выведению скрина на экран
cv2.destroyAllWindows()
screenshot = cv2.imread('our_image.jpg')
normal = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
fig1 = plt.figure()
plt.title('Screenshot from web-camera')
plt.imshow(normal)
plt.axis("off")
plt.show()
plt.close(fig1)


# блок по выведению скрина серым цветом + линия + прямоугольник
screenshot_2 = cv2.imread('our_image.jpg', cv2.IMREAD_GRAYSCALE)
gray = cv2.cvtColor(screenshot_2, cv2.COLOR_BGR2RGB)
gray = cv2.line(gray, (130, 400), (13, 200), (0, 125, 0), 7)
gray = cv2.rectangle(gray, (50, 50), (130, 140), (255, 0, 0), 7)
fig2 = plt.figure()
plt.title('Gray screenshot from web-camera with line and rectangle')
plt.imshow(gray)
plt.show()
