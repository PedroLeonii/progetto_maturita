from .base import Session
from .models import Bot, Comandi, Testo


def get_risposta(nome, token):
    session = Session()
    bot = session.query(Bot).filter_by(token=token).first()
    comando = bot.get_command(nome)
    if comando.get_tipo() == 'TEXT':
        return session.query(Testo).get(comando.id).risposta
    elif comando.get_tipo() == 'API':
        pass
    else:
        pass



