import datetime
import pytz
import random
import string

import pymysql


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
        db = database_connection()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        result = request.get_json()
        insery_query = "INSERT INTO inventory(Name, Category, ExpiryDate, ManufactureDate, Quantity," \
                       "Image) VALUES (%s, %s, %s, %s, %s, %s)"

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
        cursor.close()

        db.commit()

        db.close()
        return response


    def get(self):
        db = database_connection()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        name = request.args['name']
        category = request.args['category']

        cursor.execute("SELECT Name, Category, ExpiryDate, id, Quantity FROM inventory WHERE Name={} AND Category={}".format(str(name), str(category)))

        result = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify(result)
        # today = datetime.datetime.now()
        # for row in rows:
        #    row["is_expired"] = False if row["is_expired"] > today else True
        #    return jsonify(row)


api.add_resource(Inventory_insert, '/inventories')


if __name__ == "__main__":
    app.run(debug=True)
