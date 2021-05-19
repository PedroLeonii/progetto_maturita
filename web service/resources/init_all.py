from .users import User, Login
from .bot import Bot

def init_all(api):
    api.add_resource(User, '/user', '/user/<int:id>', endpoint='user')
    api.add_resource(Login, '/login', endpoint='login')
    api.add_resource(Bot, '/bot', endpoint='bot')
    