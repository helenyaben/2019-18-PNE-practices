'''

Example 2: ARRAYS

The JSON format let us define arrays of elements, stored in order. The first element is 0, the second 1, and so on. The
arrays are created using the brackets [].

Let's change the person.json file for adding a new attribute called phoneNumber that is an array of the phone numbers of
that person.

The phone number 0 is "1111" and the phone number 1 is "2222". Let's change our program for printing the new information.
The variable phoneNumbers contains the list of phone numbers. Using a for loop we read all the phone numbers and print
them on the console.

'''

import json
import termcolor

# Open de json file

f = open('person.json', 'r')

person = json.load(f)

print()
termcolor.cprint("Name: ", 'green', end="") # By default, the print function ends with a new line, here we specify we want it to end with a blackspace
print(person["Firstname"], person["Lastname"])

termcolor.cprint("Age: ", 'green', end="")
print(person['age'])

for i in range(len(person["phoneNumber"])):
    printing = 'phoneNumber' + " " + str(i) + ":"
    termcolor.cprint(printing, 'green', end = " ")
    termcolor.cprint(person['phoneNumber'][i], 'blue')