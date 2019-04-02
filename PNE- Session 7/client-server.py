'''

CLIENT-SERVER (SOCKET PROGRAMMING)

In computing, a server is a computer program or a device that provides functionality for other programs or devices,
called "clients".

Servers can provide various functionalities, often called "services", such as sharing data or resources among multiple
clients, or performing computation for a client. A single server can serve multiple clients, and a single client can use
multiple servers.

Client–server systems are today most frequently implemented by (and often identified with) the request–response model:
a client sends a request to the server, which performs some action and sends a response back to the client, typically
with a result or acknowledgement.

Client and servers can be in the same computer (we will do it for developing our clients and server from our computer,
without having to use two different computers. Which is good, because you will be able to test your projects from your home)

Sockets (aka socket programming) enable programs to send and receive data, bi-directionally, at any given moment.
This tutorial walks through how you can send data from device-to-device, client-to-server, and vice versa using socket
programming in Python.

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens
on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener
socket while client reaches out to the server.

But first, what is 'IP'?

An Internet Protocol address (IP address) is a numerical label assigned to each device connected to a computer network
that uses the Internet Protocol for communication.
An IP address serves two principal functions: host or network interface identification and location addressing.

And what is a port?

If you could consider all the addresses a computer processor could talk to as the address space, then certain addresses
will have specialized purposes. For example, an address could be a memory address or another address could be a port address.
A port address could be used to talk to external processes or devices. A port then, is simply a hole in the processor address
space where data can be sent and received from.

Any networking process or device uses a specific network port to transmit and receive data. This means that it listens
for incoming packets whose destination port matches that port number, and/or transmits outgoing packets whose source port
is set to that port number. Processes may use multiple network ports to receive and send data.

What is the ping command?

The ping command (in the terminal): The ping command is a Command Prompt command used to test the ability of the source
computer to reach a specified destination computer. The ping command is usually used as a simple way to verify that a
computer can communicate over the network with another computer or network device.

In the terminal of this mac we write either:
(1) ping IPaddress
(2) ping url

1. INTRODUCTION TO THE PROGRAMMING OF CLIENTS

We will learn the basic ideas used for communicating a client an a server thought internet. The communicating model is
very similar to the already know model of reading and writing local files in your computer.

2. SOCKETS

For communicating with a program that is running in another computer we used the socket concept. Instead of opening a
local file, it opens a "channel" for communicating with the other programs. The socket is an object, and as such, it has
properties and methods for managing that channel.

Sockets are defined by the IP address, the listening port and the protocols inside it.

The functions required to work with sockets are inside the socket module:
(1) Server socket methods:
-s.bind() ----> This method binds address (hostname, port number pair) to socket.
-s.listen() ----> This method sets up and start TCP listener.
-s.accept() ---->This passively accept TCP client connection, waiting until connection arrives (blocking).
(2) Client socket methods:
-s.connect() ----> This method actively initiates TCP server connection.
(3) General socket methods:
-s.recv()

This method receives TCP message
-s.send() ----> This method transmits TCP message
-s.recvfrom() ----> This method receives UDP message
-s.sendto() ----> This method transmits UDP message
-s.close() ----> This method closes socket
-socket.gethostname() -----> Returns the hostname.

'''







