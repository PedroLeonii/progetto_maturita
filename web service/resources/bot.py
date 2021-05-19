from flask_restful import Resource
from flask import request
from bot_manager.server_com import send_bot_manager

class Bot(Resource):
    
    def post(self):
        token = request.get_json().get('token')
        if token:
            resp = send_bot_manager(token)
            return resp
        return resp, 401

    def put(self):
        return {'risp':'PUT request over bot'}

    def get(self):
        return {'risp':'GET request over bot'}

    def delete(self):
        return {'risp':'DELETE request over bot'}
