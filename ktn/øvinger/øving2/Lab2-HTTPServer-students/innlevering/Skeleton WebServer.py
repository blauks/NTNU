from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 7999

serverSocket.bind(('',serverPort))

serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filepath = message.split()[1]
        f = open(filepath[1:])
        outputdata = f.read()

        f.close()

        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")

        response = outputdata + "\r\n"
        connectionSocket.send(response.encode())
        connectionSocket.close()

    except (IOError, IndexError):
        connectionSocket.send(b"HTTP/1.1 404\r\n\r\n")
        connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
        connectionSocket.close()
serverSocket.close()
