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
  specific_points = [2, 5, 11, 12, 13, 14, 15, 16, 19, 20, 23, 24, 25, 26, 27, 28]  # Chỉ quan tâm đến một số điểm cụ thể
  body_points = getSpecificBodyPoints(landmarks, x, y, specific_points)
  for point_index in specific_points:
    body_points.append((int(landmarks[point_index].x * x), int(landmarks[point_index].y * y)))
  return body_points

def getDistanceFrom2Points(point1, point2):
  return sqrt(pow(point1.x-point2.x,2) + pow(point1.y-point2.y,2))

def getDistances(landmarks):
  l = [[11, 12], [11, 13], [13, 15], [12, 14],[14, 16],[11, 15], [12, 16], [11, 23], [12, 24], [23, 25], [24, 26], [25, 27], [26, 28], [23, 29], [24, 30], [11, 29], [12, 30]]
  l_distances = []

  for i in l:
    l_distances.append(getDistanceFrom2Points(landmarks[i[1]], landmarks[i[0]]))
  return l_distances


def getAvgHeel(landmarks, x, y):
  right_heel = (int(landmarks[29].x * x),
                int(landmarks[29].y * y))
  left_heel = (int(landmarks[30].x * x),
              int(landmarks[30].y * y))
  
  
  x_avg = int((right_heel[0] + left_heel[0]) / 2)
  y_avg = int((right_heel[1] + left_heel[1]) / 2)
  
  return [x_avg, y_avg]
 
  # left_eye = (int(landmarks[2].x * x),
  #             int(landmarks[2].y * y))
  # right_eye = (int(landmarks[5].x * x),
  #             int(landmarks[5].y * y))    
      
  # nose = (int(landmarks[0].x * x),
  #         int(landmarks[0].y * y))
  
  # left_ear = (int(landmarks[7].x * x),
  #             int(landmarks[7].y * y))
  # right_ear = (int(landmarks[8].x * x),
  #             int(landmarks[8].y * y))
  
  # mouth_left = (int(landmarks[9].x * x),
  #               int(landmarks[9].y * y))
  # mouth_right = (int(landmarks[10].x * x),
  #               int(landmarks[10].y * y))
  
  
  # right_shoulder = (int(landmarks[12].x * x),
  #                 int(landmarks[12].y * y))
  # left_shoulder = (int(landmarks[11].x * x),
  #                 int(landmarks[11].y * y))
  
  
  # # khuỷu tay
  # left_elbow = (int(landmarks[13].x * x),
  #                 int(landmarks[13].y * y))
  # right_elbow = (int(landmarks[14].x * x),
  #                 int(landmarks[14].y * y))
  
  # left_shoulder = (int(landmarks[11].x * x),
  #                 int(landmarks[11].y * y))
  
  # # cổ tay
  # left_wrist = (int(landmarks[15].x * x),
  #               int(landmarks[15].y * y))
  # right_wrist = (int(landmarks[16].x * x),
  #               int(landmarks[16].y * y))
  
  # # ngón cái
  # left_index = (int(landmarks[19].x * x),
  #               int(landmarks[19].y * y))
  # right_index = (int(landmarks[20].x * x),
  #               int(landmarks[20].y * y))
  
  # # hông
  # left_hip = (int(landmarks[23].x * x),
  #               int(landmarks[23].y * y))
  # right_hip = (int(landmarks[24].x * x),
  #               int(landmarks[24].y * y))
  
  
  # # đầu gối
  # left_knee = (int(landmarks[25].x * x),
  #               int(landmarks[25].y * y))
  # right_knee = (int(landmarks[26].x * x),
  #               int(landmarks[26].y * y))
  
  # #cổ chân
  # left_ankle = (int(landmarks[27].x * x),
  #               int(landmarks[27].y * y))
  # right_ankle = (int(landmarks[28].x * x),
  #               int(landmarks[28].y * y))
  