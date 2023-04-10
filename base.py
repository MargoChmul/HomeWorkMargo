
from pprint import pprint
from mysql.connector import cursor
import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "user2064", password = "!QA2ws3ed")
cursor = mydb.cursor()
query = "select name, surname, age from db2064.test ORDER BY surname, name"
cursor.execute(query)
result = cursor.fetchall()
cursor.close()
pprint(result)