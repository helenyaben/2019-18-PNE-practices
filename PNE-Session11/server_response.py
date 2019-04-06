'''

HTTTP RESPONSES

1. STATUS LINE

The start line of an HTTP response, called the status line, contains the following information:
1. The protocol version, usually HTTP/1.1.
2. A status code, indicating success or failure of the request. Common status codes are 200 (200 OK: the status response
has succeeded, 404 (404 Not Found client error response code indicates that the server can't find the requested resource),
or 302 (302 Found redirect status response code indicates that the resource requested has been temporarily moved to the
URL given by the Location header.
3. A status text. A brief, purely informational, textual description of the status code to help a human understand the
HTTP message.

Example: HTTP/1.1 404 Not Found.

2. HEADERS

The header should contain at least two elements:
1. Content-Type: This is for indicating the type of content return by the server. It will be typically text/html
(but can also be image/png in the case of sending back an image in png format).
2. Content-Length: It indicates the total length of the information sent in the body of the response.

3. BODY

It contains the contents we're sending to the browser. The last part of a response is the body. Not all responses have
one.

In our server we will generate a simple response, which contents are the string: "Hello from my first server!"

http://192.168.0.195:8089/

'''

import socket
import termcolor

IP = "192.168.0.195"
PORT = 8090
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    # Build the HTTP response message. It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    contents = "Hello from my first server!"

    # -- Everything is OK
    status_line = "HTTP/1.1 200 OK\r\n"

    # -- Build the header
    header = "Content-Type: text/plain\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(contents)))

    # -- Build the message by joining together all the parts
    response_msg = str.encode(status_line + header + "\r\n" + contents)
    cs.send(response_msg)

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)

# noinspection PyUnreachableCode
'''
We can see that we've received two request messages:

FIRST REQUEST:

GET / HTTP/1.1
Host: 192.168.0.195:8090
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15
Accept-Language: es-es
Accept-Encoding: gzip, deflate
Connection: keep-alive

The first line is the request line, the most important part. We can ignore the rest of the message. Our request line is this one:

GET  / HTTP/1.1

It has three parts:
(1) The method: This first word is called the method. It indicates the operation that the client needs. In this case is a GET method. 
It means that the client wants to have access to some resource.
(2) The resource: The second word is the resource. The meaning of the "/" resource is: "I want to have access to your main page".
(2) The HTTP version that is being used.

In our case, the browser wants to get our main page with the first request.

SECOND REQUEST:

GET /favicon.ico HTTP/1.1
Host: 192.168.0.195:8090
Connection: keep-alive
Accept: */*
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15
Accept-Language: es-es
Referer: http://192.168.0.195:8090/
Accept-Encoding: gzip, deflate

The request line is:

GET /favicon.ico HTTP/1.1

The server is asking for the resource /favicon.ico. The favicon is a short image file that stores the icon of the webpage 
you are accessing. We are ignoring this request.

A favicon (short for favorite icon), also known as a shortcut icon, website icon, tab icon, URL icon, or 
bookmark icon, is a file containing one or more small icons,associated with a particular website or web page.

'''