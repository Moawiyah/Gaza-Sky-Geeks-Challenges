# Missing Number Game
# Challenge: Create a program that takes a series of numbers and examines it to find the numbers missing to make it a perfect range.
# For example, the series of numbers could be [2, 1, 5, 4, 6, 9, 7, 8, 10].
# This array is missing the number 3. The goal of this problem is to write code that finds which numbers are missing, and print them out.

list = []
n = int(input("Enter number of elements: "))

for i in range(0, n):
    x = int(input())
    list.append(x)

# Find the maximum number in the list
maxNum = max(list)

# Initialize the counter start from Find the minimum number in the list
count = min(list)

isMissing = True

# check if there missing numbers
while count <= maxNum:
    if not count in list:
        print(f"This array is missing the number {count}")
        isMissing = False
    count += 1

# Output that none are missing
if isMissing:
    print("No numbers are missing.")
