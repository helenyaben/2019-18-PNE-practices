'''

This is going to be a server which prints the messages from the client in green color

'''

# We installed the termcolor in the mac terminal using sudo pip3 install termcolor

import termcolor


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

    if msg == "EXIT":

        cs.send(str.encode("Server finished"))

        cs.close()

        return False

    # Print the received message in green color
    termcolor.cprint("Request message: {}".format(msg), 'green')

    # Send the msg back to the client (echo)

    cs.send(str.encode(msg))

    cs.close()

    return True

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

server = True

while server:

    # accept connections from outside
    # The server is waiting for connections

    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client

    # Service the client
    if process_client(clientsocket): # This is going to remain True if the message is not EXIT

        print("Attending connections from client: {}".format(address))

    else: # This is, in case it's false
        server = False
