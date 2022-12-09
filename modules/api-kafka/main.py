from kafka import KafkaConsumer
from services import LocationService
from models import Location
from json import loads
import os

TOPIC_NAME = 'locations'
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER, value_deserializer=lambda x: loads(x.decode('utf-8')), reconnect_backoff_max_ms=86400000)
for location in consumer:
    response: Location = LocationService.create(location.value)
    print (response)

