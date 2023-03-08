from bottle import route,run,request,post
import json
import grpc
import Catalog_pb2
import Catalog_pb2_grpc
import Cart_pb2
import Cart_pb2_grpc
import Payment_pb2
import Payment_pb2_grpc
@route('/')
def hello():
    return "Hello World"
#Cart
@route('/cart/ViewProduct')
def ViewProductInCart():
    body = request.json
    with grpc.insecure_channel('3.84.222.54:8080') as channel:
            stub = Cart_pb2_grpc.CartStub(channel)
            response =stub.ViewProductInCart(Cart_pb2.ProductoId(productId=int(body["productId"])))
    return response.message
#Catalog
@post('/catalog/Add')   
def AddProduct():
    body = request.json
    with grpc.insecure_channel('100.26.18.159:8080') as channel:
            stub = Catalog_pb2_grpc.CatalogStub(channel)
            stub.AddProduct(Catalog_pb2.Product(nombre= body["name"],stock=int(body["stock"])))
@route('/catalog/ViewProduct')
def ViewProduct():
    body = request.json
    with grpc.insecure_channel('100.26.18.159:8080') as channel:
            stub = Catalog_pb2_grpc.CatalogStub(channel)
            response = stub.SeeProduct(Catalog_pb2.Product(productId=int(body["productId"])))
    return response.message
      
    

run(host= 'localhost',port= 8080, debug=True)