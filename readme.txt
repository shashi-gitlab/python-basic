82% of storage used … If you run out, you can't create, edit, and upload files. Get 30 GB of storage for ₹59.00 ₹0 for 1 month.
1) recoring session
recording part on google drive

2) 2 to 3 topics

https://www.python.org/downloads/

12/10
---------------
C:\Users\Cloudesign\AppData\Local\Programs\Python\Python311

python --version

https://code.visualstudio.com/download

variables
printing in python
math operations
solve : 
3 examples

To run Python: 
In Terminal: 
python 1.py

https://www.hdfc.com/home-loan-emi-calculator

19/10/2024:


String
Fstring , format()
Data type
List
---------------------------------------
Tuple -- 26/10
Module -- 26/10
---------------------------------------
Set - 9/11
Dictionary
---------------------------------------
Function
pip --version
third party module


23/11
---------------
database - crud



email
excel
doc
pdf

   

List - 1 or more values - changable [] - duplicate - 0
Tuple - 1 or more values - unchangable ()- duplicate - 0
set - 1 or more values - partially changable - no duplicate - not in ordered format (add,remove,fetch,replace-no , update)

for in loop

List [] - many data having same data type - changable - duplicate - index
tuple () - many data having same data type- unchangable - duplicate- index
set {}- many data having same data type- p changable - unique - no index
Dictionary {key:value}- many data having unsimilar data type- changable - unique keys- keys

for in loop


16-11
-----
python function
third party module - sms 

https://www.apachefriends.org/download.html

apache,mysql -- start


visit browser and perform:
http://localhost/dashboard/

use mysql using phpyadmin tool
http://localhost/phpmyadmin/


3 types of database

1) unstructured database
    files and folder

2) structured database
    excel-- n*worksheet ==> records (in column format)
    mysql-- n*tables ==> records (in column format)

3 ) semi-structured database
    mongodb --
    cassandra --


http://localhost/phpmyadmin/

    USE SQL TAB

    1) create database pythonexample (excel)

    2) create table users(
        name varchar(100) ,
        age int
    );

    create table products(
        name varchar(100) ,
        price numeric,
        discount int
    );

    create table userinfo(
        name varchar(100) ,
        salary numeric,
        id int auto_increment primary key
    );

    insert into userinfo 
    values 
    ('rohan',10000,''),
    ('roshan',12000,''),
    ('ankit',15000,''),
    ('ameya',16000,'');


    delete from userinfo;

    update userinfo set
    name='rohan naik',salary=30000
    where id=5;

    select name,salary,id from userinfo
    select * from userinfo


    create table userinfo(
        name varchar(100) ,
        salary numeric,
        id int auto_increment primary key
    ) auto_increment=1000;