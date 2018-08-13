import numpy as np
import cv2

height = 850
width = 1700

emptyImage = np.ones((height, width, 3), np.uint8) * 255

cv2.rectangle(emptyImage, (200, 60), (1640, 660), (255, 250, 250), cv2.FILLED)

cv2.line(emptyImage, (185, 60), (185, 675), (255, 200, 200)) #vertical axis
cv2.line(emptyImage, (185, 675), (1640, 675), (255, 200, 200)) #horizontal axis

cv2.imshow("image", emptyImage)
cv2.waitKey()
