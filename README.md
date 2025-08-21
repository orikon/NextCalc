[![CI Status](https://github.com/orikon/NextCalc/actions/workflows/build.yml/badge.svg)](https://github.com/orikon/NextCalc/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub Created At](https://img.shields.io/github/created-at/orikon/NextCalc)


基于 Next.js 和 Tailwind CSS 和 Connect-Python 的计算器应用
=============================

> 这是一个简单的全栈计算器应用，它使用 Next.js 和 Tailwind CSS 作为前端，Python 作为后端，并通过 Connect Protocol 进行通信。前端通过 connect-web 客户端向后端发送计算请求，后端则使用 connect-python 处理这些请求并返回结果。

## 特性
* 基本算术运算: 支持加、减、乘、除四种基本运算。
* 响应式界面: 使用 Tailwind CSS 构建，可在不同设备上良好显示。
* 客户端-服务器通信: 演示了如何使用 Connect Protocol 实现 Web 客户端与 Python 后端之间的 RPC (Remote Procedure Call) 通信。

## 先决条件

在开始之前，请确保你的系统中已安装以下软件：

* Node.js 20.0+ / npm 10.8+
* Python 3.10+
* UV: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)
* Connect RPC / connect-python: [https://github.com/connectrpc/connect-python](https://github.com/connectrpc/connect-python)
* Buf: [https://buf.build/docs/cli/installation/](https://buf.build/docs/cli/installation/)

## 快速开始
请按照以下步骤启动项目。

### 1. 克隆代码库
首先，使用 git 命令将项目克隆到你的本地计算机：

``` sh
git clone https://github.com/orikon/NextCalc.git
cd NextCalc
```

### 2. 设置 Python 后端
在终端中，进入你的项目目录并执行以下命令：

#### 安装依赖:

首先，使用 uv 安装 connect-python 和其他必要的库：

```
cd backend
uv sync
```

#### 运行服务器:

启动 Python 服务器。服务器将监听 8000 端口。
```sh
cd backend 
uv run main.py
```
如果你看到 "Serving on http://127.0.0.1:8000" 的消息，说明服务器已成功启动并正在运行。

### 3. 设置 Next.js 前端
打开一个新的终端窗口，进入你的项目目录，并执行以下命令：

#### 安装依赖:

安装所有前端依赖，包括 @connectrpc/connect、@connectrpc/connect-web 和 tailwindcss：
```sh
cd frontend 
npm install
```
#### 运行应用:

启动 Next.js 开发服务器：
```sh
cd frontend
npm run dev
```

浏览器将自动打开一个新标签页，访问 http://localhost:3000，你就可以开始使用计算器了！

## 编译部分
```sh
# buf.gen.yaml
# https://buf.build/docs/cli/installation/

BIN="/usr/local/bin" && \
VERSION="1.56.0" && \
sudo curl -sSL \
"https://github.com/bufbuild/buf/releases/download/v${VERSION}/buf-$(uname -s)-$(uname -m)" \
-o "${BIN}/buf" && \
sudo chmod +x "${BIN}/buf"

buf format
buf generate
```

## 单元测试

```sh
cd frontend
npm test

cd backend
uv run python -m unittest tests.test_calculator
```


## 联系我们
如果你有任何问题或建议，欢迎提交 Issue。