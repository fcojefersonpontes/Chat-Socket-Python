# Chat-Socket-Python
Trabalho final da disciplina redes de computadores

Implementação de um chat com sockets de rede, com 3 (três) aplicações de usuáriostrocando mensagens entre pares, com os seguintes requisitos:

•Somente a aplicação do destinatário deve exibir a mensagem;

•Os usuários devem enviar textos curtos, que serão exibidos no aplicativo dousuário destinatário;

•As mensagens devem conter pelo menos três campos: destinatário, assunto emensagem, sendo o campo assunto de preenchimento opcional (pode serenviado em branco);

•Não é obrigatória a execução em diferentes computadores;

•As mensagens exibidas na aplicação devem informar explicitamente qual foi ousuário que enviou tal mensagem.

O trabalho foi desenvolvido na linguagem de programação python, versão 3.6, a interface gráfica dos clients foi desenvolviida com tkinter, recurso nativo do python.

Para testar o projeto deve-se seguir os seguintes passos:

1- Executar o script servidor.py, ele instanciará o servidor socket e ficará disponível para conexão com os clientes;

2- Executar os scripts client1, client2 e client3, ambos inicirão uma interface gráfica;

3- No campo referente ao nome inserir o nome do cliente  e enviar (Botão "Enviar Nome")

4- Fazer os passo 3 para todos os clientes (obs: inserir nomes diferentes para os clientes);

5- Agora pode-se enviar mensagens;

6- preencha o campo destinatário, assunto(opcinal) e mensagem, clique no botão "Enviar Mensagem". O destinatário deve receber em sua caixa de entrada a mensagem enviada.

7- Para sair clique no botão "Sair"

OBS: O sistema funciona com apenas dois clientes ou mesmo um cliente
