
import socket
import sys
import json
from time import sleep
from bot_manager import BotManager
        
port = 5000
host = 'localhost'

server = socket.socket()
server.bind((host, port))
server.listen(5)
continua = True

while True:
    connection, address = server.accept()
    print('Recived connection from host {} with port {}'.format(address[0], address[1]))
    token = connection.recv(1024).decode('UTF-8')
    msg = BotManager(token).start_bot_manager()
    connection.send(msg.encode('UTF-8'))

    while continua:
        input_continua = input('continua?')
        if input_continua == 'y':
            sys.exit(1)
        sleep(4)

