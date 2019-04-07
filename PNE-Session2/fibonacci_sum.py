# A fibonacci series is a series such that every number is the sum of the two proceding ones.

our_number = int(input('Enter a number to proceed: '))

def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b

sum = 0

for i in range(our_number + 1):
    fibo = fib(i)
    sum = sum + fib(i)
print(sum)


