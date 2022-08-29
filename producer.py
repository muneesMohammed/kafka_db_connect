from kafka import KafkaProducer

topic = "TempMonitoring"
server = "localhost:9092"
import datetime
from time import sleep
import random
while True:
    period = datetime.datetime.now()
    if((period.second % 5) == 0):
        temp = random.randrange(10, 40, 3)
        print(temp)
        producer = KafkaProducer(bootstrap_servers = [server])
        message = producer.send(topic, bytes(str(temp), encoding='utf-8'))
        metadata = message.get()
        print(metadata.topic)
        print(metadata.partition)
        sleep(1)