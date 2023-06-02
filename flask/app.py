from flask import Flask, render_template
from google.protobuf.json_format import MessageToJson
import object_coordinates_pb2
import object_coordinates_pb2_grpc
import json
import grpc


app = Flask(__name__, template_folder= "templates")

def commServer():
    channel = grpc.insecure_channel('127.0.0.1:50052')
    coordinates_client = object_coordinates_pb2_grpc.coordinatesServiceStub(channel)
    # Llama al metodo getCoordinates del servicio RPC
    response = coordinates_client.getCoordinates(object_coordinates_pb2.Empty())
    return response

@app.route('/get_coordinates')
def get_coordinates():
    coords = json.loads(MessageToJson(commServer()))
    return render_template('index.html', coords=coords)

if __name__ == '__main__':
    app.run(port=5000)
    
