import socket

# domain 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    client_socket, addr = server_socket.accept()
    print('Connection', addr)

    while True:
        request = client_socket.recv(1024)

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)

    client_socket.close()