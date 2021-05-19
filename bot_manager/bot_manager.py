import requests
import telepot
from telepot.loop import MessageLoop
import json
import urllib

class BotManager():
    def __init__(self, token):
        self.bot = telepot.Bot(token)

    def start_bot_manager(self):
        try:
            self.bot.getMe()
        except Exception:
            return json.dumps({'ok':False, 'msg':'Token invalid'})
        MessageLoop(self.bot, self.handler).run_as_thread()
        return json.dumps({'ok':True, 'msg':'Token valid'})

    def handler(self, msg):
        testo = msg.get('text')
        content_type, chat_type, chat_id = telepot.glance(msg)
        