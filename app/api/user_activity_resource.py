from flask_restful import Resource, Api
from flask import jsonify
from . import api

user_activity_api = Api(api)


class UserActivityResource(Resource):

    def get(self):
        return jsonify({'message': 'Hello, World!'})


user_activity_api.add_resource(UserActivityResource, '/')
