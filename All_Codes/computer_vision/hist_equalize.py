import cv2

im = cv2.imread(r'‪C:\Users\Lenovo\Pictures\abstract-986a.jpg')
im = cv2.resize(im, (600,300))
bw  = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(bw)
cv2.imshow('Original', bw)
cv2.imshow('Histogram Equalization', equ)
cv2.waitKey(0)