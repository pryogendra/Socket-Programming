import sys
import socket

try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except Exception as e:
    print("Failed to connect the socket.")
    print(f'Reasion : {str(e)}')
    sys.exit()

print("Socket is connected.....")

target_host=input("Enter the target host name to connect :")
target_port=int(input("Enter the target port number to connect :"))

try:
    sock.connect((target_host,target_port))
    print(f'Socket is connected to {target_host} port {target_port}')
    sock.shutdown(2)
except Exception as e:
    print("Failed to connect.")
    print(f'Reasion : {str(e)}')
    sys.exit()