'''

EXERCISE 2:

Modify the server for returning the json file created on the Exercise 1, with the information of 3 people.
Modify the client for printing the information of all the people received

'''


# -- Example of a client that uses the HTTP.client library
# -- for requesting a JSON object and printing their
# -- contents
import http.client
import json
import termcolor

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

# -- Create a variable with the data,
# -- form the JSON received

print("CONTENT: ")

person_data = json.loads(data1)

print()

for element in person_data:

    #Name
    termcolor.cprint("Name: ", "green", end=' ')
    print(person_data[element][0]["Firstname"], person_data[element][0]["Lastname"])

    #Age
    termcolor.cprint("Age: ", "green", end=' ')
    print(person_data[element][0]["age"])

    #Phones
    termcolor.cprint("Phone numbers: ", "green", end=' ')

    phoneNumbers = person_data[element][0]["phoneNumber"]

    print(len(phoneNumbers))

    for num, phone in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {} : ".format(num + 1), "green")
        termcolor.cprint("      Type: ", "blue", end=' ')
        termcolor.cprint(phoneNumbers[num]["type"], "yellow")
        termcolor.cprint("      Number: ", "blue", end=' ')
        termcolor.cprint(phoneNumbers[num]["number"], "yellow")

    print()

