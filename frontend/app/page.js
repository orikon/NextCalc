"use client"; // 这告诉 Next.js 这是一个客户端组件

import { useState } from 'react';
import { createConnectTransport } from "@connectrpc/connect-web";
import { createClient } from "@connectrpc/connect";
import { CalculatorService } from './gen/calculator_pb';


const transport = createConnectTransport({
  baseUrl: "http://localhost:8000",
});
const client = createClient(CalculatorService, transport);


export default function Home() {
  const [displayValue, setDisplayValue] = useState('0');
  const [operator, setOperator] = useState(null);
  const [firstOperand, setFirstOperand] = useState(null);
  const [waitingForSecondOperand, setWaitingForSecondOperand] = useState(false);

  // 处理数字和小数点输入
  const handleDigit = (digit) => {
    if (waitingForSecondOperand) {
      setDisplayValue(String(digit));
      setWaitingForSecondOperand(false);
    } else {
      setDisplayValue(displayValue === '0' ? String(digit) : displayValue + digit);
    }
  };

  // 处理运算符
  const handleOperator = (nextOperator) => {
    const inputValue = parseFloat(displayValue);

    if (operator && waitingForSecondOperand) {
      setOperator(nextOperator);
      return;
    }


    if (firstOperand === null) {
      setFirstOperand(inputValue);
    } else if (operator) {
      const expression = `${firstOperand} ${operator} ${inputValue}`;
      console.log(expression);

      // 发送请求给后端
      client.calculate({ expression: expression })
      .then(res => {
        // 根据后端响应更新显示值
        if (res.error) {
          setDisplayValue('Error' + String(res.result));
        } else {
          setDisplayValue(String(res.result));
        }
        setFirstOperand(res.result);
        setWaitingForSecondOperand(true);
      })
      .catch(error => {
        console.error('RPC Error:', error);
        setDisplayValue('Error');
      });
    }

    setWaitingForSecondOperand(true);
    setOperator(nextOperator);
  };

  // 处理清零
  const handleClear = () => {
    setDisplayValue('0');
    setFirstOperand(null);
    setOperator(null);
    setWaitingForSecondOperand(false);
  };

  // 处理退位
  const handleBackspace = () => {
    setDisplayValue(displayValue.slice(0, -1) || '0');
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 class="mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl"><span class="text-transparent bg-clip-text bg-gradient-to-r to-emerald-600 from-sky-400">Next Calc</span></h1>
      <div className="bg-white border rounded-lg shadow-lg overflow-hidden w-96 max-w-full">
        {/* 显示屏 */}
        <div className="bg-gray-800 text-white p-4 text-right">
          <div data-testid="display" className="text-3xl font-light h-10">{displayValue}</div>
        </div>
        
        {/* 按钮面板 */}
        <div className="grid grid-cols-4 gap-1 p-2">
          {/* 按钮绑定了点击事件 */}
          <button onClick={handleClear} className="col-span-2 text-xl bg-gray-200 hover:bg-gray-300 p-4 rounded-md">C</button>
          <button onClick={handleBackspace} className="text-xl bg-gray-200 hover:bg-gray-300 p-4 rounded-md">&lt;</button>
          <button onClick={() => handleOperator('/')} className="text-xl bg-gray-200 hover:bg-gray-300 p-4 rounded-md">/</button>

          <button onClick={() => handleDigit(7)} className="text-xl bg-white hover:bg-gray-100 p-4 rounded-md">7</button>
          <button onClick={() => handleDigit(8)} className="text-xl bg-white hover:bg-gray-100 p-4 rounded-md">8</button>
          <button onClick={() => handleDigit(9)} className="text-xl bg-white hover:bg-gray-100 p-4 rounded-md">9</button>
          <button onClick={() => handleOperator('*')} className="text-xl bg-gray-200 hover:bg-gray-300 p-4 rounded-md">*</button>
          
          <button onClick={() => handleDigit(4)} className="text-xl bg-white hover:bg-gray-100 p-4 rounded-md">4</button>
          <button onClick={() => handleDigit(5)} className="text-xl bg-white hover:bg-gray-100 p-4 rounded-md">5</button>
          <button onClick={() => handleDigit(6)} className="text-xl bg-white hover:bg-gray-100 p-4 rounded-md">6</button>
          <button onClick={() => handleOperator('-')} className="text-xl bg-gray-200 hover:bg-gray-300 p-4 rounded-md">-</button>
          
          <button onClick={() => handleDigit(1)} className="text-xl bg-white hover:bg-gray-100 p-4 rounded-md">1</button>
          <button onClick={() => handleDigit(2)} className="text-xl bg-white hover:bg-gray-100 p-4 rounded-md">2</button>
          <button onClick={() => handleDigit(3)} className="text-xl bg-white hover:bg-gray-100 p-4 rounded-md">3</button>
          <button onClick={() => handleOperator('+')} className="text-xl bg-gray-200 hover:bg-gray-300 p-4 rounded-md">+</button>
          
          <button onClick={() => handleDigit(0)} className="col-span-2 text-xl bg-white hover:bg-gray-100 p-4 rounded-md">0</button>
          <button onClick={() => handleDigit('.')} className="text-xl bg-white hover:bg-gray-100 p-4 rounded-md">.</button>
          <button onClick={() => handleOperator('=')} className="text-xl bg-blue-500 text-white hover:bg-blue-600 p-4 rounded-md">=</button>
        </div>
      </div>
      <span class="block text-sm text-gray-500 sm:text-center dark:text-gray-400 m-6">© 2025 Simon. All Rights Reserved.</span>
    </div>
  );
}