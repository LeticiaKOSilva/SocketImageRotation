import socket
import cv2
import numpy as np

PORT = 14000
FILE_NAME = 'imagemRotacionada.jpeg' #Novo caminho/nome da cópia da imagem lida pelo cliente 
ROTATION_DEGREE = 180 #Grau de rotação

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Criando socket
socket_server.bind(('', PORT))#Informando ip,porta
socket_server.listen(1)#Aguardando conexão

print("Servidor presente!\nAguardando a imagem!")

connection, addr = socket_server.accept() #Aceitando conexão

# Recebe os dados da imagem
image_data = b''  # Inicializa uma variável de bytes vazia para armazenar os dados

while True:
    content = connection.recv(2048)
    if not content:
        break
    image_data += content  # Acumula os dados de bytes

# Converte os dados recebidos em uma imagem usando numpy
image_array = np.frombuffer(image_data, dtype=np.uint8)
image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

# Fecha a conexão do cliente
connection.close()

# Aplica a rotação à imagem
altura, largura = image.shape[:2]
ponto = (largura / 2, altura / 2)  # ponto no centro da figura
rotacao = cv2.getRotationMatrix2D(ponto,ROTATION_DEGREE, 1.0)
rotacionado = cv2.warpAffine(image, rotacao, (largura, altura))

# Salva a imagem resultante
cv2.imwrite(FILE_NAME, rotacionado)

print("Servidor recebeu a imagem, aplicou a rotação e salvou a imagem resultante!")
socket_server.close() #Encerrando o servidor
