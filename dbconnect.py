
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

temp_value=str(input("enter temp value"))
print(temp_value)

myCursor.execute("INSERT INTO `temperature`(`tempertaure`) VALUES (%s)" ,(temp_value,) )
connection.commit()
print("data inserted successfully")