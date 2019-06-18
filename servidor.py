import socket
from threading import Thread
HOST = 'localhost' # Endereco IP do Servidor
PORT = 6012  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(3)
listClient = []


for s in range(3):
     con,cliente = tcp.accept()
     listClient.append(con)



for x in range(3):
        print(f'Conectado com {listClient[x]}')

def recebemsg1():
    msg=listClient[0].recv(1024)
    for soc in listClient:
        if soc!=listClient[0]:
           soc.send(msg)
    print(msg.decode('utf-8'))


def recebemsg2():
    tex=listClient[1].recv(1024)
    for soc in listClient:
        if soc!=listClient[1]:
           soc.send(tex)
    print(tex.decode('utf-8'))

def recebemsg3():
    com=listClient[2].recv(1024)
    for soc in listClient:
        if soc!=listClient[2]:
           soc.send(com)
    print(com.decode('utf-8'))

while True:
    cliente1 = Thread(target=recebemsg1())
    cliente1.start()

    cliente2 = Thread(target=recebemsg2())
    cliente2.start()

    cliente3=Thread(target=recebemsg3())
    cliente3.start()

tcp.close()
