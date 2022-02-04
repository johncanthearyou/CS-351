import socket

def get_wc(file_contents):
    lines = 0
    words = 0
    chars = 0
    first_iter = True
    for char in file_contents:
        if(char == '\n' or char == ' ' or char == '\t'):
            if(char == '\n'):
                lines += 1
            words += 1
        chars += 1

    return f'File: {file_name}\n\tLines:{lines}\n\tWords:{words} \n\tCharacters:{chars}'


# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 4455

# Bind server to the IP:Port address
server_socket.bind((host, port))
server_socket.listen()
print('Ready to serve at> %s:%s' % (host, port))

while True:
    # Accept incoming connection
    client_socket, addr = server_socket.accept()
    print('Got a connection from %s' % str(addr))

    # Get File Name & Data
    file_name = client_socket.recv(4096).decode()
    print('\tGot File Name: %s' % file_name)
    file_data = client_socket.recv(4096).decode()
    print('\tReceived File Data\n')

    # Open file and write received data to it
    file = open(file_name, 'w')
    file.write(file_data)
    file.close

    # Process file data, send result to client
    msg = get_wc(file_data).encode('ascii')
    client_socket.send(msg)

    # Close connection to this client
    client_socket.close()
