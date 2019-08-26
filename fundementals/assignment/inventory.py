import datetime
import pytz
import random
import string
import logging
import pymysql

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")

file_handler = logging.FileHandler('inventory1.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def database_connection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='db')
    return connection


from flask import Flask, request, jsonify

from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app, prefix='/api/v1.0')


class Inventory_insert(Resource):
    def post(self):

        try:
            logger.info("Database connection established")
            db = database_connection()
            cursor = db.cursor(pymysql.cursors.DictCursor)
            logger.info("Insert method running")
            insery_query = "INSERT INTO inventory(Name, Category, ExpiryDate, ManufactureDate, Quantity," \
                           "Image) VALUES (%s, %s, %s, %s, %s, %s)"
            result = request.get_json(force=True)
            if result.get('ExpiryDate'):
                date_str = result["ExpiryDate"]

                try:
                    date_convert = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S %z")
                    datetime_obj_cst = date_convert.astimezone(tz=pytz.timezone('US/Central'))
                    result["ExpiryDate"] = datetime_obj_cst
                except Exception:
                    print("Bad Request")
            else:
                result["ExpiryDate"] = None

            date_str_man = result["ManufactureDate"]
            try:
                date_convert_man = datetime.datetime.strptime(date_str_man, "%Y-%m-%d %H:%M:%S %z")
                datetime_obj_cst_man = date_convert_man.astimezone(tz=pytz.timezone('US/Central'))
                result["ManufactureDate"] = datetime_obj_cst_man
            except Exception:
                print("Enter valid time")

            image_file = result["Image"].split(".")

            result["Image"] = ''.join(random.sample(string.ascii_lowercase, 5)) + '.' + image_file[1]

            record = (
                result["Name"], result["Category"], result["ExpiryDate"], result["ManufactureDate"], result["Quantity"],
                result["Image"])

            cursor.execute(insery_query, record)
            response = jsonify("Inventory added successfully")
            logger.info(
                "Name: {}, Category: {}, ExpiryDate: {}, ManufactureDate: {}, Quantity: {}, Image: {} inserted successfully".
                format(result["Name"], result["Category"], result["ExpiryDate"], result["ManufactureDate"],
                       result["Quantity"], result["Image"]))
            db.commit()
            cursor.close()
            db.close()
            logger.info("Database connection closed")
            return response

        except Exception as e:
            logger.exception("Exception occurs at insert method", e)

    def get(self):
        try:
            logger.info("Database connection established")
            db = database_connection()
            cursor = db.cursor(pymysql.cursors.DictCursor)

            logger.info("get method called")
            name = request.args['name']
            category = request.args['category']

            if name and category:
                select_query = "SELECT Name, Category, ExpiryDate, id, Quantity FROM inventory WHERE Name=%s AND Category=%s"
                record = (str(name), str(category))
                result = cursor.execute(select_query, record)
                rows = cursor.fetchall()
                today = datetime.datetime.now()
                for row in rows:
                    if row["ExpiryDate"] == None:
                        row["is_expired"] = "expiry date not given"
                    else:
                        row["is_expired"] = False if row["ExpiryDate"] > today else True

            else:
                select_query = "SELECT Name, Category, ExpiryDate, id, Quantity FROM inventory WHERE Name=%s OR Category=%s"
                record = (str(name), str(category))
                result = cursor.execute(select_query, record)
                rows = cursor.fetchall()
                today = datetime.datetime.now()
                for row in rows:
                    if row["ExpiryDate"] == None:
                        row["is_expired"] = "expiry date not given"
                    else:
                        row["is_expired"] = False if row["ExpiryDate"] > today else True

            logger.info("get method successfully completed ")
            cursor.close()
            db.close()
            logger.info("Database connection closed")
            return jsonify(rows)

        except Exception as e:
            logger.exception("Exception occurs at search method", e)

    def put(self, id):
        try:
            logger.info("Database connection established")
            db = database_connection()
            cursor = db.cursor()
            logger.info("update quantity method called")
            result = request.get_json()
            update_query = "UPDATE inventory SET Quantity=%s WHERE id=%s"
            record = (result["Quantity"], id)
            cursor.execute(update_query, record)
            db.commit()
            response = jsonify("Quantity updated successfully")
            logger.info(" Quantity: {} updated successfully at id: {}".format(result["Quantity"], id))
            cursor.close()
            db.close()
            logger.info("Database connection closed")
            return response

        except Exception as e:
            logger.exception("Exception occurs at update quantity method", e)

    def delete(self, id):
        try:
            logger.info("Database connection established")
            db = database_connection()
            cursor = db.cursor(pymysql.cursors.DictCursor)
            logger.info("delete image method called")
            delete_image = "UPDATE inventory SET Image=%s WHERE id=%s"
            record = ('Null', id)
            cursor.execute(delete_image, record)
            db.commit()
            response = jsonify("Image deleted successfully")
            logger.info(" Image deleted successfully at id: {}".format(id))
            cursor.close()
            db.close()
            logger.info("Database connection closed")
            return response

        except Exception as e:
            logger.exception("Exception occurs in delete image method", e)


api.add_resource(Inventory_insert, '/inventories', '/inventories/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)
