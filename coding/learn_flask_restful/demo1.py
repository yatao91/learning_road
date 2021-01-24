# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, inputs, fields, marshal_with


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


class Todo1(Resource):
    def get(self):
        # 默认200
        return {'task': 'hello world'}


class Todo2(Resource):
    def get(self):
        # 设置为201
        return {'task': 'hello world'}, 201


class Todo3(Resource):
    def get(self):
        # 设置为201,且返回自定义header
        return {'task': 'hello world'}, 201, {'Etag': 'some-opaque-string'}


class Todos(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=int, help='Rate to charge for this response')
        args = parser.parse_args(strict=True)
        return {'hello': 'suyatao'}


resource_fields = {
    "task": fields.String,
    "uri": fields.Url('todo_ep')
}


class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # 这个字段不会在响应中
        self.status = 'active'


class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')


api.add_resource(HelloWorld, '/', '/hello')
api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(Todo1, '/api/todo1')
api.add_resource(Todo2, '/api/todo2')
api.add_resource(Todo3, '/api/todo3')
api.add_resource(Todos, '/todos')
api.add_resource(Todo, '/api/todo', endpoint='todo_ep')


if __name__ == '__main__':
    app.run(debug=True)
