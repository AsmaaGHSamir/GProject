import sqlite3

with open("C:\\Users\Asmaa Samir\Desktop\Project\data.txt", "w") as myFile:
    my_tuple1 = ('google.com ', '198.188.3.2 ', '255.255.255.0', '11:01 ')
    my_tuple2 = ('youtube.com', '199.588.35.22', '255.255.255.0', '1:01')
    my_tuple3 = ('google.com', '198.155.66.1', '255.255.255.0', '7:55')

    myFile.writelines(my_tuple1)
    myFile.writelines(my_tuple2)
    myFile.writelines(my_tuple3)

db = sqlite3.connect("data.db")  # create database and connect
cr = db.cursor()  # تفعيل

# noinspection SqlNoDataSourceInspection
cr.execute("CREATE TABLE  Analysis (User Name text, IP , MAC ,URLs being visited ,TIME) ")

cr.execute("insert into Analysis values(?, ?, ?, ?, ?)", my_tuple1)  # insert data

cr.execute("insert into skills values(?, ?, ?, ?, ?)", my_tuple2)

cr.execute("insert into skills values(?, ?, ?, ? , ?)", my_tuple3)

db.commit()  # save
db.close()  # close
