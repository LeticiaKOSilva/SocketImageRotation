import socket

HOST = '127.0.0.1' #ip do host
PORT = 14000 #Porta de conexão
FILE_NAME ='foto.jpeg' #caminho/nome da imagem a ser lida pelo cliente

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Criando um socket
socket_client.connect((HOST, PORT)) #Estabelecendo conexão

with open(FILE_NAME,'rb') as image_file:
    image_data = image_file.read() #Lendo imagem
    socket_client.sendall(image_data) #Enviando a mensagem para o servidor

print('Cliente enviou a imagem!')
socket_client.close() #Encerrando o socket cliente
