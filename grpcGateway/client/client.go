package main

import (
	"context"
	"log"

	pb "example.com/grpcGateway/gen/proto"

	"google.golang.org/grpc"
)

func main() {
	// Establecer la conexión con el servidor gRPC
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Error al conectar: %v", err)
	}
	defer conn.Close()

	// Crear un cliente para el servicio de coordenadas
	client := pb.NewCoordinatesServiceClient(conn)

	// Llamar al método GetCoordinates del servidor
	req := &pb.Empty{}
	res, err := client.GetCoordinates(context.Background(), req)
	if err != nil {
		log.Fatalf("Error al llamar al servidor: %v", err)
	}

	log.Println(res)
}
