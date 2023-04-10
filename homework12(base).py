from pprint import pprint
from mysql.connector import cursor
import json
import mysql.connector
from day8home import Textdata

mydb = mysql.connector.connect(
    host='localhost', user='user2064', password='!QA2ws3ed')
cursor = mydb.cursor()
query = "select income, month, year from db2064.homework12 order by year ;"
cursor.execute(query)
result = cursor.fetchall()
print(result)
cursor.close()
mydb.close()


    
t = Textdata().importData(result).createresult()


pprint(t.map)