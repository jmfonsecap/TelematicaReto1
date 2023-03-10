from concurrent import futures
import logging

import grpc
import Catalog_pb2
import Catalog_pb2_grpc
import settings

class Catalog(Catalog_pb2_grpc.CatalogServicer):

    products =[]
    products.append(settings.Product(1,20,5000,"Iphone"))
    products.append(settings.Product(2,10,100,"Estuche"))
    products.append(settings.Product(3,1,10000,"Xbox"))
    
    def SeeProduct(self, request, context):
        return Catalog_pb2.TransactionResponse(message='El producto buscado es, %i.%s y hay %i en stock' %(self.products[request.productId-1].get_id_product(),self.products[request.productId-1].get_name(),self.products[request.productId-1].get_stock()) )
    def AddProduct(self, request, context):
        product_to_add = settings.Product(len(self.products)+1, request.stock,request.price, request.nombre)
        self.products.append(product_to_add)
        return Catalog_pb2.TransactionResponse(status_code=1)
    def DeleteProduct(self, request, context):
        product_to_delete = self.products[request.productId-1]
        product_to_delete.set_id_product(0)
        product_to_delete.set_stock(0)
        product_to_delete.set_price(0)
        product_to_delete.set_name("")
        return Catalog_pb2.TransactionResponse(status_code=1)
    def GetStock(self, request, context):
        return Catalog_pb2.Stock(stock=self.products[request.productId-1].get_stock())
    def GetName(self, request, context):
        return Catalog_pb2.ProductName(name=self.products[request.productId-1].get_name())
    def AddQuantity(self, request, context):
        self.products[request.productId-1].set_stock(self.products[request.productId-1].get_stock()+request.stock)
        return Catalog_pb2.TransactionResponse(status_code=1)
    def DeleteQuantity(self, request, context):
        self.products[request.productId-1].set_stock(self.products[request.productId-1].get_stock()-request.stock)
        return Catalog_pb2.TransactionResponse(status_code=1)
    def GetPrice(self, request, context):
        return Catalog_pb2.Price(price=self.products[request.productId-1].get_price())

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
