from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CalculateRequest(_message.Message):
    __slots__ = ("expression",)
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    expression: str
    def __init__(self, expression: _Optional[str] = ...) -> None: ...

class CalculateResponse(_message.Message):
    __slots__ = ("result", "error")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result: float
    error: str
    def __init__(self, result: _Optional[float] = ..., error: _Optional[str] = ...) -> None: ...
