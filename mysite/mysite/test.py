# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 16:09:08 2021
d
@author: Jack
"""
from datetime import datetime
import psycopg2

dateTimeObj=datetime.now()
tot=0
for i in range(1,101):
     tot=tot+i
print("hello world",tot)

dateTimeObj1=datetime.now()
print("start:",dateTimeObj)
print("end:",dateTimeObj1)



conn = psycopg2.connect(database="TestDB", user="postgres", password="Td950439", host="127.0.0.1", port="5432")
print ("Opened database successfully")
cursor = conn.cursor()
cursor.execute("select * from blog_test;")

#cursor.execute("SELECT * FROM inventory;")
rows = cursor.fetchall()

# Print all rows
for row in rows:
    print("Data row = (%s, %s, %s, %s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) ))

#import qrcode
#img=qrcode.make("https://www.yahoo.com.tw")    
#img.show() 

