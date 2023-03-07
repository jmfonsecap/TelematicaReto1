from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Nada(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Pedido(_message.Message):
    __slots__ = ["pedidoId", "productId"]
    PEDIDOID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    pedidoId: int
    productId: int
    def __init__(self, pedidoId: _Optional[int] = ..., productId: _Optional[int] = ...) -> None: ...

class PedidoId(_message.Message):
    __slots__ = ["pedidoId"]
    PEDIDOID_FIELD_NUMBER: _ClassVar[int]
    pedidoId: int
    def __init__(self, pedidoId: _Optional[int] = ...) -> None: ...

class ProductId(_message.Message):
    __slots__ = ["productId"]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    productId: int
    def __init__(self, productId: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["message", "status_code"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    message: str
    status_code: int
    def __init__(self, status_code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
