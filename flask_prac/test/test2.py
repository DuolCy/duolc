from test.common.sql_database import *
sql='select * from user;'
a=select_change().select_db(sql=sql,host='localhost',username='root',pwd='',database='test')
print(a)
li = []
for i in range(len(a)):
    li.append(a[i]['username'])
print(li)
if 'ceshi' in li:
    print(111)
else:
    print(2)
