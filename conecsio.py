import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="pass",
  port="port",
  database="database"
)


mycursor = mydb.cursor()
