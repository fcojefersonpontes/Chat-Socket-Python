import tkinter


def send_name():
    msg = my_name.get()
    if msg != "":
        #client_socket.send(bytes(msg, "utf8"))
        print(msg)
        interface_name.quit()

interface_name = tkinter.Tk()
interface_name.configure()
interface_name.title("Tk teste")
interface_name.geometry("+100+100")

my_name = tkinter.StringVar()

l_divisorian = tkinter.Label(interface_name, width=1, height=1, bg="#2F4F4F")
l_divisorias = tkinter.Label(interface_name, width=1, height=1, bg="#2F4F4F")
l_divisoriae = tkinter.Label(interface_name, width=1, height=1, bg="#2F4F4F")
l_divisoriaw = tkinter.Label(interface_name, width=1, height=1, bg="#2F4F4F")
l_divisorian.grid(row=0, column=0, columnspan=3, sticky="e"+"w")
l_divisorias.grid(row=25, column=0, columnspan=3, sticky="e"+"w")
l_divisoriae.grid(row=0, column=0, rowspan=25, sticky="n"+"s")
l_divisoriaw.grid(row=0, column=3, rowspan=26, sticky="n"+"s")

l_nome = tkinter.Label(interface_name, text="Qual o seu nome ?", height=2, width=25, font="Verdana 16 bold")
l_nome.grid(row=2, column=2)

e_nome = tkinter.Entry(interface_name, font="Verdana 16", border=2, textvariable=my_name)
e_nome.grid(row=8, column=2, sticky="n")


b_1 = tkinter.Button(interface_name, text="Confirmar", font="Verdana 14 bold", fg="#2F4F4F", border=2,
                     command=send_name)
b_1.grid(row=12, column=2)


interface_name.mainloop()
