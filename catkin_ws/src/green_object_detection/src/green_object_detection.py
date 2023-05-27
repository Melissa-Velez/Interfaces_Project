#!/usr/bin/env python

import rospy
import cv2 as cv
import numpy as np
from sensor_msgs.msg import Image # Creo que no lo utilizo
from cv_bridge import CvBridge # Arriba x2
import ctypes
from std_msgs.msg import Header
from geometry_msgs.msg import PointStamped

class ObjectDetector:
    def __init__(self):
        # Cargar librería -------------
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
            
            # Llamar a la función de multiplicación de la librería de C++
            self.lib.multiply_coordinates(ctypes.byref(ctypes.c_int(x)), ctypes.byref(ctypes.c_int(y)))
            
            # Dibujar cuadro alrededor del contorno
            cv.rectangle(self.cv_image, (x, y), (x + w, y + h), (255, 0, 0), 2)            
        
        if len(contours) > 0:
            # Encontrar el contorno mas grande (suponiendo que es el objeto que buscamos)
            c = max(contours, key=cv.contourArea)
            
            # Calcular el centro del contorno
            M = cv.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            # Print de coordenadas del centro del objeto verde
            print("Coordenada X: ", cx)
            print("Coordenada Y: ", cy)
            
            # PointStamped con coordenadas multiplicadas y su timestamp
            timePoint = PointStamped()
            timePoint.header = Header(stamp=rospy.Time.now(), frame_id="camera_frame")
            timePoint.point.x = cx
            timePoint.point.y = cy
            
            # Publish objeto en el tópico
            self.pub.publish(timePoint)

def main():
    rospy.init_node('object_detector')
    obj = ObjectDetector()
    obj.vid.release()
    rospy.spin()

if __name__ == '__main__':
    main()
    cv.destroyAllWindows()