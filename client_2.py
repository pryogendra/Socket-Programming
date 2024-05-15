import socket

client_socket=socket.socket()

host='127.0.0.3'
port=1233
print("Waiting for the connection....")

try:
    client_socket.connect((host,port))
except Exception as e:
    print(str(e))

response=client_socket.recv(1024)
print(response.decode('utf-8'))
while True:
    Input=input("Say Something 2 : ")
    client_socket.send(str.encode(Input))
    response=client_socket.recv(1024)
    print(response.decode('utf-8'))
