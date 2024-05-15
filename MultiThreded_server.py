import socket
from _thread import *

server_socket=socket.socket()

host='127.0.0.3'
port=1233
thread_count=0

try:
    server_socket.bind((host,port))
except Exception as e:
    print(str(e))

print("Waiting for connection..........")
server_socket.listen(5) #maximum connection is 5

def client_thread(connection):
    connection.send(str.encode('Welcome to the server...'))
    while True:
        data=connection.recv(1024)
        reply='Hello,I am Server '+data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()
while True:
    client,addr=server_socket.accept()
    print("Connected to the "+str(addr[0]) +" " + str(addr[1]))
    start_new_thread(client_thread,(client,))
    thread_count += 1
    print("ThreadNumber=" + str(thread_count))