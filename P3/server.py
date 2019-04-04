# First we import the seq class were we have the methods for the calculations the server is going to provide the client


from Seq_class import Seq


# First, we introduce the socket module

import socket

# Now we specify the port, IP address of the server, and the maximum clients we want to accept in the queue

PORT = 8086
IP = "192.168.0.195"
MAX_OPEN_REQUESTS = 5

# Now we're going to create a function that processes all the clients

def process_client(cs):

    """Process the client request. Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    first_msg = cs.recv(2048).decode("utf-8")

    # Now we need to convert the message into a list
    msg = first_msg.split('\n')

    # We create this variable in order to check if the sequence is valid
    valid_sequence ='ACTG'

    # If the first line is empty, the server will respond with an 'alive' message
    if msg[0] == '':

        mood = 'Alive'

        cs.send(str.encode(mood))

    # Let's going to define what the server is supposed to do in case the first line is not empty
    else:

        check = True # We create a boolean variable called 'check' which is True, and it will transform into False if the sequence is not correct
        # Now for each element of the sequence, this is, for each letter, we check if it's in the variable we've just created with all the possible letters
        for i in msg[0]:

            if i in valid_sequence: # As we go from one letter to another, the program checks it
                continue

            else:
                cs.send(str.encode('Error'))
                # If the basis is not valid, the server sends an 'Error' message and the for loop breaks
                check = False
                break

        if check == True:

            sequence = msg[0] # Now we create a variable called 'sequence' which contains the sequence to analyze

            first_line = 'OK' # The teacher asked us to response an 'OK' as the first line if the sequence is okay so we create this variable since at this point, the sequence has passed the 'ITV'

            empty_list =[] # We create an empty list that we will later convert into the message we are going to send and we add the first line 'OK'

            empty_list.append(first_line)

            sequence = Seq(sequence) # We create the sequence instance

            for i in msg[1:]: # In order to simplify our calculations we get rid of the sequence in our 'received message' list

                if i == 'len':
                    empty_list.append(str(sequence.len()))

                elif i == 'complement':
                   empty_list.append(sequence.complement())

                elif i == 'reverse':
                   empty_list.append(sequence.reverse())

                elif i == 'counta':
                    empty_list.append(str(sequence.count('A')))

                elif i =='countg':
                    empty_list.append(str(sequence.count('G')))

                elif i =='countc':
                    empty_list.append(str(sequence.count('C')))

                elif i =='countt':
                    empty_list.append(str(sequence.count('T')))

                elif i =='perca':
                    empty_list.append(str(sequence.perc('A')))

                elif i =='percg':
                    empty_list.append(str(sequence.perc('G')))

                elif i =='percc':
                    empty_list.append(str(sequence.perc('C')))

                elif i =='perct':
                    empty_list.append(str(sequence.perc('T')))

                elif i =='exit':

                    cs.send(str.encode('Server finished'))
                    cs.close()
                    return False

                else:
                    empty_list.append(str('Enter a valid calculation next time'))

            send_msg = '\n'.join(empty_list) # Now we create the message from the list we've been creating from the calculations
            cs.send(str.encode(send_msg))

    cs.close()
    return True

# Now we define our socket in the MAIN PROGRAM

# First, we create an INET, STREAMing socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now we bind the socket with the IP and Port

serversocket.bind((IP, PORT))

# Notice always the double parenthesis since it's accepting a tuple

# Now we're going to define how many connections we want to have in our queue before refusing new clients with the listen() function

serversocket.listen(MAX_OPEN_REQUESTS)

# Now we're goint to print a message that tell us that the socket is ready

print("Socket ready: {}".format(serversocket))

# Here we make a loop in order to accept the clients

server = True

while server:

    # accept connections from outside
    # The server is waiting for connections

    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client

    # Service the client
    if process_client(clientsocket): # This is going to remain True if the message is not EXIT

        print("Attending connections from client: {}".format(address))

    else: # This is, in case it's false
        server = False
