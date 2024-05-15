import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',12345))

msg='Hey server'

try:
    while True:
        client_socket.send(msg.encode('utf-8'))
        data=client_socket.recv(1024)
        print(str(data))

        more_msg=input("Want to send more message (y/n) ? :")
        if more_msg.lower()=='y':
            msg=input("Enter message : ")
        else:
            break
except:
    print("Exited by user")
client_socket.close()