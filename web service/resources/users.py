from flask_restful import Resource, fields, marshal_with, abort
from flask import request
from models.models import Utenti
from models.database import db
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from datetime import timedelta

resource_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email' : fields.String
}

class User(Resource):

    def post(self):
        data = request.get_json()   
        try:
            utente = Utenti(**data)
            db.session.add(utente)
            db.session.commit()
            return {'msg':'user added correctly'}
        except:
            abort(500)
    
    def put(self):
        return {'risp':'PUT request  over user'}

    @jwt_required()
    @marshal_with(resource_fields)
    def get(self, id):
        try:
            utente = Utenti.query.get(id)
            if utente is not None:
                return utente
            raise Exception
        except:
            abort(404)

    @jwt_required()
    @marshal_with(resource_fields)
    def put(self, id):
        data = request.get_json()
        try:
            utente = Utenti.query.filter_by(id=id)
            if utente is not None:
                utente.update(data)
                db.session.commit()
                nuovo_utente = Utenti.query.get(id)
                return nuovo_utente
            raise Exception
        except:
            abort(500)

    @jwt_required()
    @marshal_with(resource_fields)
    def delete(self, id):
        try:
            utente = Utenti.query.get(id)
            db.session.delete(utente)
            db.session.commit()
            return utente
        except:
            abort(500)


class Login(Resource):
    
    def post(self):
        credenziali = request.get_json()
        try:
            password = credenziali['password'] 
            username = credenziali['username']
            utente = Utenti.query.filter_by(username = username).first()
            if password and utente is not None and utente.login(password):
                token = create_access_token(identity=username, expires_delta=timedelta(hours=1))
                return {'token': token, 'id': utente.id}
            raise Exception
        except:
            abort(404)
