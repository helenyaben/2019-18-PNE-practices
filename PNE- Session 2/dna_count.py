# We are gonna find a DNA sequence, measure its length and count the basis.

seq = input('Enter a valid sequence to proceed: ')

seq = seq.upper()

len_seq = len(seq)

print('The length of the seq is : ', len_seq)

print('The number of adenine nucleotides is: ', seq.count('A'))
print('The number of guanine nucleotides is :', seq.count('G'))
print('The number of thymine nucleotides is:  ', seq.count('T'))
print('The number of cytosine nucleotides is: ', seq.count('C'))
print('The number of uracile nucleotides is: ', seq.count('U'))
