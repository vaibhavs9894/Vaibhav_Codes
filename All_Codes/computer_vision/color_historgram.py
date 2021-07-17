import cv2
import matplotlib.pyplot as plt

im = cv2.imread(r'C:\Users\Lenovo\Pictures\abstract.jpg')
cv2.imshow("image",im)
m = cv2.resize(im, (500, 500))

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr =cv2.calcHist([im],[i],None,[256],[0,256])
    
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
cv2.imshow('image',im)
cv2.waitKey(0)