
import socket



# First we are going to define our seq_class

class Seq():

    # Here we're going to define the instance variables with the __init__method


    def __init__(self, strbases):

        self.strbases = strbases.upper()

    # Now we're going to define a regular method which gives us the length of our sequence

    def len(self):
        return len(self.strbases)

    def complement(self):

        # First, we're going to create a list from our sequence

        new_sequence = list(self.strbases)

        # Now we're going to replace the elements in the list

        for number, value in enumerate(new_sequence):

            if value == 'A':
                new_sequence[number] = 'G'
            elif value == 'G':
                new_sequence[number] = 'A'
            elif value == 'C':
                new_sequence[number] = 'T'
            elif value == 'T':
                new_sequence[number] = 'C'

        empty_string = ''

        for element in new_sequence:
            empty_string = empty_string + element

        return empty_string

    # Now we're going to create a method that gives us the reverse of the sequence

    def reverse(self):
        return self.strbases[::-1]

    # Now we're going to create a method that gives us the number of occurences of the basis.

    def count(self, base):

        len_seq = len(self.strbases)

        count_basis = 0

        for i in range(len_seq):
            if self.strbases[i] == base:
                count_basis += 1

        return '{} {} {}'.format(base, ':', count_basis)

    # Now we're going to create a method that gives us the percentage of the basis.

    def perc(self, base):

        len_seq = len(self.strbases)

        count_basis = 0

        for i in range(len_seq):
            if self.strbases[i] == base:
                count_basis += 1

        percentage_basis = round(float(count_basis) / len_seq * 100, 1)

        return '{} {} {} {}'.format(base,':', percentage_basis, '%')




# Configure the Server's IP and PORT
PORT = 8081
IP = "192.168.1.36"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client while the connection remains

        msg = clientsocket.recv(2048).decode("utf-8")

        print("Message from client: {}".format(msg))

        # Now we're going to send a message to the client, which will be the complement of the recieved sequence.

        server_seq = Seq(msg)
        output_seq = Seq(server_seq.complement())

        sequence = output_seq.strbases

        message = sequence

        send_bytes = str.encode(message)

        # We must write bytes, not a string
        clientsocket.send(send_bytes)

        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
