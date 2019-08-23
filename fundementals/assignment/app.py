"""
import datetime
import pytz
date_str = "2018-11-30 00:00:00"
datetime_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
datetime_obj_utc = datetime_obj.astimezone(tz=pytz.timezone('US/Central'))
print(datetime_obj_utc.strftime("%Y-%m-%d %H:%M:%S %Z"))
"""
from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def get_method():
    name = request.args['name']
    category = request.args['category']

    temp ="{} {}".format(name,category)

    new = temp.split(" ")
    return new[1]


if __name__ == "__main__":
    app.run(debug=True)
