
from Bases import count_basis

seq1 = input('Enter a valid sequence to proceed: ')

seq2 = input('Enter a second valid sequence to proceed: ')

print('')

print('Sequence 1 is {} basis length'.format(len(seq1)))
count_basis(seq1)

print('')

print('Sequence 2 is {} basis length'.format(len(seq2)))
count_basis(seq2)
