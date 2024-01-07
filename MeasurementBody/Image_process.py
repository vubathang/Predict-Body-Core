import cv2

image = cv2.imread('E:\Projects\GIT\Predict-Body-Core\data\image\i3.jpg')


def getCannyEdge(image):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  edges = cv2.Canny(gray, 100, 200)
  contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  return contours

canny_image = getCannyEdge(image)

def getCoordiantes(image):
    for contour in getCannyEdge(image):
        for point in contour:
            x, y = point

            if y < min_y:
                min_y = point
            if y > max_y:
                max_y = point
            if x > max_x:
                max_x = point
            if x < min_x:
                min_x = point

    return min_x, min_y, max_x, max_y



def createBoundingBox():
    # Extract the coordinates of the box
    min_x, min_y, max_x, max_y = getCoordiantes(canny_image)

    # Create a bounding box around the person
    bounding_box = cv2.rectangle(canny_image, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)

    return bounding_box

bounding_box = createBoundingBox()
cv2.imshow("Bounding Box", bounding_box)
cv2.waitKey(0)
cv2.destroyAllWindows()
