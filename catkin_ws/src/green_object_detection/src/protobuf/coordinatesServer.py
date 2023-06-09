#!/usr/bin/env python3

from concurrent import futures
import logging
import sys
import time
import signal

import object_coordinates_pb2
import object_coordinates_pb2_grpc
import rospy
from geometry_msgs.msg import PointStamped
from concurrent.futures import ThreadPoolExecutor
import grpc

class CoordinatesService(object_coordinates_pb2_grpc.coordinatesServiceServicer):
    """@class CoordinatesService
    Creación de servidor.
    """
    
    def __init__(self):
        """@brief CoordinatesService/__init__
        Suscripción al tópico /coordinates de donde se reciben las coordenadas obtenidas de la detección del objeto color verde,
        """
        self.timePoints = PointStamped()
        # Subscriber a nodo con coordenadas*100
        rospy.Subscriber("/coordinates", PointStamped, self.coordinates_callback)
        
    def getCoordinates(self, request, context):
        """@class getCoordinates
        Desde el archivo object_coordinates_pb2 generado, se crea una instancia del mensaje 'PointStamped' y establece sus campos utilizando valores de otros objetos o variables.
        """
        return object_coordinates_pb2.PointStamped(
            header = object_coordinates_pb2.PointStamped.Header(
                seq = self.timePoints.header.seq,
                stamp = int(self.timePoints.header.stamp.to_sec()),
                frame_id = self.timePoints.header.frame_id
            ),
            point = object_coordinates_pb2.PointStamped.Coordinates(
                x = self.timePoints.point.x,
                y = self.timePoints.point.y
            )
    )
    
    def coordinates_callback(self,data):
        self.timePoints = data
        
# Detiene el servidor
def stop_server(signum,frame):
    print('Asistiendo signal {signum} ({signal.Signals(signum).name}).')
    time.sleep(1)
    sys.exit(0)
    
def main():
    """@brief main
    
    """
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    object_coordinates_pb2_grpc.add_coordinatesServiceServicer_to_server(CoordinatesService(), server)
    
    server.add_insecure_port('127.0.0.1:' + port)
    server.start()
    print("Servidor iniciado, escuchando en " + port)
    # rospy.spin()
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        server.stop(0)
        print("Servidor detenido.")
    
if __name__ == '__main__':
    signal.signal(signal.SIGINT, stop_server)
    rospy.init_node('grpc_server_node', anonymous=True)
    logging.basicConfig()    
    main()