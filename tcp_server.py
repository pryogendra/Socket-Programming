import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12345))
server_socket.listen(1) #argument is connection number

msg='Hey Client'
while True:
    print("Server waiting for connection......")
    client_socket,addr=server_socket.accept()
    print(f'Client connected from {addr}')
    while True:
        data=client_socket.recv(1024)
        if not data or not data.decode('utf-8'):
            break
        else:
            print(f'Received from the client : '+data.decode('utf-8'))
        try:
            client_socket.send(bytes(msg,'utf-8'))
        except:
            print('Exited bt the user.')
        msg=f'I received {data}'
    client_socket.close()

