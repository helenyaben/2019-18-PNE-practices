'''
1. CREATING A SIMPLE CLIENT SOCKET

We make a socket instance and passed it two parameters. The first parameter is AF_INET and the second one is
SOCK_STREAM. AF_INET refers to the address family ipv4. The SOCK_STREAM means connection oriented TCP protocol.

Now we have succesfully created a socket, which is a channel of connection between two endpoints (client and a server
in most of the cases).

The server provides the client information that is been requested by the last one. When we open a website we're opening
a socket and we're accessing the port of the server. Websites use to have port 80 open and this port is used to transform
HTTP data.

When we create a client socket we are kind of reading the server information, like the file reading object we saw.

If we want to communicate with a remote server:

'''

import socket

# SERVER IP, PORT
IP = "192.168.0.195" # We put the IP of our computer and run the client and the server sockets parallel in two different terminals.
PORT = 8081

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

mssg = str.encode(input('Enter the message you want to send: '))
s.sendall(mssg)

msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER:\n")
print(msg)

while True: # We have modified the function so it can work within a loop
    mssg_2 = str.encode(input('Enter the message you want to send: '))
    s.send(mssg_2)
    if mssg_2 == 'stop':
        guessing = False







