# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np

def Add_salt_pepper_Noise(mat, pa, pb):
    
    rows,cols = mat.shape
    amount1 = int(rows*cols*pa)
    amount2 = int(rows*cols*pb)
    
    for i in range(amount1):
        mat[np.random.randint(0,rows-1), np.random.randint(0,cols-1)]=0
        
    for i in range(amount2):
        mat[np.random.randint(0,rows-1), np.random.randint(0,cols-1)]=255
        
    return mat

def Add_gaussian_Noise(mat1, mean, sigma):
    
    noice_m=mat1.copy()
    cv2.randn(noice_m,mean,sigma)
    cv2.add(mat1, noice_m, noice_m)
    
    return noice_m


def main():
    
    img = cv2.imread("/Users/gejiali/学习/ECE/EC601/OpenCV_homework/Test_images/baboon.jpg")
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Original Image", img)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex3/gray.png",gray)   
    
    mean = 5
    sigma = 20
    pa = 0.03
    pb = 0.03
          
    gauss_noiseImage = Add_gaussian_Noise(gray,mean,sigma)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex3/gaussiannoise.png",gauss_noiseImage)
    boxfilter_img = cv2.boxFilter(gauss_noiseImage, -1, (3, 3))
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex3/gaussianBoxfilter.png",boxfilter_img)
    gaussfilter_img=cv2.GaussianBlur(gauss_noiseImage, (3,3), 1.5, 3)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex3/gaussianGaussfilter.png",gaussfilter_img)
    medianfilter_img=cv2.medianBlur(gauss_noiseImage,5)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex3/gaussianMedianfilter.png",medianfilter_img)
    
    pepper_saltImage=Add_salt_pepper_Noise(gray,pa,pb)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex3/peppersaltnoise.png",pepper_saltImage)
    boxfilter_img = cv2.boxFilter(pepper_saltImage, -1, (3, 3))
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex3/peppersaltBoxfilter.png",boxfilter_img)
    gaussfilter_img=cv2.GaussianBlur(pepper_saltImage, (3,3), 1.5, 3)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex3/peppersaltGaussfilter.png",gaussfilter_img)
    medianfilter_img=cv2.medianBlur(pepper_saltImage,5)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex3/peppersaltMedianfilter.png",medianfilter_img)
    
if __name__ == "__main__":
    main()
