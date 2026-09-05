'''Nested Tuple Calculation

Given:

students = (
    ("Ali", 80, 75, 90),
    ("Sara", 85, 90, 88),
    ("John", 70, 65, 78)
)

Find:

Each student's total marks
Each student's average
The student with the highest average
'''


students = (
    ("Ali", 80, 75, 90),
    ("Sara", 85, 90, 88),
    ("John", 70, 65, 78)
)

highest_avg = 0
top_student = ""

for student in students:
    name = student[0]
    marks = student[1:]

    total = sum(marks)
    average = total / len(marks)

    print(name)
    print("Total:", total)
    print("Average:", average)

    if average > highest_avg:
        highest_avg = average
        top_student = name

print("\nStudent with highest average:", top_student)
print("Highest average:", highest_avg)




'''Find Second Largest

Find the second-largest element in a tuple without using sort() or sorted().

Example:

numbers = (10, 45, 23, 89, 67, 89)'''




numbers = (10, 45, 23, 89, 67, 89)

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest:", second_largest)



'''Function to Find Maximum and Minimum
Write a function:

find_min_max(numbers)

that accepts a tuple and returns both the minimum and maximum without using min() or max().'''



def find_min_max(numbers):
    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

    return minimum, maximum


numbers = (10, 45, 23, 89, 67, 12)

result = find_min_max(numbers)

print("Minimum:", result[0])
print("Maximum:", result[1])


'''Tuple Analysis Function

Write a function:

analyze(numbers)

For:

numbers = (10, 20, 15, 20, 30, 10, 40, 15, 50)

The function should return:

Total elements
Sum
Average
Maximum
Minimum
Number of even elements
Number of odd elements
Number of duplicate values

Restrictions: Don't use sort(), sorted(), Counter, min(), or max().'''


def analyze(numbers):
    total_elements = 0
    total_sum = 0
    even_count = 0
    odd_count = 0

    # Find total, sum, even and odd
    for num in numbers:
        total_elements += 1
        total_sum += num

        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    average = total_sum / total_elements

    # Find maximum and minimum
    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

    # Count duplicate values
    duplicate_count = 0

    for i in range(total_elements):
        count = 0

        for j in range(total_elements):
            if numbers[i] == numbers[j]:
                count += 1

        if count > 1:
            # Count each duplicated value only once
            already_counted = False

            for k in range(i):
                if numbers[k] == numbers[i]:
                    already_counted = True
                    break

            if not already_counted:
                duplicate_count += 1

    return (
        total_elements,
        total_sum,
        average,
        maximum,
        minimum,
        even_count,
        odd_count,
        duplicate_count
    )


numbers = (10, 20, 15, 20, 30, 10, 40, 15, 50)

result = analyze(numbers)

print("Total elements:", result[0])
print("Sum:", result[1])
print("Average:", result[2])
print("Maximum:", result[3])
print("Minimum:", result[4])
print("Number of even elements:", result[5])
print("Number of odd elements:", result[6])
print("Number of duplicate values:", result[7])




'''
Write a function named multiply_all that accepts any number of numerical arguments and returns their product. If no arguments are passed, it should return 1. '''
def multiply_all(*args):
    # args is treated as a tuple internally
    product = 1
    for num in args:
        product *= num
    return product

print(multiply_all(2, 3, 4))  # Output: 24
print(multiply_all())         # Output: 1


'''
Frequency of an Element
Write a function that accepts a tuple and an element, then returns how many times that element occurs without using count().
'''
def frequency(t, element):
    count = 0

    for item in t:
        if item == element:
            count += 1

    return count


t = (1, 2, 3, 2, 4, 2, 5)
print(frequency(t, 2))


'''
Tuple Compression
Write a function that converts:

(1, 1, 1, 2, 2, 3, 3, 3)

into:

((1, 3), (2, 2), (3, 3))
'''
def compress_tuple(t):
    result = []
    i = 0

    while i < len(t):
        value = t[i]
        count = 0

        while i < len(t) and t[i] == value:
            count += 1
            i += 1

        result.append((value, count))

    return tuple(result)


t = (1, 1, 1, 2, 2, 3, 3, 3)

print(compress_tuple(t))




















