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
