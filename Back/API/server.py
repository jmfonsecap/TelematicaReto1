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

@route('/cart/ViewProduct')
def ViewProductInCart():
    body = request.body.read()
    body = body.replace("+","").replace("payload=","")
    parsedBody = urllib.unquote(body).decode('utf8')
    jsonObj = json.loads(parsedBody)
    with grpc.insecure_channel('18.204.5.43:8080') as channel:
            stub = Cart_pb2_grpc.CartStub(channel)
            response =stub.ViewProductInCart(Cart_pb2.ProductoId(productId=jsonObj.productId))
    return response.message
    
    

run(host= 'localhost',port= 8080, debug=True)