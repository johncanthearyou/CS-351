import socket
from subprocess import check_output

def get_wc(file_name):
    return check_output(["wc", "-l", file_name])

# create a socket object
server_socket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           
port = 9999                                           

# bind to the port
server_socket.bind((host, port))
print("Ready to serve at> %s:%s" % (host, port) )                               

# queue up to 5 requests
server_socket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = server_socket.accept()      

    print("Got a connection from %s" % str(addr))

    #Get File Name & Data
    file_name = server_socket.recv(1024)
    file_data = server_socket.recv(1024)

    #Open file and write received data to it
    file = open(file_name, "w")
    file.write(file_data)
    file.close

    msg = get_wc( file_name )
    clientsocket.send(msg.encode())

    clientsocket.close()