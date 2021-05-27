import telepot
from telepot.loop import MessageLoop
import json
from gen_risposte import genera_risposte

class BotManager:

    def __init__(self, token):
        self.token = token
        self.bot = telepot.Bot(token)
        self.handlers = {'chat': self.handler_message, 'callback_query': self.handler_callback}

    def start_bot_manager(self):
        try:
            self.bot.getMe()
        except Exception:
            return json.dumps({'ok':False, 'msg': 'Token invalid'})
        MessageLoop(self.bot, self.handlers).run_as_thread()
        return json.dumps({'ok': True, 'msg': 'Token valid'})

    def handler_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        content = msg['text'].split(' ')
        comando = content[0]
        list_args = content[1:] if len(content) > 0 else []

        if content_type == 'text' and comando.startswith('/'):
            genera_risposte(
                comando,
                chat_id,
                self.bot,
                list_args
            )
        elif content_type == 'voice':
            self.bot.sendMessage(chat_id, 'Sono sordo muto!')
        elif content_type == 'photo':
            self.bot.sendMessage(chat_id, 'bella photo')
        else:
            self.bot.sendMessage(chat_id, 'bella gif')

    def handler_callback(self, msg):
        pass
