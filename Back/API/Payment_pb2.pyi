from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ItemId(_message.Message):
    __slots__ = ["pedidoId"]
    PEDIDOID_FIELD_NUMBER: _ClassVar[int]
    pedidoId: int
    def __init__(self, pedidoId: _Optional[int] = ...) -> None: ...

class Nones(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Respuesta(_message.Message):
    __slots__ = ["message", "status_code"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    message: str
    status_code: int
    def __init__(self, status_code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
