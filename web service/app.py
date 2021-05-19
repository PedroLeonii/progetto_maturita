from flask import Flask, request, jsonify
from flask_restful import Api
from resources.init_all import init_all
from models.database import init_db
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_pyfile('./configuration.cfg')

api = Api(app)

JWTManager(app)
Bcrypt(app)
init_db(app)
init_all(api)

if __name__ == '__main__':
    app.run(port='5001', debug=True)
    