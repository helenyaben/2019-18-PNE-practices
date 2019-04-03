'''

We're going to create a simple client shocket to connect it to the server we've just created.

'''

import socket

# SERVER IP, PORT
IP = "192.168.0.195"
PORT = 8086

# Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Close the socket
s.close()

