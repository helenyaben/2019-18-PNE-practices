
import http.server
import socketserver
import termcolor

PORT = 8002


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        print("GET received! Request line:")

        termcolor.cprint("  " + self.requestline, 'green')

        print("  Command: " + self.command)

        print("  Path: " + self.path)

        # Now, with the self.path function, we will see what is the resource of the request.

        if self.path == "/":
            f = open('index.html', 'r')
            content = f.read()
            f.close()

        else:
            print('Error: the introduced resource does not exist')

            '''
            The self.send_error(code) function sends the error response to the browser
            
            '''
            self.send_error(404)
            return

        # Now we elaborate the response:

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()


        self.wfile.write(str.encode(content))

        return

Handler = TestHandler

# -- Open the socket server
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


