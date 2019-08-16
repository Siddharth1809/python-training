import pymysql

my_db = pymysql.connect(host='localhost',
                        user='root',
                        password='Mtech',
                        db='test_db')

my_cursor = my_db.cursor()

my_cursor.execute('DROP TABLE IF EXISTS Employee')

table = """CREATE TABLE Employee (First_Name CHAR(20) NOT NULL,
                                Last_Name CHAR(20) NOT NULL,
                                Age INT,
                                Sex CHAR(10),
                                Income FLOAT)"""

my_cursor.execute(table)

my_cursor.close()
my_db.close()
