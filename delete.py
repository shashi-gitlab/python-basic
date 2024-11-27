import mysql.connector
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

db = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='pythonexample'
)

cursor = db.cursor()
# print(cursor)
# this is an object created from database to perform query execution


query = ("delete from userinfo where id=4")

cursor.execute(query)
db.commit()
cursor.close()
db.close()