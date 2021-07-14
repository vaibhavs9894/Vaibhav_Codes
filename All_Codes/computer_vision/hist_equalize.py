import cv2

im = cv2.imread(r'C:\Users\HP 346 G3\Downloads\cute-birds-romance-4k-2r-1920x1080.jpg')
im = cv2.resize(im,(600,300))
bw  = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(bw)
cv2.imshow('Original', bw)
cv2.imshow('Histogram Equalization', equ)
cv2.waitKey(0)