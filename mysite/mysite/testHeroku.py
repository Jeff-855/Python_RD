# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 22:06:45 2021

@author: Jack
"""

import os
import psycopg2
print("url0:" )
DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a jefftestapp').read()[:-1]
print("url:" + DATABASE_URL + "urlend")
conn = psycopg2.connect('postgres://cgnhzkzooignln:9abdc56a2a5eb8577433249138fa2c0637e712bb976a5aeb0d01b9501084260b@ec2-34-239-33-57.compute-1.amazonaws.com:5432/d648rd7mjivgot')
print("conn ok")
cursor = conn.cursor()

print("conn ok1")

acctSQL = '''CREATE TABLE account(
           user_id serial PRIMARY KEY,
           username VARCHAR (50) UNIQUE NOT NULL,
           password VARCHAR (50) NOT NULL,
           email VARCHAR (355) UNIQUE NOT NULL,
           created_on TIMESTAMP NOT NULL,
           last_login TIMESTAMP
        );'''
    
acctSQL1 = '''insert into  account(user_id,username,password,email,created_on,last_login)
           values ('8','tes8','test1','yang3082@gmail.com','2021-06-26','2021-06-26')
        ;'''
        
acctSQL2 = '''insert into  blog_test(test_id,name,created_date,salary)
           values ('10','test10','2021-06-22 13:59:32',200010)
        ;'''
#cursor.execute("select * from account;")
#cursor.execute("select * from blog_test;")

#cursor.execute("SELECT * FROM inventory;")
#rows = cursor.fetchall()

# Print all rows
#for row in rows:
#    print("Data row = (%s, %s, %s, %s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) ))

cursor.execute(acctSQL2)
print("conn ok2")
conn.commit()

cursor.close()
conn.close()