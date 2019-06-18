import tkinter

janela = tkinter.Tk()
janela.title("Client1")
janela.configure(bg="#DCDCDC")

l_destinatario = tkinter.Label(janela, text=" Destinatário: ", font="Verdana 18 bold", width=11, height=2,
                               bg="#DCDCDC")
l_mensagem = tkinter.Label(janela, text="   Mensagem: ", font="Verdana 18 bold", width=11, height=2, bg="#DCDCDC")
l_caixa_de_entrada = tkinter.Label(janela, text="Caixa de Entrada", font="Verdana 18 bold", height=1, bg="#DCDCDC")
l_divisoriac = tkinter.Label(janela, width=1, height=1, bg="#DCDCDC")
l_divisorian = tkinter.Label(janela, width=1, height=1, bg="#2F4F4F")
l_divisorias = tkinter.Label(janela, width=1, height=1, bg="#2F4F4F")
l_divisoriae = tkinter.Label(janela, width=1, height=1, bg="#2F4F4F")
l_divisoriaw = tkinter.Label(janela, width=1, height=1, bg="#2F4F4F")

msg_list = tkinter.Listbox(janela, height=15, width=56)

e_destinatario = tkinter.Entry(janela, font="Verdana 14 ")
e_mensagem = tkinter.Entry(janela, font="Verdana 14 ")

b_enviar = tkinter.Button(janela, text="Enviar Mensagem", font="Verdana 14 ", width=13, height=1, border=3,
                          relief="groove")
b_sair = tkinter.Button(janela, text="Sair", font="Verdana 14 ", border=3, relief='groove')


l_divisorian.grid(row=0, column=1, columnspan=4, sticky="e"+"w")
l_divisorias.grid(row=10, column=1, columnspan=4, sticky="e"+"w")
l_divisoriae.grid(row=0, column=0, rowspan=11, sticky="n"+"s")
l_divisoriaw.grid(row=0, column=5, rowspan=11, sticky="n"+"s")

l_destinatario.grid(row=1, column=1, sticky="w")
l_mensagem.grid(row=2, column=1, sticky="w")
l_divisoriac.grid(row=5, column=1, columnspan=4, sticky="e"+"w")
l_caixa_de_entrada.grid(row=6, column=1, columnspan=4)

e_destinatario.grid(row=1, column=2)
e_mensagem.grid(row=2, column=2)

b_enviar.grid(row=3, column=2, sticky="n")
msg_list.grid(row=8, column=1, columnspan=3)
b_sair.grid(row=9, column=2, sticky="w")

janela.geometry("+100+100")
janela.mainloop()
