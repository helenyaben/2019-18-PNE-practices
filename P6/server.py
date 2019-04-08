
import http.server
import socketserver
import termcolor

from seq_class import Seq

# Now we define the server's port
PORT = 8001

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Now, we need to know which is the resource of the request and depending on it, we will perform different actions

        if self.path == '/':

            # Open the form1.html file
            f = open("index.html", 'r')
            contents = f.read()

        # Now, if the request starts with /echo, which occurs when we submit a message, then the thing is different

        elif self.path.startswith("/echo"):

            path = self.path
            options_choosen = 'countperc'
            basis_choseen = 'basis'

            if options_choosen not in path or basis_choseen not in path:
                f = open('error.html', 'r')
                contents = f.read()
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

            # First we split the resource in such a way that we create a list with the message and the rest of the resource

            resource_list = self.path.split('&')

            for i in range(len(resource_list)):
                new_element = resource_list[i].split('=')
                resource_list[i] = new_element[1]
            print(resource_list)

            sequence = resource_list[0].upper()

            word_len = 'len'

            check_len = True

            if word_len in resource_list:

                operation = resource_list[2]
                operation = operation.lower()
                basis = resource_list[3]

            else:

                check_len = False
                operation = resource_list[1]
                basis = resource_list[2]

            print(operation)
            print(basis)
            print(sequence)

            # We're going to check if the sequence is valid
            valid_sequence = 'ACTG'

            check = True  # We create a boolean variable called 'check' which is True, and it will transform into False if the sequence is not correct
            # Now for each element of the sequence, this is, for each letter, we check if it's in the variable we've just created with all the possible letters

            for i in sequence:

                if i in valid_sequence:  # As we go from one letter to another, the program checks it
                    continue
                else:
                    check = False
                    break

            if check == True:

                seq_1 = Seq(sequence)

                sequence_basis = seq_1.strbases

                if operation == 'perc':
                    seq_operation = seq_1.perc(basis)

                elif operation =='count':
                    seq_operation = seq_1.count(basis)

                else:
                    seq_operation = 'You have not choosen any operation'

                if check_len == True:

                    seq_length = seq_1.len()
                    contents = """
                   <!DOCTYPE html>
                    <html lang="en" dir="ltr">
                      <head>
                        <meta charset="utf-8">
                        <title>RESULTS PAGE</title>
                      </head>
                      <body style="background-color: lightyellow;">
                        <h1>RESULTS PAGE</h1>
                        <p> Sequence: {} </p>
                        <p> Length of the sequence: {} </p>
                        <p> Operation {} on the base {} : </p>
                        <p> {} </>
                        <p><a href="http://localhost:8001/"> Click here to go to the home page</a></p>
                      </body>
                    </html>""".format(sequence_basis,seq_length, operation, basis, seq_operation)
                else:
                    contents = """
                   <!DOCTYPE html>
                    <html lang="en" dir="ltr">
                      <head>
                        <meta charset="utf-8">
                        <title>RESULTS PAGE</title>
                      </head>
                      <body style="background-color: lightyellow;">
                        <h1>RESULTS PAGE</h1>
                        <p> Sequence: {} </p>
                        <p> Operation {} on the base {} : </p>
                        <p> {} </>
                        <p><a href="http://localhost:8001/"> Click here to go to the home page</a></p>
                      </body>
                    </html>""".format(sequence_basis, operation, basis, seq_operation)
            else:
                contents = """
                <!DOCTYPE html>
                <html lang="en" dir="ltr">
                  <head>
                    <meta charset="utf-8">
                    <title>ERROR PAGE</title>
                  </head>
                  <body style="background-color: lightyellow;">
                    <h1>ERROR PAGE</h1>
                    <p> {} </p>
                    <p><a href="http://localhost:8001/"> Click here to go to the home page</a></p>
                  </body>
                </html>""".format('ERROR: The sequence is not valid')
# If the basis is not valid, the server sends an 'Error' message and the for loop breaks

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