import tkinter

janela = tkinter.Tk()
janela.title("Client1")

l_destinatario = tkinter.Label(janela, text="Destinatário: ", height=2)
l_mensagem = tkinter.Label(janela, text="Mensagem: ", height=2)
l_caixa_de_entrada = tkinter.Label(janela, text="Caixa de Entrada")
l_divisoria = tkinter.Label(janela, text="", bg="gray")
l_divisorian = tkinter.Label(janela, text="", bg="gray")


e_destinatario = tkinter.Entry(janela)
e_mensagem = tkinter.Entry(janela)

b_enviar = tkinter.Button(janela, text="Enviar Mensagem", relief="groove")
b_sair = tkinter.Button(janela, text="Sair", relief='groove')

l_divisorian.grid(row=0, column=0, columnspan=4, sticky="e"+"w")
l_destinatario.grid(row=1, column=1)
l_mensagem.grid(row=2, column=1)
l_divisoria.grid(row=5, column=1, columnspan=4, sticky="e"+"w")
l_caixa_de_entrada.grid(row=7, column=1, columnspan=7)

e_destinatario.grid(row=1, column=2)
e_mensagem.grid(row=2, column=2)

b_enviar.grid(row=3, column=3)
b_sair.grid(row=3, column=2)

janela.geometry("425x500+100+100")
janela.mainloop()
