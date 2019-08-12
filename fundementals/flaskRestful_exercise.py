from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'world'}


api.add_resource(HelloWorld, '/')

todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(TodoSimple, '/<string:todo_id>')

# $ curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
# $ curl http://localhost:5000/todo1 -d "data=change my breakpads" -X PUT


if __name__ == "__main__":
    app.run(debug=True)
