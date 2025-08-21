// 必须在 import 之前
jest.mock('@connectrpc/connect-web', () => ({
    createConnectTransport: jest.fn(() => ({})),
}));
  
const mockCalculate = jest.fn();
jest.mock('@connectrpc/connect', () => ({
createClient: jest.fn(() => ({
    calculate: jest.fn(),
})),
}));
  
jest.mock('../app/gen/calculator_pb', () => ({
    CalculatorService: {},
}));
  
// beforeEach 只处理 mockCalculate
beforeEach(() => {
    mockCalculate.mockClear();
    mockCalculate.mockResolvedValue({
        result: 8,
        error: undefined,
    });
});

import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import Home from '../app/page';
  


  
describe('Calculator App Frontend', () => {
  
    test('所有数字按钮的点击都能在显示屏上正确显示', () => {
      render(<Home />);
      const display = screen.getByTestId('display');
      fireEvent.click(screen.getByText('7'));
      expect(display).toHaveTextContent('7');
      fireEvent.click(screen.getByText('8'));
      expect(display).toHaveTextContent('78');
      fireEvent.click(screen.getByText('.'));
      expect(display).toHaveTextContent('78.');
      fireEvent.click(screen.getByText('9'));
      expect(display).toHaveTextContent('78.9');
    });
  
    test('清零按钮 (C) 应该重置显示屏和状态', () => {
      render(<Home />);
      const display = screen.getByTestId('display');
        
      fireEvent.click(screen.getByText('1'));
      fireEvent.click(screen.getByText('2'));
      fireEvent.click(screen.getByText('+'));
      fireEvent.click(screen.getByText('3'));
      fireEvent.click(screen.getByText('C'));
        
      expect(display).toHaveTextContent('0');
    });
  
    test('回退按钮 (<) 应该删除最后一个字符', () => {
      render(<Home />);
      fireEvent.click(screen.getByText('1'));
      fireEvent.click(screen.getByText('2'));
      fireEvent.click(screen.getByText('3'));
      const display = screen.getByTestId('display');
      expect(display).toBeInTheDocument();
      fireEvent.click(screen.getByText('<'));
      expect(screen.getByText('12')).toBeInTheDocument();
    });
  
    // test('基本的加法运算应该能正常工作并更新显示屏', async () => {
    //   render(<Home />);
    //   fireEvent.click(screen.getByText('5'));
    //   fireEvent.click(screen.getByText('+'));
    //   fireEvent.click(screen.getByText('3'));
    //   fireEvent.click(screen.getByText('='));
    //   // mockCalculate 被调用并返回8
    //   const result = await screen.findByText('8');
    //   expect(result).toBeInTheDocument();
    // });
  
});