import pymysql


def insert_new_record(First_Name, Last_Name, Age, Sex, Income):
    global my_db, my_cursor
    try:
        my_db = pymysql.connect(host='localhost',
                                user='root',
                                password='Mtech',
                                db='test_db')
        my_cursor = my_db.cursor()
        insert_query = "INSERT INTO Employee(First_Name, Last_Name,Age, Sex, Income) VALUES(%s, %s, %s, %s, %s)"
        record = (First_Name, Last_Name, Age, Sex, Income)
        my_cursor.execute(insert_query, record)
        my_db.commit()
        print("Record inserted successfully into Employee table")
        print(my_cursor.rowcount)
        print(my_cursor.rownumber)
        print(my_cursor.lastrowid)

    finally:
        my_db.close()
        my_cursor.close()

n = int(input("Enter number of records:"))
for i in range(n):
    First_Name = str(input("Enter Employee First Name:"))
    Last_Name = str(input("Enter Employee Last Name:"))
    Age = int(input("Enter Employee Age:"))
    Sex = str(input("Enter Employee Sex M|F:"))
    Income = float(input("Enter Employee Income:"))
    insert_new_record(First_Name, Last_Name, Age, Sex, Income)
