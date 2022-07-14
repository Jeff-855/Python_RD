from datetime import datetime

dateTimeObj=datetime.now()
tot=0
for i in range(1,101):
    tot=tot+i
print("hello world",tot)

dateTimeObj1=datetime.now()
print("start:",dateTimeObj)
print("end:",dateTimeObj1)