def sum(n):
    num = 0
    sum = 0
    while num <= n:
        sum = sum + num
        print(sum)
        num += 1

therm = int(input('Enter a valid number to proceed: '))

sum(therm)