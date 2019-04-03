'''

CLIENT BLOCKING THE SERVER

Try the following client. It connects to the server, ask the user to enter a message, send the message to the server,
read the server's response (the echo) and repeat it again.

'''

import socket

# SERVER IP, PORT
IP = "192.168.0.195"
PORT = 8086


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # The client is blocking the server....  NOT A GOOD DESIGN!!!
    msg = input("> ")

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()

# noinspection PyUnreachableCode
'''
The client is not well design. It is blocking the server while the user is entering the message... that should be avoided. 
This is a better solution: FILE solution-client.py
'''