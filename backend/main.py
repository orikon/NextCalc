import typing
from connectrpc.server import ClientRequest, ServerResponse

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "gen")) # buf generate files can not modify

import calculator_pb2
from calculator_pb2_connect import CalculatorServiceProtocol, wsgi_calculator_service

class CalculatorService(CalculatorServiceProtocol):
    def calculate(self, req: ClientRequest[calculator_pb2.CalculateRequest]) -> ServerResponse[calculator_pb2.CalculateResponse]:
        try:
            if req.msg.expression == "":
                raise ValueError("Null expression")
            parts = req.msg.expression.split()
            if len(parts) != 3:
                raise ValueError("Invalid expression format. Expected 'operand operator operand'.")
            operand1 = float(parts[0])
            op = parts[1]
            operand2 = float(parts[2])
            if op == "+":
                result = operand1 + operand2
            elif op == "-":
                result = operand1 - operand2
            elif op == "*":
                result = operand1 * operand2
            elif op == "/":
                result = operand1 / operand2
            else:
                raise ValueError(f"Unsupported operator: {op}")
            return ServerResponse(calculator_pb2.CalculateResponse(result=result))
        except (ValueError, ZeroDivisionError) as e:
            return ServerResponse(calculator_pb2.CalculateResponse(error=str(e)))
        except Exception:
            return ServerResponse(calculator_pb2.CalculateResponse(error="An unexpected error occurred."))

def cors_middleware(app):
    # WSGI CORS middleware
    def middleware(environ, start_response):
        def custom_start_response(status, headers, exc_info=None):
            headers.append(('Access-Control-Allow-Origin', '*'))
            headers.append(('Access-Control-Allow-Methods', 'GET, POST, OPTIONS'))
            headers.append(('Access-Control-Allow-Headers', 'Content-Type, Connect-Protocol-Version'))
            return start_response(status, headers, exc_info)
        # 处理预检请求
        if environ['REQUEST_METHOD'] == 'OPTIONS':
            custom_start_response('200 OK', [])
            return [b'']
        return app(environ, custom_start_response)
    return middleware

# 构造 WSGI 应用并加上 CORS 中间件
app = wsgi_calculator_service(CalculatorService())
app = cors_middleware(app)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    print("Serving on http://127.0.0.1:8000")
    with make_server("127.0.0.1", 8000, app) as httpd:
        httpd.serve_forever()