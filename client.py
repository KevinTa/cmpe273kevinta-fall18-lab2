from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        number = calculator_pb2.Number(value1=99, value2=88)
        response = stub.Add(number)
    print(str(response.value1) + ' + ' + str(response.value2) + " = " + str(response.result))


if __name__ == '__main__':
    run()