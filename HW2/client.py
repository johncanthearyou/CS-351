import socket
from sys import argv
from time import sleep

# This function will create a socket and send a file name and its associated data
#   to a server, which will compute the number of lines, words, and characters in
#   that file. The server will return a formatted string containing the number of lines, 
#   words, and characters in that file. The client then prints that returned
#   string to the standard ouput (terminal)
def main():
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Hardcode Server IP address
    host = ''
    port = 4455

    # connection to hostname on the port.
    client_socket.connect((host, port))

    # Open & Read File
    file_name = argv[1]
    file = open(file_name, 'r')
    file_data = file.read()

    # Send File Data to the server
    client_socket.send(file_data.encode('ascii'))

    message = client_socket.recv(4096).decode('ascii')
    print(f'File: {file_name}\n{message}')

    file.close()
    client_socket.close()

# Invoke main
if(__name__ == '__main__'):
    main()
