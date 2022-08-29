import sys
from kafka import KafkaConsumer
import mysql.connector


serverName ="localhost"
db_username = "root"
db_password =""
db_name ="iot_db"


connection = mysql.connector.connect(
  host=serverName,
  user=db_username,
  password=db_password,
  database=db_name
)
myCursor=connection.cursor()



topic = "TempMonitoring"

server = "localhost:9092"
consumer=KafkaConsumer(topic,bootstrap_servers=server,auto_offset_reset = 'earliest')
try:
    for message in consumer:
        data=message.value
        data_val=data.decode()
        partition=message.partition
        myCursor.execute("INSERT INTO `temperature`(`tempertaure`) VALUES ("+data_val+") ")
        connection.commit()
        print(partition)
except KeyboardInterrupt:
    sys.exit()







