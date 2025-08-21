calculator_pb2.py: calculator.proto
	protoc --proto_path=. --python_out=. calculator.proto

calculator_pb2_connect.py: calculator.proto
	protoc --proto_path=. --plugin=protoc-gen-connect-python=.venv/bin/protoc-gen-connect_python --connect-python_out=. calculator.proto