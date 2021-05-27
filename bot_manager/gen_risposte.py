from database.models import Bot, Testuali, Api
from database.base import Session
from web_apis import send_image

_APIS = {'get_image': send_image, }


def genera_risposte(nome_comando, chat_id, bot, list_args):
    session = Session()
    db_bot = session.query(Bot).filter_by(token= bot._token).first()
    comando = db_bot.get_command(nome_comando)
    if comando.get_tipo() == 'TEXT':
        comando_txt = session.query(Testuali).get(comando.id)
        if comando_txt.controllo_args(list_args):
            risposta = comando_txt.risposta.format(*list_args)
            bot.sendMessage(chat_id, risposta)
        else:
            bot.sendMessage(chat_id, comando.help_msg)
    elif comando.get_tipo() == 'API':
        comando_api = session.query(Api).get(comando.id)
        _APIS[comando_api.funzione](bot, list_args, chat_id)
    else:
        pass



