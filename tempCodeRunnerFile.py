# import cv2
# from MeasurementBody import measurement as ms

# image = cv2.imread('./data/image/i3.jpg')

# landmarks = ms.getLandmark(image)
# x = image.shape[1]
# y = image.shape[0]

# print(x, y)

# # Vẽ tất cả các điểm trên ảnh
# for point in ms.getAvgHeel(landmarks, x, y)[2]:
#     cv2.circle(image, tuple(point), 5, (0, 255, 0), -1)  # Vẽ một hình tròn với bán kính 5 tại mỗi điểm

# cv2.line(image, ms.getHeadPoint(image), ms.getAvgHeel(landmarks, x, y)[:2], (0, 255, 0), 3)

# ratio_image = 500 / y

# image = cv2.resize(image, (0, 0), fx=ratio_image, fy=ratio_image)
# cv2.imshow('Result', image)
# cv2.waitKey(0)
# print("Space between shoulders:", result_space_shoulder)
# # ms.printDistances(landmarks