import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg='Hey Server...'
while True:
    client_socket.sendto(msg.encode('utf-8'),('127.0.0.2',123))
    data,addr=client_socket.recvfrom(4096)
    print("Server says : "+str(data.decode('utf-8')))
    msg=input('Enter new message to send : ')
client_socket.close()