import mysql.connector

database =  mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)

# prepare cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS topbohemia")

print("database created!")