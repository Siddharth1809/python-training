import pymysql


my_db = pymysql.connect(host='localhost',
                        user='root',
                        password='Mtech',
                        db='test_db')

my_cursor = my_db.cursor()

read_query = "SELECT * FROM Employee WHERE INCOME > '%d'" % (15000)

my_cursor.execute(read_query)
result = my_cursor.fetchall()
for item in result:  # type of item is tuple so it has index values
    First_Name = item[0]
    Last_Name = item[1]
    Age = item[2]
    Sex = item[3]
    Income = item[4]
    print("First_Name : {},Last_Name : {},Age : {}, Sex : {}, Income : {}".format(First_Name, Last_Name,
                                                                                  Age, Sex, Income))
my_cursor.close()
my_db.close()