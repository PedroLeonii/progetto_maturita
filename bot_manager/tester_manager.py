import socket as s

server = ('localhost', 5000)

token = '1726299570:AAFc_QNlpTcX4WtQjxjx81KdTiVZQDADOEg'.encode('utf-8')

soc = s.socket()
soc.connect(server)
soc.send(token)
resp = soc.recv(1024).decode('utf-8')
print(resp)
