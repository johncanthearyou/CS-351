import socket
import os
from sys import argv

# Hardcode Server IP address
host = ''
port = 4455
size = 4096

# This function will create a socket and send a file name and its 
#     associated data to a server, which will compute the number of 
#     lines, words, and characters in that file. The server will
#     return a formatted string containing the number of lines, words,
#     and characters in that file. The client then prints that returned
#     string to the standard ouput (terminal)
def main(file_name):
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connection to hostname on the port.
    client_socket.connect((host, port))

    # Open & Read File
    file = open(file_name, 'r')

    if(file.seek(0, os.SEEK_END)==0):
        #File is empty, don't need to process on server
        result = '\tLines: 0\n\tWords: 0\n\tCharacters: 0'
    else:
        #File isn't empty, read file contents
        file_data = file.read()
        # Send File Data to the server
        client_socket.send(file_data.encode('ascii'))
        # Receive the result string from the server
        result = client_socket.recv(size).decode('ascii')

    print(f'File: {file_name}\n{result}')

    file.close() #close the file object
    client_socket.close() #close connection to server

# Invoke main
if(__name__ == '__main__'):
    main(argv[1])
