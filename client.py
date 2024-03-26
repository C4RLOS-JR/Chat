import socket
import threading
from tkinter import *
import tkinter
from tkinter import simpledialog


class Chat:
  def __init__(self):
    HOST = 'localhost'
    PORT = 55556
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.client.connect((HOST, PORT))

    login = Tk()
    login.withdraw()

    self.janela_carregada = False
    self.ativo = True

    self.nome = simpledialog.askstring('Nome', 'Digite seu nome!', parent=login)
    self.sala = simpledialog.askstring('Sala', 'Digite o nome da sala deseja entrar!', parent=login)

    thread = threading.Thread(target=self.conectar)
    thread.start()
    self.janela()

  def janela(self):
    self.root = Tk()
    self.root.geometry('500x400')
    self.root.title('Chat')

    self.caixa_texto = Text(self.root)
    self.caixa_texto.place(relx=0.05, rely=0.01, width=450, height=300)

    self.enviar_mensagem = Entry(self.root)
    self.enviar_mensagem.place(relx=0.05, rely=0.8, width=390, height=20)

    self.btn_enviar = Button(self.root, text='Enviar', command=self.enviarMensagem)
    self.btn_enviar.place(relx=0.85, rely=0.8, width=50, height=20)
    self.root.protocol('WM_DELETE_WINDOW', self.fechar)

    self.root.mainloop()

  def fechar(self):
    self.root.destroy()
    self.client.close()

  def conectar(self):
    while True:
      recebido = self.client.recv(1024)
      if recebido == b'SALA':
        self.client.send(self.nome.encode())
        self.client.send(self.sala.encode())
      else:
        try:
          self.caixa_texto.insert('end', recebido.decode())
        except:
          pass

  def enviarMensagem(self):
    mensagem = self.enviar_mensagem.get()
    self.enviar_mensagem.delete(0,END)
    self.client.send(mensagem.encode())

chat = Chat()