import socket
from sys import argv
from time import sleep

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hardcode Server IP address
host = 'JWS-MacBook-Pro.local'
port = 4455

# connection to hostname on the port.
client_socket.connect((host, port))

# Open & Read File
file_name = argv[1]
file = open(file_name, 'r')
file_data = file.read()

# Send File Name & Data from server
client_socket.send(file_name.encode('ascii'))
sleep(1)
client_socket.send(file_data.encode('ascii'))

message = client_socket.recv(4096).decode('ascii')
print(message)

file.close()
client_socket.close()
