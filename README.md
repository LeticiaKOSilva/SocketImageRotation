# SocketImageRotation
### -> Criação de 2 sockets(Cliente e Servidor) para realizar uma rotação e cópia de uma imagem em python

- O programa foi feito utilizando a linguagem Python;
- Foram criados 2 arquivos, sendo eles:
  
    - Server: responsável por criar um socket,esperar uma conexão, receber a imagem do cliente, realização a rotação dessa
      imageme e criar uma cópia da imagem com a rotação.
    - Client: responsável por criar um socket, criar uma conexão, lê e enviar uma imagem para o servidor.
      
- As bibliotecas utilizadas foram:
  
    - sockect: criar os sockets;
    - numpy: para criar os arrays necessários para realizar as manipulações necessárias com a imagem;
    - cv2: utilizada para a rotação da imagem.
