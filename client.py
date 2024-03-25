import socket

HOST = 'localhost'
PORT = 55556

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

mensagem = client.recv(1024)
if mensagem == b'SALA':
  client.send(input('Digite seu nome: ').encode())
  client.send(input('Digite o nome da sala: ').encode())