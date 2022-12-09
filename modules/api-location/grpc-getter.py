import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Getting sample payload...")

channel = grpc.insecure_channel("localhost:30002")
stub = location_pb2_grpc.LocationServiceStub(channel)

location = location_pb2.LocationMessage(
    id=2,
)

response = stub.Get(location)
print(response)
