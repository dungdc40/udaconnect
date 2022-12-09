import time
import os
from concurrent import futures
import json
from kafka import KafkaProducer

import grpc
import location_pb2
import location_pb2_grpc

from services import LocationService
from models import Location
from datetime import datetime


# Set up a Kafka producer
TOPIC_NAME = 'items'
KAFKA_SERVER = os.environ["KAFKA_SERVER"]
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, reconnect_backoff_max_ms=86400000, reconnect_backoff_ms=100)


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Get(self, request, context):
        location: Location = LocationService.retrieve(request.id)
        message = {
            "id":location.id,
            "person_id":location.person_id,
            "longitude":location.longitude,
            "latitude":location.latitude,
            "creation_time":location.creation_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        print(message)
        return location_pb2.LocationMessage(**message)

    def Create(self, request, context):
        message = {
            "id": request.id,
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }
        kafka_data = json.dumps(message).encode()
        producer.send("locations", kafka_data)
        producer.flush()
        return location_pb2.LocationMessage(**message)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
