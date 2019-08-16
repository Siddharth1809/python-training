import pymysql
from pymysql import Error


def insert_Varibles_Into_Table(id, name, price, purchase_date):
    global my_db, my_cursor
    try:
        my_db = pymysql.connect(host='localhost',
                                user='root',
                                password='Mtech',
                                db='Electronics')

        my_cursor = my_db.cursor()
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                                VALUES (%s, %s, %s, %s) """
        recordTuple = (id, name, price, purchase_date)
        my_cursor.execute(mySql_insert_query, recordTuple)
        my_db.commit()
        print("Record inserted successfully into Laptop table")
    except pymysql.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        my_cursor.close()
        my_db.close()
        print("MySQL connection is closed")


insert_Varibles_Into_Table(1, 'Lenovo ThinkPad P71', 6459, '2019-08-14')
insert_Varibles_Into_Table(2, 'Area 51M', 6999, '2019-04-14')
insert_Varibles_Into_Table(3, 'MacBook Pro', 2499, '2019-06-20')
insert_Varibles_Into_Table(4, 'HP Pavilion Power', 1999, '2019-01-11')
insert_Varibles_Into_Table(5, 'MSI WS75 9TL-496', 5799, '2019-02-27')
insert_Varibles_Into_Table(6, 'Microsoft Surface', 2330, '2019-07-23')

"""
insert_query = "\*INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES (%s, %s, %s, %s) \*"
    records_to_insert = [(4, 'HP Pavilion Power', 1999, '2019-01-11'),          # list of tuples
                         (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
                         (6, 'Microsoft Surface', 2330, '2019-07-23')]
    my_cursor = my_db.cursor()
    my_cursor.executemany(insert_query, records_to_insert)      # insert records using executemany(query,records)

"""