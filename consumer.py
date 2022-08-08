from kafka import KafkaConsumer
import json 
import time

consumer = KafkaConsumer(
    'jobs',
     bootstrap_servers=['127.0.0.1:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    jobs = message.value
    time.sleep(5)
    print('{} added'.format(jobs))
