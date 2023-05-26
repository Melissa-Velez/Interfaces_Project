#!/usr/bin/env python

import rospy
import cv2 as cv
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ObjectDetector:
    def __init__(self):
    #def camera_display():
        # Captura de video
        self.vid = cv.VideoCapture(1)
        self.cv_image = None
        while True:
            if not self.vid.isOpened():
                print("No es posible visualizar camara")
                exit()
            ret, self.cv_image = self.vid.read()
            self.image_green_detector(self.cv_image)
            cv.imshow("Camera", self.cv_image)
            if cv.waitKey(1) == ord('q'):
                break

    def image_green_detector(self, data):
        #cv_image = self.bridge.imgmsg_to_cv(data, "bgr8")
        hsv = cv.cvtColor(self.cv_image, cv.COLOR_BGR2HSV)

        lower_green = np.array([40, 40, 40])
        upper_green = np.array([70, 255, 255])

        mask = cv.inRange(hsv, lower_green, upper_green)
        contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        # Dibujar contornos
        #cv.drawContours(self.cv_image, contours, -1, (255, 0, 0), 2) # Dibujar contornos
        #cv.imshow("mask", mask) #Observar la mascara
        
        # Dibujar contornos con rectangulo
        for contour in contours:
            # Coordenadas del rectangulo
            x, y, w, h = cv.boundingRect(contour)
            # Dibujar cuadro alrededor del contorno
            cv.rectangle(self.cv_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        
        if len(contours) > 0:
            # Encontrar el contorno mas grande (suponiendo que es el objeto que buscamos)
            c = max(contours, key=cv.contourArea)
            # Calcular el centro del contorno
            M = cv.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            print("Coordenada X: ", cx)
            print("Coordenada Y: ", cy)

def main():
    rospy.init_node('object_detector')
    obj = ObjectDetector()
    obj.vid.release()
    rospy.spin()

if __name__ == '__main__':
    main()
    cv.destroyAllWindows()













