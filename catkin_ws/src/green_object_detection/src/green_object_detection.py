#!/usr/bin/env python

import rospy
import cv2 as cv
import numpy as np
import ctypes
from std_msgs.msg import Header
from geometry_msgs.msg import PointStamped

class ObjectDetector:
    def __init__(self):
        # Cargar libreria -------------
        self.lib = ctypes.CDLL("/home/melissa/Interfaces_Project/catkin_ws/src/green_object_detection/src/library/libmultiply_coordinates.so")
        
        # Crea Publisher para el topic donde se publicaran las nuevas coordenadas
        self.pub = rospy.Publisher('/coordinates', PointStamped, queue_size=10)
        
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
        hsv = cv.cvtColor(self.cv_image, cv.COLOR_BGR2HSV)

        # Rangos de verde
        lower_green = np.array([40, 40, 40])
        upper_green = np.array([70, 255, 255])

        mask = cv.inRange(hsv, lower_green, upper_green)
        contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
        # Dibujar contornos con rectangulo
        for contour in contours:
            # Coordenadas del rectangulo
            x, y, w, h = cv.boundingRect(contour)
            
            # Dibujar cuadro alrededor del contorno
            cv.rectangle(self.cv_image, (x, y), (x + w, y + h), (255, 0, 0), 2)            
        
        if len(contours) > 0:
            # Encontrar el contorno mas grande
            c = max(contours, key=cv.contourArea)
            cx = 0
            cy = 0
            
            # Calcular el centro del contorno
            M = cv.moments(c)
            
            if M['m00'] > 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
            else:
                pass
            
            # Coordenadas ctypes
            newCoordX = ctypes.c_int(cx)
            newCoordY = ctypes.c_int(cy)
            # Importacion de libreria y nuevas coordenadas*100
            self.lib.multiply_coordinates(ctypes.byref(newCoordX), ctypes.byref(newCoordY))
            print("COORDENADA X: ", newCoordX.value)
            print("COORDENADA Y: ", newCoordY.value)
            
            # PointStamped con coordenadas multiplicadas y su timestamp
            self.timePoint = PointStamped()
            self.timePoint.header = Header(stamp=rospy.Time.now(), frame_id="camera_frame")
            self.timePoint.point.x = newCoordX.value #cx
            self.timePoint.point.y = newCoordY.value #cy
            
            # Publish objeto en el topico
            self.pub.publish(self.timePoint)

def main():
    rospy.init_node('object_detector')
    obj = ObjectDetector()
    obj.vid.release()
    rospy.spin()

if __name__ == '__main__':
    main()
    cv.destroyAllWindows()