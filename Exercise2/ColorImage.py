import cv2
#import numpy as np
#import sys

def main():

    
    img = cv2.imread("/Users/gejiali/学习/ECE/EC601/OpenCV_homework/Test_images/Lenna.png")
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Original Image", img)

    red,green,blue = cv2.split(img)

    RGBpixel = img[20,25]
    print RGBpixel

    cv2.imshow("Red",red)
    cv2.imshow("Green",green)
    cv2.imshow("Blue",blue)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex2/Red.png", red)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex2/Green.png", green)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex2/Blue.png", blue)

    ycrcb_image = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    Y, Cb, Cr = cv2.split(ycrcb_image)

    YCRCBpixel = ycrcb_image[20,25]
    print YCRCBpixel

    cv2.imshow("Y",   Y)
    cv2.imshow("Cb",  Cb)
    cv2.imshow("Cr",  Cr)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex2/Y.png", Y)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex2/Cb.png", Cb)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex2/Cr.png", Cr)

    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(hsv_image)

    HSVpixel = hsv_image[20,25]
    print HSVpixel

    cv2.imshow("Hue", H)
    cv2.imshow("Saturation", S)
    cv2.imshow("Value", V)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex2/Hue.png", H)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex2/Saturation.png", S)
    cv2.imwrite("/Users/gejiali/学习/ECE/EC601/ex2/Value.png", V)
		
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
       
if __name__ == "__main__":
    main()
