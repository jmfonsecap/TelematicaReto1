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
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import Catalog_pb2
import Catalog_pb2_grpc
import settings

class Catalog(Catalog_pb2_grpc.CatalogServicer):

    products =[]
    products.append(settings.Product(1,20,"Juan"))
    products.append(settings.Product(2,10,"Carlos"))
    
    def SeeProduct(self, request, context):
        return Catalog_pb2.TransactionResponse(message='El producto buscado es, %i.%s y hay %i en stock' %(self.products[request.productId-1].get_id_product(),self.products[request.productId-1].get_name(),self.products[request.productId-1].get_stock()) )
    def AddProduct(self, request, context):
        product_to_add = settings.Product(len(self.products)+1, request.stock, request.name)
        self.products.append(product_to_add)
        return Catalog_pb2.TransactionResponse(status_code=1)
    def DeleteProduct(self, request, context):
        product_to_delete = self.products[request.productId-1]
        product_to_delete.set_id_product(0)
        product_to_delete.set_stock(0)
        product_to_delete.set_name("")
        return Catalog_pb2.TransactionResponse(status_code=1)
    def GetStock(self, request, context):
        return Catalog_pb2.Stock(stock=self.products[request.productId-1].get_stock())
    def AddQuantity(self, request, context):
        self.products[request.productId-1].set_stock(self.products[request.productId-1].get_stock()+request.stock)
        return Catalog_pb2.TransactionResponse(status_code=1)
    def DeleteQuantity(self, request, context):
        self.products[request.productId-1].set_stock(self.products[request.productId-1].get_stock()-request.stock)
        return Catalog_pb2.TransactionResponse(status_code=1)
def serve():
    port = '8080'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Catalog_pb2_grpc.add_CatalogServicer_to_server(Catalog(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
