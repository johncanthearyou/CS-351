import socket
import os

def get_wc(file_name):
    lines = 0
    words = 0
    chars = 0

    file = open(file_name)
    file.seek(0)
    for line in file:
        print(line)
        lines += 1
        words += len(line.split())
        chars += len(line)

    return f'File: {file_name}\n\tLines: {lines}\n\tWords: {words} \n\tCharacters: {chars}'


# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 4455

# Bind server to the IP:Port address
server_socket.bind((host, port))
server_socket.listen()
print(f'Ready to serve at> {host}:{port}')

while True:
    # Accept incoming connection
    client_socket, addr = server_socket.accept()
    print(f'Got a connection from {addr}')

    # Get File Name & Data
    file_name = client_socket.recv(4096).decode()
    print(f'\tGot File Name: {file_name}')
    file_data = client_socket.recv(4096).decode()
    print('\tReceived File Data\n')

    # Create file and write received data to it
    file = open(file_name, 'x')
    file.write(file_data)
    file.close

    # Process file data, send result to client
    msg = get_wc(file_name).encode('ascii')
    client_socket.send(msg)

    # Don't keep received file around
    os.remove(file_name)

    # Close connection to this client
    client_socket.close()
