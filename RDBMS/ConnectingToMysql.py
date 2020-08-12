import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="temp")
mycursor = mydb.cursor()
mycursor.execute("select * from emp")
emp_details = mycursor.fetchall()

for i in emp_details:
    print(i)