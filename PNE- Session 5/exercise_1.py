# We are gonna find a DNA sequence, measure its length and count the basis.

seq = input('Enter a valid sequence to proceed: ')

def count_basis(seq):

    seq = seq.upper()

    len_seq = len(seq)

    count_a = 0
    count_t = 0
    count_c = 0
    count_u = 0
    count_g = 0

    for i in range(len(seq)):
        if seq[i] == "A":
            count_a += 1
        elif seq[i] == "T":
            count_t += 1
        elif seq[i] == "C":
            count_c += 1
        elif seq[i] == "U":
            count_u += 1
        elif seq[i] == "G":
            count_g += 1

    percentage_a = round(float(count_a)/len_seq*100, 1)
    percentage_g = round(float(count_g)/len_seq*100, 1)
    percentage_t = round(float(count_t)/len_seq*100, 1)
    percentage_c = round(float(count_c)/len_seq*100, 1)
    percentage_u = round(float(count_u)/len_seq*100, 1)

    print('Base A:')
    print('Counter: {}'.format(count_a))
    print('Percentage: {} %'.format(percentage_a))
    print('Base G:')
    print('Counter: {}'.format(count_g))
    print('Percentage: {} %'.format(percentage_g))
    print('Base T:')
    print('Counter: {}'.format(count_t))
    print('Percentage: {} %'.format(percentage_t))
    print('Base C:')
    print('Counter: {}'.format(count_c))
    print('Percentage: {} %'.format(percentage_c))
    print('Base U:')
    print('Counter: {}'.format(count_u))
    print('Percentage: {} %'.format(percentage_u))


print('Sequence is {} basis length'.format(len(seq)))
count_basis(seq)







