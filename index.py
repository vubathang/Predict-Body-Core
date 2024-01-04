import cv2
from MeasurementBody import measurement as ms

image = cv2.imread('./data/image/i3.jpg')

landmarks = ms.getLandmark(image)
x = image.shape[1]
y = image.shape[0]

print(x, y)

cv2.line(image, ms.getHeadPoint(image), ms.getAvgHeel(landmarks, x, y), (0, 225, 0), 3)

ratio_image = 500 / y

image = cv2.resize(image, (0, 0), fx=ratio_image, fy=ratio_image)
cv2.imshow('Result', image)
cv2.waitKey(0)