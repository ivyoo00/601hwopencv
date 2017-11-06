# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
#import numpy as np

def main():
    
    img = cv2.imread("/Users/gejiali/学习/ECE/EC601/OpenCV_homework/Test_images/baboon.jpg")
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Original Image", img)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex3/gray.png",gray)   
    
    current_threshold = 128
    max_threshold = 255
    threshold1 = 27
    threshold2 = 125
    
    ret,img_binary = cv2.threshold(gray,current_threshold,max_threshold,cv2.THRESH_BINARY)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex4/binary.png",img_binary)
    
    ret,img_binary1 = cv2.threshold(gray,threshold1,max_threshold,cv2.THRESH_BINARY)
    ret,binary_inv = cv2.threshold(gray,threshold2,max_threshold,cv2.THRESH_BINARY_INV)
    img_thresholding = cv2.bitwise_and(img_binary1,binary_inv)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex4/band_thresholding.png",img_thresholding)
    
    ret,img_semi = cv2.threshold(gray,current_threshold,max_threshold,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    img_semi = cv2.bitwise_and(gray,img_semi)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex4/Semi Thresholding.png",img_semi)
    
    img_adaptive_thresh = cv2.adaptiveThreshold(gray, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex4/Adaptive Thresholding.png",img_adaptive_thresh)
    
    
if __name__ == "__main__":
    main()
