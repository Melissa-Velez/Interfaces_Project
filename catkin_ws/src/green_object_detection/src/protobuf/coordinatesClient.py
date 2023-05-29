from __future__ import print_function

import grpc
import logging
import object_coordinates_pb2
import object_coordinates_pb2_grpc


# def execute(): #jv
#     with grpc.insecure_channel('localhost:50051') as channel:
#         stub = object_coordinates_pb2_grpc.coordinatesServiceStub(channel)
#         response = stub.getCoords(object_coordinates_pb2.Empty())
#         print("Coordenadas recibidas: " + str(response))

def execute():
    # Crea el canal apuntando al servidor 
    channel = grpc.insecure_channel('localhost:50051')
    coordinates_client = object_coordinates_pb2_grpc.coordinatesServiceStub(channel)
    # Llama al metodo getCoordinates del servicio RPC
    response = coordinates_client.getCoordinates(object_coordinates_pb2.Empty())
    print("Coordenadas recibidas: " + str(response))

if __name__ == '__main__':
    logging.basicConfig()
    execute()    