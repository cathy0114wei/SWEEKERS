from kafka import KafkaConsumer
from json import loads
import time

consumer = KafkaConsumer(
    'jobs',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    time.sleep(5)
    print('{} added'.format(message))