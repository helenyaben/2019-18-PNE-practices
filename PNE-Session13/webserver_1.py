'''

As we said, to create a web server, we need to import two modules: http.server and socketserver.


'''

import http.server
import socketserver

# Define the Server's port
PORT = 8000


'''
A web server needs to be told how to handle incoming requests.

These incoming requests are handled by special handlers. You can think of a web server as a dispatcher, a request comes 
in, the http server inspects the request and dispatches it to a designated handler. Of course these handlers can do 
anything you desire.

But what do you think the most basic handler is? Well, that would be a handler that just serves a static file.
In other words, when I go to yahoo.com, the web server at the other end sends back a static html file. This is in fact 
what we are exactly trying to do.
And that is what the http.server.SimpleHTTPRequestHandler is: a simple HTTP request handler that serves files from the 
current directory and any of its subdirectories.

'''


# -- Use the http.server Handler
Handler = http.server.SimpleHTTPRequestHandler


'''

Now let’s talk about the socketserver.TCPServer class. An instance of TCPServer describes a server that uses the TCP 
protocol to send and receive messages (http is an application layer protocol on top of TCP).

To instantiate a TCP Server, we need two things:

1- The TCP address (IP address and a port number).

2- The handler.

As you can see, the TCP address is passed as a tuple of (ip address, port number)

Passing an empty string as the ip address means that the server will be listening on any network interface (all available 
IP addresses).

And since PORT stores the value of 8000, then the server will be listening on incoming requests on that port.

Well, how about serve_forever?

serve_forever is a method on the TCPServer instance that starts the server and begins listening and responding to
incoming requests. It makes the server waits until a client is connected. When it happens, the handler function is called.

By default the SimpleHTTPRequestHandler will look for a file named index.html in the current directory.

'''


# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    httpd.serve_forever()

'''

If we run it in the terminal, we have an HTTP server that is listening on any interface at port 8080 waiting for 
incoming http requests.

What is localhost?

In computer networking talk, localhost refers to "this computer" or even more accurately "the computer I'm working on."
In fact you can totally replace localhost with the IP of your computer in your browser and you would still get the same result.

'''