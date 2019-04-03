'''

As we said, Sockets and the socket API are used to send messages across a network. They provide a form of inter-process
communication (IPC). The network can be a logical, local network to the computer, or one that’s physically connected to
an external network, with its own connections to other networks. The obvious example is the Internet, which you connect
to via your ISP.

The servers initially create one socket, bound to the IP and the PORT where the clients should connect.

They wait, until a client connects.
In our examples: the server only can attend one client at a time.
Once the client is connected, a new socket is created: this sockets allows the server to communicate with the client.
The server reads the request message, process it and generates the response.
Then it waits for the next client.
The clients are queued.

We're going to configure our first server socket.


https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg

Starting in the top left-hand column, note the API calls the server makes to setup a “listening” socket:

-socket()
-bind()
-listen()
-accept()

A listening socket does just what it sounds like. It listens for connections from clients. When a client connects,
the server calls accept() to accept, or complete, the connection.

The client calls connect() to establish a connection to the server and initiate the three-way handshake. The handshake
step is important since it ensures that each side of the connection is reachable in the network, in other words that the
client can reach the server and vice-versa. It may be that only one host, client or server, can reach the other.

In the middle is the round-trip section, where data is exchanged between the client and server using calls to send()
and recv().

At the bottom, the client and server close() their respective sockets.


'''

import socket # First, we import our socket module

PORT = 8086
IP = "192.168.0.195"
MAX_OPEN_REQUESTS = 5

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets

'''

Enable a server to accept connections. If backlog is specified, it must be at least 0 (if it is lower, it is set to 0); 
it specifies the number of unaccepted connections that the system will allow before refusing new connections. If not 
specified, a default reasonable value is chosen.

'''

# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

'''
Once the server is configured, we use the socket's accept() method for waiting for a client to communicate. Once the 
client is connected, a new socket is created (clientsocket). This new socket is bound to another port. And it is only use 
for communicating exclusively with that client.

'''

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # This server do nothing. The new socket is closed
    clientsocket.close()


