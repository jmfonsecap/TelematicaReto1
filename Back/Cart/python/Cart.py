from __future__ import print_function
from concurrent import futures
import logging

import grpc
import Catalog_pb2
import Catalog_pb2_grpc
import Cart_pb2
import Cart_pb2_grpc
import settings

class Cart(Cart_pb2_grpc.CartServicer):

    products=[]
    products.append(settings.Product(1,1,5000,"Iphone"))
    products.append(settings.Product(2,2,10000,"Estuche"))

    def AddToCart(self, request, context):
        with grpc.insecure_channel('18.204.5.43:8080') as channel:
            stub = Catalog_pb2_grpc.CatalogStub(channel)
            response = stub.GetStock(Catalog_pb2.ProductId(productId=request.productId))
            if response.stock <= 0:
                return Cart_pb2.Response(status_code=0,message="No quedan items en la tienda")
            else:
                stub.DeleteQuantity(Catalog_pb2.Stock(productId=request.productId,stock=1))
                name = stub.GetName(Catalog_pb2.ProductId(productId=request.productId))
                price = stub.GetPrice(Catalog_pb2.ProductId(productId=request.productId))
                self.products.append(settings.Product(request.productId,1,price.price,name.name))
                return Cart_pb2.Response(status_code=1)
    def ViewProductInCart(self, request, context):
        producto= self.products[request.productId-1]
        return Cart_pb2.Response(message= 'El objeto en carrito %i. es %s y tiene %i agregado/s'%(producto.get_id_product(),producto.get_name(),producto.get_quantity()))
    def GetCarLength(self, request, context):
        return Cart_pb2.Length(length= len(self.products))
    def GetPrecio(self, request, context):
        product = self.products[request.pedidoId-1]
        total = (product.get_individual_price())*(product.get_quantity())
        return Cart_pb2.Precio(precio=total)
    def RemoveFromCart(self, request, context):
        product_to_delete = self.products[request.productId-1]
        product_to_delete.set_id_product(0)
        product_to_delete.set_quantity(0)
        product_to_delete.set_price(0)
        product_to_delete.set_name("")
        return Cart_pb2.Response(status_code=1)
    def ViewCart(self, request, context):
        carrito = "Los objetos en el carrito son: \n"
        for i in self.products:
            carrito +=  i.get_name()+" y tiene agregado "+ str(i.get_quantity())+" \n"
        return Cart_pb2.Response(message=carrito)

def serve():
    port = '8080'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Cart_pb2_grpc.add_CartServicer_to_server(Cart(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
