import cv2
import mediapipe as mp
from math import sqrt

def getCannyEdge(image):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  edges = cv2.Canny(gray, 100, 200)
  contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  return contours

def getLandmark(image):
  mp_pose = mp.solutions.pose
  pose = mp_pose.Pose(min_detection_confidence=0.3, min_tracking_confidence=0.3)
  results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  return results.pose_landmarks.landmark

def getHeadPoint(image):
  max = [0, 10000000]
  for c in getCannyEdge(image):
    for p in c:
      if(p[0][1] < max[1]):
        max = [p[0][0], p[0][1]]
  return max

def getSpecificBodyPoints(landmarks, x, y, specific_points):
  body_points = []
  for point_index in specific_points:
    body_points.append((int(landmarks[point_index].x * x), int(landmarks[point_index].y * y)))
  return body_points

def getDistanceFrom2Points(point1, point2, x, y):
  return sqrt(pow(point1.x * x-point2.x * x,2) + pow(point1.y * y -point2.y * y,2))

def getDistances(landmarks, img):
  x = img.shape[1]
  y = img.shape[0]
  l = [[11, 12], [11, 13], [13, 15], [12, 14],[14, 16],[11, 15], [12, 16], [11, 23], [12, 24], [23, 25], [24, 26], [25, 27], [26, 28], [23, 29], [24, 30], [11, 29], [12, 30]]
  l_distances = []

  for i in l:
    l_distances.append(getDistanceFrom2Points(landmarks[i[1]], landmarks[i[0]], x, y))
  return l_distances


def getAvgHeel(landmarks, x, y):
  right_heel = (int(landmarks[29].x * x),
                int(landmarks[29].y * y))
  left_heel = (int(landmarks[30].x * x),
              int(landmarks[30].y * y))
  
  
  x_avg = int((right_heel[0] + left_heel[0]) / 2)
  y_avg = int((right_heel[1] + left_heel[1]) / 2)
  
  return [x_avg, y_avg]
 

def test(img, h):
  point1 = getHeadPoint(img)
  point2 = getAvgHeel(getLandmark(img), img.shape[1], img.shape[0])
  h_img = sqrt(pow(point1[1]-point2[1],2) + pow(point1[0]-point2[0],2))
  ratio = h / h_img

  l = getDistances(getLandmark(img), img)
   # Khai báo biến count và total_distance cho từng cặp giá trị
  count_67, count_24, count_1415 = 0, 0, 0
  total_distance_67, total_distance_24, total_distance_1415 = 0, 0, 0

  for index, distance in enumerate(l, start=1):
    print("Thứ tự {}: {}".format(index, distance * ratio))
    
    # Kiểm tra và tính trung bình cho từng cặp giá trị
    if index in [6, 7]:
        total_distance_67 += distance * ratio
        count_67 += 1
    elif index in [2, 4]:
        total_distance_24 += distance * ratio
        count_24 += 1
    elif index in [14, 15]:
        total_distance_1415 += distance * ratio
        count_1415 += 1

  # Tính và in trung bình cho từng cặp giá trị
  print("Trung bình của Thứ tự 6 và 7: {}".format(total_distance_67 / count_67) if count_67 > 0 else "Không có giá trị để tính trung bình.")
  print("Trung bình của Thứ tự 14 và 15: {}".format(total_distance_1415 / count_1415) if count_1415 > 0 else "Không có giá trị để tính trung bình.")
  print("Trung bình của Thứ tự 2 và 4: {}".format(total_distance_24 / count_24) if count_24 > 0 else "Không có giá trị để tính trung bình.")
  