'''

ECHO CLIENT

'''

# First of all, we import the socket module

import socket

# Now we define the IP and the PORT of the SERVER

PORT = 8086
IP = "192.168.0.195"

# Here we create the client socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT)) # Notice that we use different socket module functions for clients and servers

# Now we define the message we want to send

msg = 'Hello'

# Send the request message to the server
s.send(str.encode(msg))

# Now we define the response message

# Receive the servers respoinse
response = s.recv(2048).decode()

# Print the server's response
print("Response: {}".format(response))

s.close()

