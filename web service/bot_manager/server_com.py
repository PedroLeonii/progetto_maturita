import socket
import json
from flask import jsonify

def send_bot_manager(msg, host='localhost', port=5000):
    client = socket.socket()
    client.connect((host, port))
    client.send(msg.encode('UTF-8'))
    response = json.loads(client.recv(1024).decode('UTF-8'))
    client.close()
    return response