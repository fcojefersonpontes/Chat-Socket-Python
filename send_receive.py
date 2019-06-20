
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            #msg = client_socket.recv(BUFSIZ).decode("utf8")
            tex, orig = client_socket.recvfrom(1024)
            tex = tex.decode('utf-8')
            texto = tex.split()

            if texto[1] == my_name.get():
                msg = f"De:{texto[0]}\nPara:{my_name.get()}\nAssunto:{texto[2]}\nMensagem:{texto[3]}\n"
            elif len(texto) > 5:
                if texto[5] == my_name.get():
                    msg = f"De:{texto[4]}\nPara:{my_name.get()}\nAssunto:{texto[6]}\nMensagem:{texto[7]}\n"


            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    if my_destinatario != "":
        msg = my_destinatario.get() + '\n' + my_assunto.get() + '\n' + my_msg.get() + '\n'
        my_destinatario.set("")  # Clears input field.
        my_assunto.set("")
        my_msg.set("")      # Clears input field.
        client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        janela.quit()


def sair(event=None):  # event is passed by binders.
    """Encerrar a conexão"""
    msg = "{quit}"
    client_socket.send(bytes(msg, "utf8"))
    client_socket.close()
    janela.quit()



def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

janela = tkinter.Tk()
janela.title("Client1")
janela.configure(bg="#DCDCDC")
janela.geometry("+100+100")


messages_frame = tkinter.Frame(janela)
my_name = tkinter.StringVar()
my_destinatario = tkinter.StringVar()
my_assunto = tkinter.StringVar()
my_msg = tkinter.StringVar()  # For the messages to be sent.

scrollbar = tkinter.Scrollbar(messages_frame)

l_my_name = tkinter.Label(janela, text=" Seu nome: ", font="Verdana 16 bold", width=11, height=2, bg="#DCDCDC")
l_destinatario = tkinter.Label(janela, text=" Destinatário:", font="Verdana 16 bold", width=11, height=1, bg="#DCDCDC")
l_assunto = tkinter.Label(janela, text="       Assunto:", font="Verdana 16 bold", width=11, height=1, bg="#DCDCDC")
l_mensagem = tkinter.Label(janela, text="   Mensagem:", font="Verdana 16 bold", width=11, height=1, bg="#DCDCDC")

l_caixa_de_entrada = tkinter.Label(janela, text="Caixa de Entrada", font="Verdana 16 bold", height=1, bg="#DCDCDC")

l_divisoriac = tkinter.Label(janela, width=1, height=1, bg="#DCDCDC")
l_divisorian = tkinter.Label(janela, width=1, height=1, bg="#2F4F4F")
l_divisorias = tkinter.Label(janela, width=1, height=1, bg="#2F4F4F")
l_divisoriae = tkinter.Label(janela, width=1, height=1, bg="#2F4F4F")
l_divisoriaw = tkinter.Label(janela, width=1, height=1, bg="#2F4F4F")

msg_list = tkinter.Listbox(janela, height=11, width=38, font="Verdana 12 bold", fg="#2F4F4F", border=2,
                           yscrollcommand=scrollbar.set)
e_my_name = tkinter.Entry(janela, font="Verdana 12 bold", fg="#2F4F4F", textvariable=my_name)
e_my_name.bind("<Return>", )
e_destinatario = tkinter.Entry(janela, font="Verdana 12 bold", fg="#2F4F4F", textvariable=my_destinatario)
e_destinatario.bind("<Return>", )
e_assunto = tkinter.Entry(janela, font="verdana 12 bold", fg="#2F4F4F", textvariable=my_assunto)
e_assunto.bind("<Return>", )
e_mensagem = tkinter.Entry(janela, font="Verdana 12 bold", fg="#2F4F4F", textvariable=my_msg)
e_mensagem.bind("<Return>", )

janela.protocol("WM_DELETE_WINDOW", on_closing)

b_enviar = tkinter.Button(janela, text="Enviar Mensagem", font="Verdana 14 bold", height=1, border=3,
                          relief="groove", fg="#2F4F4F", command=send)
b_sair = tkinter.Button(janela, text="Sair", font="Verdana 14 bold", fg="#B22222", border=3, relief='groove',
                        command=sair)

scrollbar.grid()
msg_list.grid(row=9, column=1, columnspan=2)
messages_frame.grid()

l_divisorian.grid(row=0, column=0, columnspan=3, sticky="e"+"w")
l_divisorias.grid(row=11, column=0, columnspan=3, sticky="e"+"w")
l_divisoriae.grid(row=0, column=0, rowspan=12, sticky="n"+"s")
l_divisoriaw.grid(row=0, column=3, rowspan=12, sticky="n"+"s")

l_my_name.grid(row=1, column=1, sticky="w")
l_destinatario.grid(row=2, column=1, sticky="w")
l_assunto.grid(row=3, column=1, sticky="w")
l_mensagem.grid(row=4, column=1, sticky="w")
l_divisoriac.grid(row=7, column=1)
l_caixa_de_entrada.grid(row=8, column=1, columnspan=3)

e_my_name.grid(row=1, column=2)
e_destinatario.grid(row=2, column=2)
e_assunto.grid(row=3, column=2)
e_mensagem.grid(row=4, column=2)

b_enviar.grid(row=5, column=2, sticky="n")

b_sair.grid(row=11, column=1, columnspan=3)


HOST = "localhost"
PORT = 33000
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
# Starts GUI execution.
janela.mainloop()
