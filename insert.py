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

insert_object = {
  'name': 'Amit C',
  'age': 5000
}

add_age = ("INSERT INTO userinfo "
              "(name, age) "
              "VALUES (%(name)s, %(age)s)")

cursor.execute(add_age, insert_object)
db.commit()
cursor.close()
db.close()