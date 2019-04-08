import requests, sys
from seq_class import Seq
import termcolor

# Here we have the code we got from the Api documents of emsembl

server = "http://rest.ensembl.org"
ext = "/sequence/id"
headers = {"Content-Type": "application/json", "Accept": "application/json"}
r = requests.post(server + ext, headers=headers, data='{ "ids" : ["ENSG00000165879"] }')

if not r.ok:
    r.raise_for_status()
    sys.exit()


seq_dict = r.json()

print()
termcolor.cprint("This is the FRAT1 gene analysis", "green")
print()

# We get our sequence from the dict we have obtained from the emsemble database
sequence = (seq_dict[0]["seq"])

# We make our instance in the Seq class
seq = Seq(sequence)

# Call method len() from Seq class
number_bases = seq.len()

# Call method count() from Seq class
t_bases = seq.count('T')

# Call method perc() from Seq class
t_perc = seq.perc('T')

termcolor.cprint("The number bases of T is ", 'blue', end="")
termcolor.cprint(t_bases, 'yellow')
termcolor.cprint("The percentage of bases of T is ", 'blue', end='')
termcolor.cprint(t_perc, 'yellow')


basis = ['A', 'C', 'G', 'T']

# Create an empty list
empty_list =[]

# We count the different bases and we add this counts to the empty list
for element in basis:
    counter = seq.count(element)
    empty_list.append(counter)

empty_list_1 = []

# We get a list of lists, in which each list is a list consisting of the basis and the counter of the basis
for i in empty_list:
    new_list = i.split(':')
    empty_list_1.append(new_list)

# New list with the counters only
empty_list_2 =[]
for element in empty_list_1:
    empty_list_2.append(element[1])

# If the maximum of our last new list is equal to the second element of each element of our list of lists empty_list_1, then we get the popular basis
for element in empty_list_1:
    if max(empty_list_2) == element[1]:
        termcolor.cprint("The most popular basis is: ", 'blue', end='')
        termcolor.cprint(element[0], 'yellow')
        base = element[0].strip()
        termcolor.cprint("The percentage of the most popular basis is ", 'blue', end='')
        termcolor.cprint(seq.perc(base), 'yellow')





