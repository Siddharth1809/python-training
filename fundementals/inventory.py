import pymysql

import datetime
import logging
from flask import Flask, request, jsonify, url_for
from flask_restful import Resource, Api

my_db = pymysql.connect(host='localhost',
                        user='root',
                        password='root',
                        db='db')
my_cursor = my_db.cursor()

app = Flask(__name__)

api = Api(app, prefix='/api/v1.0')

today = datetime.datetime.utcnow()

logger = logging.getLogger(__name__)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('inventory.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class InventoryCollection(Resource):

    def get(self):
        try:
            my_cursor = my_db.cursor(pymysql.cursors.DictCursor)

            my_cursor.execute('''select id,Name,Category,Quantity, DATE_FORMAT(CONVERT_TZ(str_to_date(ExpiryDate,'%Y-%m-%d %H:%i:%s'),
                                'GMT','US/Central'), '%d/%m/%Y %h:%i %p') as 'Expiry-Date', DATE_FORMAT(CONVERT_TZ(str_to_date(ManuFactureDate,'%Y-%m-%d %H:%i:%s'),
                                'GMT','US/Central'), '%d/%m/%Y %h:%i %p') as 'ManuFacture-Date'
                                from inventory  ''')
            rows = my_cursor.fetchall()
            response = jsonify(rows)
            my_cursor.close()
            my_db.close()
            return response

        except Exception as e:
            logging.exception(e)

    def post(self):
        try:
            result = request.get_json()

            insert_query = "INSERT INTO inventory(Name, Category, ExpiryDate, ManufactureDate, Quantity) VALUES(%s, %s, %s, %s, %s)"
            record = (
                result['Name'], result['Category'], result['ExpiryDate'], result['ManufactureDate'], result['Quantity'])
            my_cursor.execute(insert_query, record)
            my_db.commit()
            response = jsonify('Inventory inserted successfully!')
            my_cursor.close()
            my_db.close()
            return response

        except Exception as e:
            logging.exception(e)


class InventoriesName(Resource):

    def get(self, name):
        try:
            my_cursor = my_db.cursor(pymysql.cursors.DictCursor)
            my_cursor.execute("SELECT Name,Category,ExpiryDate,id,Quantity FROM inventory WHERE Name=%s", name)
            rows = my_cursor.fetchall()
            for row in rows:
                row["is_expired"] = False if row["ExpiryDate"] > today else True
            my_cursor.close()
            my_db.close()
            return jsonify(rows)

        except Exception as e:
            logging.exception(e)


class InventoriesCategory(Resource):

    def get(self, category):
        try:
            my_cursor = my_db.cursor(pymysql.cursors.DictCursor)
            my_cursor.execute("SELECT Name,Category,ExpiryDate,id,Quantity FROM inventory WHERE Category=%s", category)
            rows = my_cursor.fetchall()
            for row in rows:
                row["is_expired"] = False if row["ExpiryDate"] > today else True
            my_cursor.close()
            my_db.close()
            return jsonify(rows)

        except Exception as e:
            logging.exception(e)


class InventoryUpdate(Resource):
    def put(self, id):
        try:
            result = request.get_json()
            update_query = "UPDATE inventory SET Quantity=%s WHERE id=%s"
            record = (result['Quantity'], id)
            my_cursor.execute(update_query, record)
            my_db.commit()
            response = jsonify('Quantity updated successfully!')
            my_cursor.close()
            my_db.close()
            return response

        except Exception as e:
            logging.exception(e)


class InventoryImage(Resource):
    def put(self, id):
        try:
            result = request.get_json()
            update_query = "UPDATE inventory SET Image=%s WHERE id=%s"
            record = (result['Image'], id)
            my_cursor.execute(update_query, record)
            my_db.commit()
            response = jsonify('Image updated successfully')
            my_cursor.close()
            my_db.close()
            return response

        except Exception as e:
            logging.exception(e)

    def get(self, id):
        try:
            my_cursor = my_db.cursor(pymysql.cursors.DictCursor)
            my_cursor.execute("SELECT Name,Category,ExpiryDate,id,Quantity,Image FROM inventory WHERE id=%s", id)
            rows = my_cursor.fetchall()
            url = "http://localhost:5000"
            with app.test_request_context():
                for row in rows:
                    if row["Image"] != 'Null':
                        row["ImageURL"] = url + url_for("static", filename=row["Image"])
                    else:
                        row["ImageURL"] = 'Image deleted'
            my_cursor.close()
            my_db.close()
            return jsonify(rows)

        except Exception as e:
            logging.exception(e)


class Inventory_Image_Delete(Resource):
    def delete(self, id):
        try:
            my_cursor = my_db.cursor(pymysql.cursors.DictCursor)
            delete_query = "UPDATE inventory SET Image = %s WHERE id = %s"
            record = ('Null', id)
            my_cursor.execute(delete_query, record)

            my_db.commit()
            rows = my_cursor.fetchone()
            my_cursor.close()
            my_db.close()
            return jsonify(rows)

        except Exception as e:
            logging.exception(e)


api.add_resource(InventoryCollection, '/inventories')
api.add_resource(InventoriesName, '/inventories/<string:name>')
api.add_resource(InventoriesCategory, '/inventories/category/<string:category>')
api.add_resource(InventoryUpdate, '/inventories/<int:id>')
api.add_resource(InventoryImage, '/inventories/images/<int:id>')
api.add_resource(Inventory_Image_Delete, '/inventories/images/remove/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)
