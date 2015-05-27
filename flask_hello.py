from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        raise ApiError(400, "duckies")

class ApiError(Exception):
    def __init__(self, code, message = None):
        self.code = code
        if message is not None:
            self.data = {
                'status': code,
                'message': message
            }

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)