# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

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
        return Catalog_pb2.TransactionResponse(status_code=1)
    def ViewCart(self, request, context):
        carrito = "Los objetos en el carrito son: \n"
        for i in self.products:
            carrito =  i.getName()+" y tiene agregado "+ str(i.getQuantity())+" \n"
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = Catalog_pb2_grpc.CatalogStub(channel)
        stub.AddProduct(Catalog_pb2.Product(name= "MyHeart",stock=2))
        response = stub.SeeProduct(Catalog_pb2.ProductId(productId=3))
        print("Greeter client received: " + response.message)
        stub.AddQuantity(Catalog_pb2.Stock(productId=3,stock=10))
        stub.DeleteQuantity(Catalog_pb2.Stock(productId=3,stock=5))
        response = stub.GetName(Catalog_pb2.ProductId(productId=3))
        print(response.name)
        stub.DeleteProduct(Catalog_pb2.ProductId(productId=3))
        response = stub.SeeProduct(Catalog_pb2.ProductId(productId=3))
        print("Greeter client received: " + response.message)

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
    #run()
