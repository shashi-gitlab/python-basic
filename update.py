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

update_object = {
  'name': 'Chandan',
  'age': 38
}

add_age = ("update userinfo set name=%(name)s, age=%(age)s where id=2")

cursor.execute(add_age, update_object)
db.commit()
cursor.close()
db.close()