'''

Example 3: ARRAY OF OBJECTS

The objects defined with curly brackets can also be elements in an array. Let's modify our previous example for including
additional information on the type of phone number. Now, the phone number will have two attributes: the number and the type.

'''

import json
import termcolor

# Now we open the file

f = open('person_3.json', 'r')

person = json.load(f)

# Print the information in the object
print()
termcolor.cprint("Name: ", 'green', end="")
print(person['Firstname'], person['Lastname'])

termcolor.cprint("Age: ", 'green', end="")
print(person['age'])

# Get the phoneNumber list
phoneNumbers = person['phoneNumber']


# Print the number of elements int the list
termcolor.cprint("Phone numbers: ", 'green', end='')
print(len(phoneNumbers))

# Print all the numbers
for i, num in enumerate(phoneNumbers):
    termcolor.cprint("  Phone {}:".format(i), 'blue')

    # The element num contains 2 fields: number and type
    termcolor.cprint("    Type: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("    Number: ", 'red', end='')
    print(num['number'])