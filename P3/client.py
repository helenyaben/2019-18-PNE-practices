import socket


# SERVER IP, PORT
IP = "192.168.0.195"
PORT = 8086

client = True # We create a while loop so the client keep asking the user for entering new values for new future connections once the server has finished the previous one

while client:

    # Here we have created a menu to inform the user about the program and to give her/him the instructions to be followed

    print('\nHi, you are about to connect with a server.')
    print('Please, follow the instructions.')
    print('\nINSTRUCTIONS\n')
    print('First, you will be asked for a sequence.')
    print('Second, you will be asked for the processes you want to be undertaken for the sequence. Remember to separate them by spaces. ')
    print('If you do not write anything, the server will send you if it is alive or not')

    print('\nThese are the possible processes:\n-len: to calculate the length of the sequence\n-complement: calculate the complement sequence\n-reverse : calculate the reverse sequence\n-countBASIS; count the number of basis\n-percBASIS: calculate the percentage of the basis \n exit: if you want to finish the server')

   # Once we've given the instructions, we ask the user if he/she wants to continue. Maybe the user does not want to continue after the first connection or maybe he is not interested.

    print('Do you want to continue?')
    print('(A) Yes')
    print('(B) No')

    ask =input('Choose between A or B: ')
    ask = ask.upper()

    # If the user wants to continue
    if ask == 'A':
        sequence = input('Please enter a valid DNA sequence to proceed: ')
        sequence = sequence.upper()
        sequence = ' '.join(sequence.split())

        process = input('Please enter the calculations you want to perform separated by spaces: ')
        process = process.lower()
        process = process.lower()
        process = ' '.join(process.split())

        process_list = process.split(" ")
        info = ','.join(process_list)

        print('These are the processes you have selected: ', info)

        msg_list = []
        msg_list.append(sequence)

        msg_list = msg_list + process_list

        msg = '\n'.join(msg_list)

    # If the user does not want to continue
    else:
        client = False # We make the boolean False and we break the loop
        break

    # Now we can create the socket and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()