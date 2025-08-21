import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# 添加项目根目录到 sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import CalculatorService
from gen.calculator_pb2 import CalculateRequest, CalculateResponse

import asyncio
import aiohttp
from gen.calculator_pb2_connect import AsyncCalculatorServiceClient
from connectrpc.client_protocol import ConnectProtocol

class TestCalculatorService(unittest.TestCase):

    def setUp(self):
        self.url = "http://localhost:8000"
        self.service = CalculatorService()

    def test_calculate_addition_successful(self):
        """
        测试正常的加法运算。
        """
        async def run_test():
            async with aiohttp.ClientSession() as session:
                client = AsyncCalculatorServiceClient(
                    base_url=self.url,
                    http_client=session,
                    protocol=ConnectProtocol.CONNECT_PROTOBUF,
                )
                req = CalculateRequest(expression="5 + 3")
                resp = await client.calculate(req)
                                
                self.assertEqual(resp.result, float("8"))
                self.assertEqual(resp.error, "")

        asyncio.run(run_test())


    def test_say_subtraction_successful(self):
        """
        测试正常的减法运算。
        """
        async def run_test():
            async with aiohttp.ClientSession() as session:
                client = AsyncCalculatorServiceClient(
                    base_url=self.url,
                    http_client=session,
                    protocol=ConnectProtocol.CONNECT_PROTOBUF,
                )
                req = CalculateRequest(expression="10 - 2")
                resp = await client.calculate(req)
                                
                self.assertEqual(resp.result, float("8"))
                self.assertEqual(resp.error, "")

        asyncio.run(run_test())



    def test_say_multiplication_successful(self):
        """
        测试正常的乘法运算。
        """
        async def run_test():
            async with aiohttp.ClientSession() as session:
                client = AsyncCalculatorServiceClient(
                    base_url=self.url,
                    http_client=session,
                    protocol=ConnectProtocol.CONNECT_PROTOBUF,
                )
                req = CalculateRequest(expression="4 * 5")
                resp = await client.calculate(req)
                                
                self.assertEqual(resp.result, float("20"))
                self.assertEqual(resp.error, "")

        asyncio.run(run_test())

        
    def test_say_division_successful(self):
        """
        测试正常的除法运算。
        """
        async def run_test():
            async with aiohttp.ClientSession() as session:
                client = AsyncCalculatorServiceClient(
                    base_url=self.url,
                    http_client=session,
                    protocol=ConnectProtocol.CONNECT_PROTOBUF,
                )
                req = CalculateRequest(expression="10 / 2")
                resp = await client.calculate(req)
                                
                self.assertEqual(resp.result, float("5"))
                self.assertEqual(resp.error, "")

        asyncio.run(run_test())

    def test_say_division_by_zero_returns_error(self):
        """
        测试除以零的边缘情况，应返回错误信息。
        """
        async def run_test():
            async with aiohttp.ClientSession() as session:
                client = AsyncCalculatorServiceClient(
                    base_url=self.url,
                    http_client=session,
                    protocol=ConnectProtocol.CONNECT_PROTOBUF,
                )
                req = CalculateRequest(expression="10 / 0")
                resp = await client.calculate(req)

                self.assertEqual(resp.result, float("0"))
                self.assertEqual(resp.error, "float division by zero")

        asyncio.run(run_test())


    def test_say_invalid_expression_returns_error(self):
        """
        测试无效表达式的情况，应返回错误信息。
        """
        async def run_test():
            async with aiohttp.ClientSession() as session:
                client = AsyncCalculatorServiceClient(
                    base_url=self.url,
                    http_client=session,
                    protocol=ConnectProtocol.CONNECT_PROTOBUF,
                )
                req = CalculateRequest(expression="5 + hello")
                resp = await client.calculate(req)

                self.assertEqual(resp.result, float("0"))
                self.assertEqual(resp.error, "could not convert string to float: 'hello'")

        asyncio.run(run_test())
        
        
        
    # def test_say_empty_expression_returns_error(self):
    #     """
    #     测试空表达式的情况，应返回错误信息。
    #     """
    #     async def run_test():
    #         async with aiohttp.ClientSession() as session:
    #             client = AsyncCalculatorServiceClient(
    #                 base_url=self.url,
    #                 http_client=session,
    #                 protocol=ConnectProtocol.CONNECT_PROTOBUF,
    #             )
    #             req = CalculateRequest(expression="")
    #             resp = await client.calculate(req)

    #             print(resp.result, resp.error)

    #     asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main()
