'''

1. ECHO SERVER

Develop an Echo Server with forms. When you ask the server for the main page (/ resource) it should return a form with
a text input and a submit button. When a text message is sent to the echo server, it will generate a response html page
that contains the user message. With a link in the bottom it should be possible to return to the main form. The message
will be processed though the echo action.

'''

# First we import the required modules

import http.server
import socketserver
import termcolor

# Now we define the server's port
PORT = 8002

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        list_path = self.path

        # Now, we need to know which is the resource of the request and depending on it, we will perform different actions

        if self.path == '/':

            # Open the form1.html file
            f = open("form1.html", 'r')
            contents = f.read()

        # Now, if the request starts with /echo, which occurs when we submit a message, then the thing is different

        elif self.path.startswith("/echo"):

            # First we split the resource in such a way that we create a list with the message and the rest of the resource

            resource_list = self.path.split('=')
            request_msg = resource_list[1]
            symbol = '+'

            """I've noticed that when you send a message with more than one word, the message appears so that different 
            words are separated by '+' symbols. Let's fix that."""

            if symbol in request_msg: # This is, if the symbol is in the message
                request_2 =request_msg.split('+') # We create a list with the different words of the message
                request_msg = ' '.join(request_2) # We finally join them separated by commas

            """ The response contents will be an html which shows the message we have submitted"""

            contents = """
           <!DOCTYPE html>
            <html lang="en" dir="ltr">
              <head>
                <meta charset="utf-8">
                <title>ECHO PAGE</title>
              </head>
              <body style="background-color: lightyellow;">
                <h1>ECHO PAGE</h1>
                <p> {} </p>
                <p><a href="http://localhost:8002/"> Click here to go to the home page</a></p>
              </body>
            </html>""".format(request_msg)

        # If the resource is not '/' or '/echo/ then it redirects us to an error html

        else:
            f = open('error.html', 'r')
            contents =f.read()
            f.close()

        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")