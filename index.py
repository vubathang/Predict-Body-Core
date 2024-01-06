import cv2
from MeasurementBody import measurement as ms

image = cv2.imread('./data/image/i3.jpg')

landmarks = ms.getLandmark(image)
x = image.shape[1]
y = image.shape[0]

print(x, y)

cv2.line(image, ms.getHeadPoint(image), ms.getAvgHeel(landmarks, x, y)[:2], (0, 255, 0), 3)

ratio_image = 500 / y

image = cv2.resize(image, (0, 0), fx=ratio_image, fy=ratio_image)
cv2.imshow('Result', image)
cv2.waitKey(0)
print("Khoảng cách:", ms.getDistances(landmarks))

<<<<<<< HEAD
# Giả định tỷ lệ pixel-to-cm
estimated_pixel_to_cm_ratio = 150

# Tính toán khoảng cách và chuyển đổi sang đơn vị cm
distances_in_pixels = ms.getDistances(landmarks)
distances_in_cm = [distance * estimated_pixel_to_cm_ratio for distance in distances_in_pixels]

print("Khoảng cách (cm): ", distances_in_cm)
=======
>>>>>>> d8f801bf48470d7f4e609d407640ae3786cc9611
