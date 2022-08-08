import os
from datetime import datetime
import time
import threading
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError

from kafka import KafkaProducer
import logging
from json import dumps, loads
import csv
logging.basicConfig(level=logging.INFO)


producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092', value_serializer=lambda K:dumps(K).encode('utf-8'))

with open('job_postings.csv', 'r') as file:
  reader = csv.reader(file, delimiter = '\t')
  for messages in reader:
    producer.send('jobs', messages)
    producer.flush()
    time.sleep(5)