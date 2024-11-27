import mysql.connector
'''
    in phpmyadmin tool
    check mysql database,
    check user table
    having following values

    user='root',
    password='',
    host='localhost',
'''

db = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='pythonexample'
)

print(db)

db.close()