'''

ECHO SERVER

An echo server is usually an application which is used to test if the connection between a client and a server is successful.
It consists of a server which sends back whatever text the client sent.

We use the send() and recv() socket's method for communicating with the client.

Let's develop a server that just send back the request messages from the clients. This is called an echo server
(Because it echoed back all the received messsages).

The new socket is passed as an argument to the process_client() function, that is in charge of servicing the client.

'''


# First, we introduce the socket module

import socket

# Now we specify the port, IP address of the server, and the maximum clients we want to accept in the queue

PORT = 8086
IP = "192.168.0.195"
MAX_OPEN_REQUESTS = 5

# Now we're going to create a function that processes all the clients

def process_client(cs):

    """Process the client request. Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print("Request message: {}".format(msg))

    # Send the msg back to the client (echo)
    cs.send(str.encode(msg))

    # Close the socket
    cs.close()

# Now we define our socket in the MAIN PROGRAM

# First, we create an INET, STREAMing socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now we bind the socket with the IP and Port

serversocket.bind((IP, PORT))

# Notice always the double parenthesis since it's accepting a tuple

# Now we're going to define how many connections we want to have in our queue before refusing new clients with the listen() function

serversocket.listen(MAX_OPEN_REQUESTS)

# Now we're goint to print a message that tell us that the socket is ready

print("Socket ready: {}".format(serversocket))

# Here we make a loop in order to accept the clients

while True:

    # accept connections from outside
    # The server is waiting for connections

    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client

    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)