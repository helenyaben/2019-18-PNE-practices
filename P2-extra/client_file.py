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



# SERVER IP, PORT

IP = "192.168.0.195"
PORT = 8081

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)

s.connect((IP, PORT))

# We first ask the user to enter a valid sequence

seq = input('Enter a valid sequence to proceed: ')

# We now convert the sequence into an instance
instance_seq = Seq(seq)

# Transformation to complement sequence
comp_seq = Seq(instance_seq.complement())

# Transformation to reverse sequence
rever_seq = Seq(comp_seq.reverse())

mssg = str.encode(rever_seq.strbases)

s.send(mssg)

# Now we are going to receive the message from the server:

msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER:\n")
print(msg)
