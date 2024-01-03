import cv2
import mediapipe as mp

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

def getAvgHeel(landmarks, x, y):
  right_heel = (int(landmarks[29].x * x),
                int(landmarks[29].y * y))
  left_heel = (int(landmarks[30].x * x),
              int(landmarks[30].y * y))
  x_avg = int((right_heel[0] + left_heel[0]) / 2)
  y_avg = int((right_heel[1] + left_heel[1]) / 2)
  return [x_avg, y_avg]