from .database import db
from flask_bcrypt import check_password_hash, generate_password_hash

class Utenti(db.Model):
    __tablename__='utenti'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email

    def login(self, password):
        return check_password_hash(self.password, password)

class Bot(db.Model):
    __tablename__='manager'

    id = db.Column('token', db.String(47), primary_key=True)
    id_utente = db.Column(db.String(200), db.ForeignKey('utenti.id'))
    isalive = db.Column(db.Boolean, default=True)
    
