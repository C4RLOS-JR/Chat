import socket
import threading

HOST = 'localhost'
PORT = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

while True:
  client, addr = server.accept()
  client.send(b'SALA')
  nome = client.recv(1024).decode()
  sala = client.recv(1024).decode()
  print(sala)