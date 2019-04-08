import json
import termcolor

# Now we open the file and load the data

f = open("exercise_1.json", "r")

person_data = json.load(f)

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