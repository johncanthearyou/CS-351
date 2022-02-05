# John Stockton
# CS-351
# Dr. Wang
# Winter 2022

import socket
import os
from sys import argv

# Hardcode Server IP address
host = ''
port = 4455
size = 4096
encoding = 'utf-8'

def send_to_server(file):
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connection to hostname on the port.
    client_socket.connect((host, port))

    #Read file contents
    file_data = file.read()

    # Send File Data to the server
    client_socket.send(file_data.encode(encoding))

    # Receive the result string from the server
    result = client_socket.recv(size).decode(encoding)

    client_socket.close() #close connection to server

    return result

# This function will create a socket and send a file name and its 
#     associated data to a server, which will compute the number of 
#     lines, words, and characters in that file. The server will
#     return a formatted string containing the number of lines, words,
#     and characters in that file. The client then prints that returned
#     string to the standard ouput (terminal)
def main(file_name):
    file = open(file_name, 'r') #Open file

    if(file.seek(0, os.SEEK_END)==0):
        #File is empty, don't need to process on server
        result = '\tLines: 0\n\tWords: 0\n\tCharacters: 0'
    else:
        file.seek(0) #Go back to beggining of file
        result = send_to_server(file)

    file.close() #close the file object

    print(f'File: {file_name}\n{result}')

# Invoke main
if(__name__ == '__main__'):
    main(argv[1])
