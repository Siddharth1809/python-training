import pymysql
import pymysql.cursors

my_db = pymysql.connect(host='localhost',
                        user='root',
                        password='Mtech',
                        db='test_db',
                        cursorclass=pymysql.cursors.DictCursor)

with my_db:
    my_cursor = my_db.cursor()

    read_query = "SELECT * FROM Employee WHERE INCOME > '%d'" % (15000)

    my_cursor.execute(read_query)
    result = my_cursor.fetchall()
    for item in result:
        print(item["First_Name"], item["Last_Name"], item["Age"], item["Sex"], item["Income"])

# we import pymysql.cursors and cursorclass in pymysql.cursors.DictCursosrs
# which allows to fetch record by column name
