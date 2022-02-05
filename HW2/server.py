import socket
import os

# get local machine name
host = socket.gethostname()
port = 4455
size = 4096
file_name = 'tmpfile'

# Function get_wc takes a file object and computes the number of lines,
#     words, and characters within that file
# Inputs: File, the file object to be processed for the counts
# Outputs: str, a formatted message giving the number of lines,
#              words, and characters of a given file
def get_wc(file):
    lines = 0
    words = 0
    chars = 0

    for line in file:
        lines += 1
        words += len(line.split())
        chars += len(line)

    return f'\tLines: {lines}\n\tWords: {words} \n\tCharacters: {chars}'

# This function creates a socket and listens for incoming requests
#     until the program is terminated
# Upon Client Connection:
#   1. A client will connect and send this server a file's content
#   2. This server will count the number of lines, words, 
#      and characters the the received file
#   3. This server will send a formatted string to the client of the
#      number of lines, words, and characters and close the connection
#      to the client
def main():
    # create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind server to the IP:Port address
    server_socket.bind((host, port))
    server_socket.listen()
    print(f'Ready to serve at> {host}:{port}')

    while True:
        # Accept incoming connection
        client_socket, addr = server_socket.accept()
        print(f'Got a connection from {addr}')

        # Get file data
        file_data = client_socket.recv(size).decode()
        print('\tReceived File Data\n')

        # Create file and write received data to it
        file = open(file_name, 'w+')
        file.write(file_data)
        file.seek(0)

        # Process file data, send result to client
        msg = get_wc(file).encode('ascii')
        client_socket.send(msg)

        # Delete file from the directory
        file.close()
        os.remove(file_name)

        # Close connection to this client
        client_socket.close()

# Invoke main
if(__name__ == '__main__'):
    main()
