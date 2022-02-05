Author: John Stockton
Class: CS-351
Insructor: Dr. Wang
Term: Winter 2022

The HW2 assignment contains two files: server.py and client.py. They work in conjunction
    in order to determine the number of lines, words, and characters in a given file.
    While the server program is running:
        1. The client will send the file in question to the server program.
        2. The server will then process the received file and return a formatted string
           containing the result of the processing.
        3. the client will print the final result to the standard output (terminal).
    The server program will only terminate upon explicit termination from the user (ctrl+c).

To run server.py use this command in the terminal:
    `python server.py` OR `python3 server.py`

Once server.py is running, it will print the IP address and port number
    on which it is listening. In order to run client.py you MUST copy this
    IP address (without the port number) and paste it into the string defined on line #11 of client.py. 

To run client server.py use this command in the terminal:
    `python client.py <exampleFileName>` OR `python3 client.py <exampleFileName>`
    Where <exampleFileName> is a placeholder for the file you would like 
    to process on the server