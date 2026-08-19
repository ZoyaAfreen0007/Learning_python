'''Find the Second Largest Number:
Take n numbers from the user and find the second-largest number without using sort() or max().'''

n = int(input("Enter how many numbers: "))

numbers = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("Second largest number does not exist.")
else:
    print("Second largest number:", second_largest)



'''LCM Without Built-in Functions
Take two numbers and find their LCM using loops.'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    start = a
else:
    start = b

lcm = start

while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1

print("LCM =", lcm)


'''Frequency of a Digit

Count how many times a particular digit appears in a number.

Example: 122333, digit 3 → 3 times'''

num = int(input("Enter a number: "))
digit = int(input("Enter the digit to find: "))

count = 0

while num > 0:
    last_digit = num % 10

    if last_digit == digit:
        count += 1

    num = num // 10

print("Frequency:", count)














