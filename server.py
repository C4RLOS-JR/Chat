import socket
import threading

HOST = 'localhost'
PORT = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

def  broadcast(sala, mensagem):
  for pessoa in salas[sala]:
    if isinstance(mensagem, str):
      mensagem = mensagem.encode()
    pessoa.send(mensagem)

def enviarMensagem(nome, sala, client):
  mensagem = client.recv(1024).decode()
  mensagem = f'{nome}: {mensagem}\n'
  broadcast(sala, mensagem)

salas = {}

while True:
  client, addr = server.accept()
  client.send(b'SALA')
  nome = client.recv(1024).decode()
  sala = client.recv(1024).decode()
  if sala not in salas.keys():
    salas[sala] = []
  salas[sala].append(client)
  print(f'{nome} se conectou na sala {sala}! - INFO{addr}')
  broadcast(sala, f'{nome}: Entrou na sala!\n')
  
  thread = threading.Thread(target=enviarMensagem, args=(nome, sala, client))
  thread.start()