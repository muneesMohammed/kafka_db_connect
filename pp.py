from kafka import KafkaProducer
# import random
# from time import sleep
# # Output = input("Enter the data to be send:")

# print(Output)
topic = "TempMonitoring"
server = "localhost:9092"

for i in range(10, 40):
     output = random.randrange(40)
     sleep(10)
   

producer = KafkaProducer(bootstrap_servers = [server])

message = producer.send(topic, bytes(output, encoding='utf-8'))

metadata = message.get()

print(metadata.topic)

print(metadata.partition)