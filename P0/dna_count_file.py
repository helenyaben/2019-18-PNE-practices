f = open('dna.txt', 'r')

seq = f.read()

seq = seq.replace(' ', '').replace('\n', '').replace('\r', '')

print('The sequence we are going to analize is: ', seq)

sorted_list = set(list(seq))

print('The total number of basis is: ', len(seq))

print('The number of different basis is : ', len(sorted_list))

f.close()