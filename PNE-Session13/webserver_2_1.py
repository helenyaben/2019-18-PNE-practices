'''

IMPLEMENTING OUR OWN HANDLER

Let's define our own Handler for attending the clients.

WEB SERVER 2_1: Detecting GET requests

This example just prints a message on the console telling us that we have received a GET request message

'''


import http.server
import socketserver

# Define the Server's port
PORT = 8002


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # We just print a message
        print("GET received!")

        # IN this simple server version:
        # We are NOT processing the client's request
        # We are NOT generating any response message
        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")


'''

We should create a Class derived from the http.server.BaseHTTPRequestHandler base Class. For attending the GET request 
message, we should implement the do_GET method. This method will be called whenever there is a GET request from the client. 
In this example we are just printing a message on the console

Notice that we are not processing the client requests. And we are not generating any response message. For the later 
reason the browser will show us an error message.

We have also improved how the server is stopped: whenever the control-c is detected (or the server is stopped within pycharm) 
the server_close() method is called and a message is printed on the script

In our console there should appear the message: GET received! (many times, because as the browser is not getting any 
response from the server, it is sending the request message many times).


'''