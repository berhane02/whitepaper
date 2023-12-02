#pip install mysql
#pip install mysql-connector

import mysql.connector

dataBase = mysql.connector.connect(
    host="127.0.0.1", 
    port="3306", 
    user="root", 
    password="admin123"
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE whitePaper")

print("all done!")


