from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Price(_message.Message):
    __slots__ = ["price"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    price: int
    def __init__(self, price: _Optional[int] = ...) -> None: ...

class Product(_message.Message):
    __slots__ = ["nombre", "productId", "stock"]
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    nombre: str
    productId: int
    stock: int
    def __init__(self, productId: _Optional[int] = ..., nombre: _Optional[str] = ..., stock: _Optional[int] = ...) -> None: ...

class ProductId(_message.Message):
    __slots__ = ["productId"]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    productId: int
    def __init__(self, productId: _Optional[int] = ...) -> None: ...

class ProductName(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Stock(_message.Message):
    __slots__ = ["productId", "stock"]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    productId: int
    stock: int
    def __init__(self, stock: _Optional[int] = ..., productId: _Optional[int] = ...) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = ["message", "status_code"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    message: str
    status_code: int
    def __init__(self, status_code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
