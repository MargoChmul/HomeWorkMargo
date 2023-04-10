from pprint import pprint
import random
from mysql.connector import cursor
import json
import mysql.connector


mydb = mysql.connector.connect(
    host='localhost', user='user2064', password='!QA2ws3ed')
cursor = mydb.cursor()
query = "insert into db2064.myrecords (summa) values "

list = []
i = 0
while i < 1000212:
    i+=1
    x = random.randint(1, 100)
    query += f"({x})"
    cursor.execute(query)
    mydb.commit()
    query = "insert into db2064.myrecords (summa) values "
    
cursor.close()
mydb.close()