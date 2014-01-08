import os
import json

from flask import Flask, request
from flask.ext import restful
from flask.ext.restful import reqparse

from ext_module import external

# Instantiate Flask app, load Flask-RESTful API
app = Flask(__name__)
api = restful.Api(app)


class Watch(restful.Resource):
    def get(self):
        return {'time': external.give_me_time()}


class Queries(restful.Resource):
    def __init__(self):
        """Used to instantiate argument parsing data fields"""
        super(Queries, self).__init__()
        self.parser = reqparse.RequestParser()

    def get(self):
        """
        Currently coded to echo the query parameters received as response
        """
        self.parser.add_argument("title", type=str)
        self.parser.add_argument("name", type=str)
        args = self.parser.parse_args()
        return {'answer': args}


# Create a RESTful "resource"
class Tasks(restful.Resource):
    def get(self, todo_id):
        """Used when HTTP verb GET is used at resource URL"""
        return {todo_id: todos[todo_id]}

    def post(self, todo_id):
        """Used when HTTP verb POST is used at resource URL"""
        todos[todo_id] = json.loads(request.data)
        return {todo_id: todos[todo_id]}


# Load sample data to API server
# In production, this will be a DB connection or setting
todos = {
            1: {'title': u'Buy groceries',
                'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
                'done': False},
            2: {'title': u'Learn Python',
                'description': u'Need to find a good Python tutorial on web',
                'done': False}
        }


api.add_resource(Watch, '/', '/api/v1.0/time')
api.add_resource(Queries, '/api/v1.0/query')
api.add_resource(Tasks, '/api/v1.0/tasks/<int:todo_id>')


if __name__ == '__main__':
    # Bind to environment variable PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT_API1', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
