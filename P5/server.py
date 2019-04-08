'''

This is going to be a server that has the same function as the server of practice 4 but we'll do it with the
htt.server module.

'''

# First of all, we import the modules we're going to use

import termcolor
import socketserver
import http.server

# We first define the port through which we are going to receive the connections

PORT = 8002

'''

Now we define a subclass from the class http.server.BaseHTTPRequestHandler to define a new method of our handler.

As we know, the Handler is the element of our code that is going to 'handle' the new connections.

'''


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        """This method is called whenever the client invokes the GET method
                in the HTTP protocol request"""

        # First we are going to print some information of the request in our console (request line, command, and resource)

        print("GET received! Request line: ", termcolor.cprint("  " + self.requestline, 'green'))
        print("  Command: " + self.command)
        print("  Path: " + self.path)

        """ Now, with the self.path method we will see what resource is the browser introducing and
                  depending on the resource we will send one HTML file or another"""

        if self.path == '/':
            f = open('index.html', 'r') # This object opens the file
            contents = f.read() # This object reads the file
            f.close() # Close the file

        elif self.path == '/blue':
            f = open('blue.html', 'r')
            contents = f.read()
            f.close()

        elif self.path == '/pink':
            f = open('pink.html', 'r')
            contents = f.read()
            f.close()

        else: # If the resource is not /, or /blue or /pink then the opened file will be the error file
            f = open('error.html', 'r')
            contents = f.read()
            f.close()

        # Now we are going to compose the response message

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        self.wfile.write(str.encode(contents))

        return


# Now we define the Handler as the TestHandler

Handler = TestHandler

# Open the socket server

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()

    # If the user interrupts the program, the error does not arise but the program quits and it prints a message
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")


