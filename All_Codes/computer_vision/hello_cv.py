import cv2
im = cv2.imread('django.jpg')
print("height",im.shape[0])
print("width",im.shape[1])
im = cv2.resize(im, (500, 500))
bw = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow("normal image",im)
cv2.imshow("bw image",bw)
cv2.waitKey(0)