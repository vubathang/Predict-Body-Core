import cv2
from MeasurementBody import measurement as ms

image = cv2.imread("D:\Studying\PROJECT\img_PredictBody/6/front_img.jpg")

landmarks = ms.getLandmark(image)
x = image.shape[1]
y = image.shape[0]

print(x, y)

cv2.line(image, ms.getHeadPoint(image), ms.getAvgHeel(landmarks, x, y)[:2], (0, 255, 0), 3)
specific_points = [2, 5, 11, 12, 13, 14, 15, 16, 19, 20, 23, 24, 25, 26, 27, 28] 
body_points = ms.getSpecificBodyPoints(landmarks, x, y, specific_points)
for point in body_points:
    cv2.circle(image, tuple(point), 5, (0, 255, 0), -1)  # Vẽ một hình tròn với bán kính 5 tại mỗi điểm

ratio_image = 500 / y

image = cv2.resize(image, (0, 0), fx=ratio_image, fy=ratio_image)
cv2.imshow('Result', image)
cv2.waitKey(0)

# print("Khoảng cách:", ms.getDistances(landmarks))
h = 172 # Nhập cái số đo height trong ảnh vào đây nhé
ms.test(image, h)
