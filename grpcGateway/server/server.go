package main

import (
	"context"
	"log"
	"net"

	// "net/http"
	//"runtime"

	pb "example.com/grpcGateway/gen/proto"

	"google.golang.org/grpc"
)

type coordinatesServiceServer struct {
	pb.UnimplementedCoordinatesServiceServer
}

// Faltaria una function de user

func (s *coordinatesServiceServer) GetCoordinates(ctx context.Context, req *pb.Empty) (*pb.PointStamped, error) {

	// Establecer la conexión con el servidor gRPC
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Error al conectar: %v", err)
	}
	defer conn.Close()

	// Crear un cliente para el servicio de coordenadas
	client := pb.NewCoordinatesServiceClient(conn)

	// Llamar al método GetCoordinates del servidor
	// req := &pb.Empty{}
	//res, err := client.GetCoordinates(context.Background(), req)
	res, err := client.GetCoordinates(context.Background(), &pb.Empty{})
	if err != nil {
		log.Printf("Error al llamar al servidor: %v", err)
		return nil, err
	}

	return res, nil
	//&log.Println("Coordinadas recibidas: %+v", res)

	// Version original V1
	// return &pb.PointStamped{
	// 	Header: &pb.PointStamped_Header{
	// 		Seq:     1,
	// 		Stamp:   123,
	// 		FrameId: "camera",
	// 	},
	// 	Point: &pb.PointStamped_Coordinates{
	// 		X: 12,
	// 		Y: 234,
	// 	},
	// }, nil

	//
	//log.Printf("Punto estampado: %+v", &pb.PointStamped{})

	//return &pb.PointStamped{}, nil

}

func main() {
	// added V2
	// go func() {
	// 	// aux
	// 	mux := runtime.NewServeMux() // ??
	// 	// register
	// 	pb.RegisterCoordinatesServiceHandlerServer(context.Background(), mux, &coordinatesServiceServer{})
	// 	// ttps server
	// 	log.Fatalln(http.ListenAndServe("localhost:50052", mux))
	// 	// g h
	// }()

	// Create TCP Server
	listener, err := net.Listen("tcp", "localhost:50052") // puerto 50051
	if err != nil {
		log.Fatalln(err)
	}

	// Create gRPC Server
	grpcServer := grpc.NewServer()

	pb.RegisterCoordinatesServiceServer(grpcServer, &coordinatesServiceServer{})

	log.Println("Listening on 50052")

	// Connect servers
	err = grpcServer.Serve(listener)
	if err != nil {
		// log.Println(err) // V1
		log.Fatalf("Problema con servidor: %v", err)
	} //else {
	//log.Println("Listening on 50051")
	//}
}
