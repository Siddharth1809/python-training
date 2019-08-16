

# create database 'test_db'

import pymysql

my_db = pymysql.connect(host='localhost',
                        user='root',
                        password='Mtech',
                        )

my_cursor = my_db.cursor()

my_cursor.execute('create database Electronics')

my_cursor.close()
my_db.close()
