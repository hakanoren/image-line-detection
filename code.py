import cv2
import numpy as np

image = cv2.imread("image4i.jpg")

image = image[60:400,60:350]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(image,(5,5),0)
ret, threshold = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)

edges = cv2.Canny(threshold,100,200)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=50)

for line in lines:
    x, y, w, h = line[0]
    cv2.line(blur,(x, y),(w, h),(0,255,0), 2)



cv2.imshow("blur",blur)
cv2.imshow("image",image)


cv2.waitKey(0)
cv2.destroyAllWindows()

