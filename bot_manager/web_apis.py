import requests

_unsplash_token = 'K-ODZwBXkqDzKqleRjIBlN0OVi27eeh2LiiQSfd1hpc'
_unsplash_url = 'https://api.unsplash.com/photos/random/?query={}&per_page=1&client_id={}'

_giphy_token = ''
_giphy_url = ''

def send_image(bot, list_args, chat_id):
    query = ' '.join(list_args)
    url = _unsplash_url.format(query, _unsplash_token)
    resp = requests.get(url).json()
    print(resp)
    bot.sendPhoto(chat_id, resp['urls']['regular'])

def send_gif(bot, list_args, chat_id):
     query = ' '.join(list_args)
