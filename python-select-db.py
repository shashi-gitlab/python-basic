import mysql.connector
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

db = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='pythonexample'
)

cursor = db.cursor()
query = ("SELECT id,name,age FROM userInfo")
cursor.execute(query)
for (id, name, age) in cursor:
    print(id,name,age)

for (value) in cursor:
    print(value)

cursor.close()
db.close()