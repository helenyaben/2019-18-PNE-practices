from Seq import Seq

seq_1 = input('Introduce a sequence 1: ')
seq_2= input('Introduce a sequence 2: ')

sequence_1 = Seq(seq_1)
sequence_2 = Seq(seq_2)

sequence_3 = Seq(sequence_1.complement())
sequence_4 = Seq(sequence_3.reverse())

print('Sequence 1: ', sequence_1.strbases)
print('\t Length:', sequence_1.len())
print('\t Bases count: ', sequence_1.perc('A'), sequence_1.perc('G'), sequence_1.perc('C'), sequence_1.perc('T'))

print('Sequence 2: ', sequence_2.strbases)
print('\t Length:', sequence_2.len())
print('\t Bases count: ', sequence_2.perc('A'), sequence_2.perc('G'), sequence_2.perc('C'), sequence_2.perc('T'))

print('Sequence 3: ', sequence_3.strbases)
print('\t Length:', sequence_3.len())
print('\t Bases count: ', sequence_3.perc('A'), sequence_3.perc('G'), sequence_3.perc('C'), sequence_3.perc('T'))

print('Sequence 4: ', sequence_4.strbases)
print('\t Length:', sequence_4.len())
print('\t Bases count: ', sequence_4.perc('A'), sequence_4.perc('G'), sequence_4.perc('C'), sequence_4.perc('T'))