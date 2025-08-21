# Generated Connect client code

from __future__ import annotations
from collections.abc import AsyncIterator
from collections.abc import Iterator
from collections.abc import Iterable
import aiohttp
import urllib3
import typing
import sys

from connectrpc.client_async import AsyncConnectClient
from connectrpc.client_sync import ConnectClient
from connectrpc.client_protocol import ConnectProtocol
from connectrpc.client_connect import ConnectProtocolError
from connectrpc.headers import HeaderInput
from connectrpc.server import ClientRequest
from connectrpc.server import ClientStream
from connectrpc.server import ServerResponse
from connectrpc.server import ServerStream
from connectrpc.server_sync import ConnectWSGI
from connectrpc.streams import StreamInput
from connectrpc.streams import AsyncStreamOutput
from connectrpc.streams import StreamOutput
from connectrpc.unary import UnaryOutput
from connectrpc.unary import ClientStreamingOutput

if typing.TYPE_CHECKING:
    # wsgiref.types was added in Python 3.11.
    if sys.version_info >= (3, 11):
        from wsgiref.types import WSGIApplication
    else:
        from _typeshed.wsgi import WSGIApplication

import calculator_pb2

class CalculatorServiceClient:
    def __init__(
        self,
        base_url: str,
        http_client: urllib3.PoolManager | None = None,
        protocol: ConnectProtocol = ConnectProtocol.CONNECT_PROTOBUF,
    ):
        self.base_url = base_url
        self._connect_client = ConnectClient(http_client, protocol)
    def call_calculate(
        self, req: calculator_pb2.CalculateRequest,extra_headers: HeaderInput | None=None, timeout_seconds: float | None=None
    ) -> UnaryOutput[calculator_pb2.CalculateResponse]:
        """Low-level method to call Calculate, granting access to errors and metadata"""
        url = self.base_url + "/calculator.CalculatorService/Calculate"
        return self._connect_client.call_unary(url, req, calculator_pb2.CalculateResponse,extra_headers, timeout_seconds)


    def calculate(
        self, req: calculator_pb2.CalculateRequest,extra_headers: HeaderInput | None=None, timeout_seconds: float | None=None
    ) -> calculator_pb2.CalculateResponse:
        response = self.call_calculate(req, extra_headers, timeout_seconds)
        err = response.error()
        if err is not None:
            raise err
        msg = response.message()
        if msg is None:
            raise ConnectProtocolError('missing response message')
        return msg


class AsyncCalculatorServiceClient:
    def __init__(
        self,
        base_url: str,
        http_client: aiohttp.ClientSession,
        protocol: ConnectProtocol = ConnectProtocol.CONNECT_PROTOBUF,
    ):
        self.base_url = base_url
        self._connect_client = AsyncConnectClient(http_client, protocol)

    async def call_calculate(
        self, req: calculator_pb2.CalculateRequest,extra_headers: HeaderInput | None=None, timeout_seconds: float | None=None
    ) -> UnaryOutput[calculator_pb2.CalculateResponse]:
        """Low-level method to call Calculate, granting access to errors and metadata"""
        url = self.base_url + "/calculator.CalculatorService/Calculate"
        return await self._connect_client.call_unary(url, req, calculator_pb2.CalculateResponse,extra_headers, timeout_seconds)

    async def calculate(
        self, req: calculator_pb2.CalculateRequest,extra_headers: HeaderInput | None=None, timeout_seconds: float | None=None
    ) -> calculator_pb2.CalculateResponse:
        response = await self.call_calculate(req, extra_headers, timeout_seconds)
        err = response.error()
        if err is not None:
            raise err
        msg = response.message()
        if msg is None:
            raise ConnectProtocolError('missing response message')
        return msg


@typing.runtime_checkable
class CalculatorServiceProtocol(typing.Protocol):
    def calculate(self, req: ClientRequest[calculator_pb2.CalculateRequest]) -> ServerResponse[calculator_pb2.CalculateResponse]:
        ...

CALCULATOR_SERVICE_PATH_PREFIX = "/calculator.CalculatorService"

def wsgi_calculator_service(implementation: CalculatorServiceProtocol) -> WSGIApplication:
    app = ConnectWSGI()
    app.register_unary_rpc("/calculator.CalculatorService/Calculate", implementation.calculate, calculator_pb2.CalculateRequest)
    return app
