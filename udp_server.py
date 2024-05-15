import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.2',123))

while True:
    data,addr=server_socket.recvfrom(4096)
    msg='Hey Client...'
    server_socket.sendto(msg.encode('utf-8'),addr)
    print(str(data.decode('utf-8')))