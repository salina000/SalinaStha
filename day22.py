import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "june4"
)
mydb = connection.cursor()
mydb.execute('Select * from student')
# mydb.execute('Select name from student')
# mydb.execute('Select id from student')
data = mydb.fetchall()
print(data)

# insert
mydb.execute("insert into `student` (`id`,`name`) values (45,'I am from python'))
connection.commit()