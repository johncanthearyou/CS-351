import socket
from sys import argv

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hardcode Server IP address
host = "ip-172-31-28-157"
port = 9999

# connection to hostname on the port.
client_socket.connect((host, port))

# Open & Read File
file_name = argv[1]
file = open(file_name, "r")
file_data = file.read()

# Send File Name & Data from server
client_socket.send(file_name.encode())
client_socket.send(file_data.encode())

client_socket.close()
