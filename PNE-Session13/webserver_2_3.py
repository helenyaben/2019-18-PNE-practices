'''

WEBSERVER 2_3: Generating the response message

Now we will add a response message to our handler so that the browser will show some contents instead of an error message.
Our server will always send the same message, no matter what resources is the client requesting: is a happy server :-)


In this example we will print the following properties:

In our TestHandler Class we can use the following methods for generating the response very easily:

-self.send_response(code) : Creates a response header with a status line with the error CODE passed as an argument.
The response is not really sent yet, but stored into a buffer.

-self.send_header(): Add a header to the response message (Ex. Content-Type, Content-Length...).

-self.end_headers(): Add a blank line to the response message (indicating that the header is finished).

The message body is sent using the self.wfile.write() method.


'''

import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8000


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        # Message to send back to the clinet
        contents = "I am the happy server! :-)"

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

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
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")


