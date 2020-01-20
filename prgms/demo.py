import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")

mycursor = mydb.cursor()           #cursors as pointer point to the location
mycursor.execute("show databases")  #If you want to execute any sql stmt use execute()

for i in mycursor:
    print(i)