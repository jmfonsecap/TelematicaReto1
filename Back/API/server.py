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
@post('/cart/Add')
def Add():
    body = request.json
    with grpc.insecure_channel('3.84.222.54:8080') as channel:
            stub = Cart_pb2_grpc.CartStub(channel)
            stub.AddToCart(Cart_pb2.Pedido(productId=int(body["productId"])))

@post('/cart/Remove')
def Remove():
    body = request.json
    with grpc.insecure_channel('3.84.222.54:8080') as channel:
            stub = Cart_pb2_grpc.CartStub(channel)
            stub.RemoveFromCart(Cart_pb2.PedidoId(pedidoId=int(body["pedidoId"])))

@route('/cart/')
def Remove():
    body = request.json
    with grpc.insecure_channel('3.84.222.54:8080') as channel:
            stub = Cart_pb2_grpc.CartStub(channel)
            response = stub.ViewCart(Cart_pb2.Nada())
    return response.message
@post('/cart/AddQuantity')
def AddQuantity():
    body = request.json
    with grpc.insecure_channel('3.84.222.54:8080') as channel:
            stub = Cart_pb2_grpc.CartStub(channel)
            stub.AddQuantity(Cart_pb2.PedidoId(pedidoId=int(body["pedidoId"])))
  
#Catalog
@route('/catalog/ViewProduct')
def ViewProduct():
    body = request.json
    with grpc.insecure_channel('100.26.18.159:8080') as channel:
            stub = Catalog_pb2_grpc.CatalogStub(channel)
            response = stub.SeeProduct(Catalog_pb2.Product(productId=int(body["productId"])))
    return response.message
@post('/catalog/Add')   
def AddProduct():
    body = request.json
    with grpc.insecure_channel('100.26.18.159:8080') as channel:
            stub = Catalog_pb2_grpc.CatalogStub(channel)
            stub.AddProduct(Catalog_pb2.Product(nombre= body["name"],stock=int(body["stock"])))
@post('/catalog/Delete')
def DeleteProduct():
    body = request.json
    with grpc.insecure_channel('100.26.18.159:8080') as channel:
            stub = Catalog_pb2_grpc.CatalogStub(channel)
            stub.DeleteProduct(Catalog_pb2.ProductId(productId=int(body["productId"])))
@route('/catalog/Stock')
def GetStock():
    body = request.json
    with grpc.insecure_channel('100.26.18.159:8080') as channel:
            stub = Catalog_pb2_grpc.CatalogStub(channel)
            response =stub.GetStock(Catalog_pb2.ProductId(productId=int(body["productId"])))
            
    return str(response.stock)
@route('/catalog/Price')
def GetPrice():
    body = request.json
    with grpc.insecure_channel('100.26.18.159:8080') as channel:
            stub = Catalog_pb2_grpc.CatalogStub(channel)
            response =stub.GetPrice(Catalog_pb2.ProductId(productId=int(body["productId"])))
            
    return str(response.price)
@route('/catalog/name')
def GetName():
    body = request.json
    with grpc.insecure_channel('100.26.18.159:8080') as channel:
            stub = Catalog_pb2_grpc.CatalogStub(channel)
            response =stub.GetName(Catalog_pb2.ProductId(productId=int(body["productId"])))
            
    return response.name
@post('/catalog/AddQuantity')
def AddQuantity():
    body = request.json
    with grpc.insecure_channel('100.26.18.159:8080') as channel:
            stub = Catalog_pb2_grpc.CatalogStub(channel)
            response =stub.AddQuantity(Catalog_pb2.Stock(stock=int(body["stock"]),productId=int(body["productId"])))
@post('/catalog/DeleteQuantity')
def DeleteQuantity():
    body = request.json
    with grpc.insecure_channel('100.26.18.159:8080') as channel:
            stub = Catalog_pb2_grpc.CatalogStub(channel)
            response =stub.DeleteQuantity(Catalog_pb2.Stock(stock=int(body["stock"]),productId=int(body["productId"])))

#Payment
@route('/payment/PayAll')
def PayAll():
    body = request.json
    with grpc.insecure_channel('34.207.120.145:8080') as channel:
            stub = Payment_pb2_grpc.PaymentStub(channel)
            response = stub.PagarTodoCarro(Payment_pb2.Nones())
    return response.message
@route('/payment/Pay')
def Pay():
    body = request.json
    with grpc.insecure_channel('34.207.120.145:8080') as channel:
            stub = Payment_pb2_grpc.PaymentStub(channel)
            response = stub.PagarItemEnElCarro(Payment_pb2.ItemId(itemId=int(body["itemId"]) ))
    return response.message

      
    

run(host= 'localhost',port= 8080, debug=True)