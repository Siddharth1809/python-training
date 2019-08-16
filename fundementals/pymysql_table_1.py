import pymysql
from pymysql import Error

my_db = pymysql.connect(host='localhost',
                        user='root',
                        password='Mtech',
                        db='Electronics')

my_cursor = my_db.cursor()

my_cursor.execute('DROP TABLE IF EXISTS Laptop')

try:

    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """
    result = my_cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")
except pymysql.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
        my_cursor.close()
        my_db.close()
        print("MySQL connection is closed")
