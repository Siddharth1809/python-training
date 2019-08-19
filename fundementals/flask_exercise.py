# curl is used in command lines or scripts to transfer data.
# It is also used in cars, television sets, routers, printers, audio equipment, mobile phones, tablets,
# settop boxes, media players and is the internet transfer backbone for thousands of software applications
# affecting billions of humans daily.
# sudo apt install curl

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Python'


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries ',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False

    },
    {
        'id': 2,
        'title': u'Learn Python ',
        'description': u'Need to find a good python tutorial on the web',
        'done': False

    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)

    return jsonify({'tasks': task[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


if __name__ == "__main__":
    app.run(debug=True)
