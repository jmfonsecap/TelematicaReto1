package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	pb "google.golang.org/grpc/code/PaymentWork/protos"
)

var (
	port = flag.Int("port", 8080, "The server port")
	addr = flag.String("addr", "52.91.127.103:8080", "the address to connect to")
)


type server struct {
	pb.UnimplementedPaymentServer
}



func (s *server) PagarTodoCarro(ctx context.Context, in *pb.None) (*pb.Respuesta, error) {
	flag.Parse()

	conn, err := grpc.Dial(*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewCartClient(conn)


	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	r, err := c.GetCarLength(ctx,&pb.Nada{})
	if err != nil {
		log.Fatalf("Error: %v", err)
	}
	sum:= 0
	p, err := c.GetPrecio(ctx,&pb.PedidoId{PedidoId:int32(1)})
	for i := 1; i <= int(r.GetLength()); i++ {
		p, err = c.GetPrecio(ctx,&pb.PedidoId{PedidoId:int32(i)})
		if err != nil {
			log.Fatalf("Error: %v", err)
		}
		c.RemoveFromCart(ctx,&pb.PedidoId{PedidoId:int32(i)})
		
		sum += int(p.GetPrecio())
		
	}
	result := fmt.Sprintf("%s%d", "El total a pagar es: ",sum)

	return &pb.Respuesta{Message: result }, nil
}
func (s *server) PagarItemEnElCarro(ctx context.Context, in *pb.ItemId) (*pb.Respuesta, error) {
	flag.Parse()
	// Set up a connection to the server.
	conn, err := grpc.Dial(*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewCartClient(conn)

	// Contact the server and print out its response.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	p, err := c.GetPrecio(ctx,&pb.PedidoId{PedidoId:in.GetPedidoId()})
	c.RemoveFromCart(ctx,&pb.PedidoId{PedidoId:in.GetPedidoId()})
	result := fmt.Sprintf("%s%d", "El total a pagar es: ",p)
	return &pb.Respuesta{Message: result }, nil
}

func main() {
	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterPaymentServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
