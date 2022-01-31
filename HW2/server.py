import socket                                         

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           
port = 9999                                           

# bind to the port
serversocket.bind((host, port))
print("Ready to serve at> %s:%s" % (host, port) )                               

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()      

   print("Got a connection from %s" % str(addr))
    
   #TODO: Get File

   #TODO: Parse file for number of lines, words, & character
   num_lines = 1
   num_words = 2
   num_chars = 3
   msg = format("Lines: %d\nWords: %d\nCharacters: %d" 
                    % (num_lines, num_words, num_chars))

   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()