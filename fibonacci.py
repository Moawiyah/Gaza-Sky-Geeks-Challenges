# Fibonacci challenge
# Challenge: A Fibonacci Sequence is created by adding two numbers to create the next number in the sequence.
# You then sum that number with the one preceding it to get the next number, and so on.
# For example, if you have the sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, then the next number in the sequence is 55.

fib = []

num1 = int(input('Please input the first number: '))
num2 = int(input('Please input the second number: '))

fib.append(num1)
fib.append(num2)

n = int(input('Enter number of elements: '))

for i in range(0, n):
    X = fib[len(fib)-1] + fib[len(fib)-2]
    fib.append(X)

print(fib)
