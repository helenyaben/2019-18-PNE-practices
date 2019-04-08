'''

HTTP.client python library:

The python HTTP.client library allow us to implement python clients easily. This is an example of use. The client is
requesting the main page (/) from the server, and printing the data on the console.

'''

# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client

PORT = 8001
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

print("CONTENT: ")

# -- Print the received data
print(data1)