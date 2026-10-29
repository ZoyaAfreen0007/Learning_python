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


'''
Return Top 3 Values
Write a function that returns the three largest elements of a tuple without using sort() or sorted().
'''

def top_three(t):
    first = second = third = float('-inf')

    for num in t:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num

    return (first, second, third)


t = (10, 5, 25, 8, 30, 15, 20)
print(top_three(t))


'''
Nested Tuple Sum
Write a function that accepts a nested tuple:

t = ((1, 2), (3, 4), (5, 6))

and returns the total sum of all elements.
'''

def nested_sum(t):
    total = 0

    for sub_tuple in t:
        for num in sub_tuple:
            total += num

    return total


t = ((1, 2), (3, 4), (5, 6))
print(nested_sum(t))


'''
Palindrome Tuple
Write a function that checks whether a tuple is a palindrome without converting it into a string.

(1, 2, 3, 2, 1) → True
(1, 2, 3, 4) → False
'''
def is_palindrome(t):
    for i in range(len(t) // 2):
        if t[i] != t[len(t) - 1 - i]:
            return False
    return True


print(is_palindrome((1, 2, 3, 2, 1)))  
print(is_palindrome((1, 2, 3, 4)))      


'''
Sum of Tuple Elements
Write a function to calculate the sum of all elements in a tuple without using sum().
'''

def tuple_sum(t):
    total = 0

    for i in t:
        total += i

    return total


t = (10, 20, 30, 40, 50)

print(tuple_sum(t))



#Given t = (10, 20, 30, 40, 50), find the second-largest element without using max() or sorting.


t = (10, 20, 30, 40, 50)

largest = t[0]
second_largest = t[0]

for i in t:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("Second largest element:", second_largest)


#. Given t = (1, 2, 2, 3, 3, 3, 4), create a tuple containing each distinct element only once, preserving the original order.

t = (1, 2, 2, 3, 3, 3, 4)

result = ()

for i in t:
    if i not in result:
        result = result + (i,)

print(result)

'''Given t = ((1, 2), (3, 4), (5, 6)), calculate the sum of all the numbers in the nested tuple.'''

t = ((1, 2), (3, 4), (5, 6))

total = 0

for i in t:
    for j in i:
        total = total + j

print("Sum:", total)


'''Given t = (10, 20, 30, 40, 50), find the pair of elements whose sum equals 60.
'''


t = (10, 20, 30, 40, 50)

for i in range(len(t)):
    for j in range(i + 1, len(t)):
        if t[i] + t[j] == 60:
            print(t[i], t[j])


#. Given t = (4, 7, 2, 9, 5, 8), find the longest continuous sequence of increasing numbers.
t = (4, 7, 2, 9, 5, 8)

longest = (t[0],)
current = (t[0],)

for i in range(1, len(t)):
    if t[i] > t[i - 1]:
        current = current + (t[i],)
    else:
        current = (t[i],)

    if len(current) > len(longest):
        longest = current

print("Longest increasing sequence:", longest)
print("Length:", len(longest))


'''Convert the list [10, 20, 30, 40] into a tuple, then calculate its sum without using sum().'''

numbers = [10, 20, 30, 40]

t = tuple(numbers)

total = 0

for i in t:
    total = total + i

print("Tuple:", t)
print("Sum:", total)


'''Given t = (2, 4, 6, 8, 10), check whether every element is even.'''

t = (2, 4, 6, 8, 10)

for i in t:
    if i % 2 != 0:
        print("Not all elements are even")
        break
else:
    print("All elements are even")


'''Given t = (10, 20, 30) and u = (40, 50, 60), combine them into one tuple.'''

t = (10, 20, 30)
u = (40, 50, 60)

result = t + u

print(result)

'''Find the third-largest distinct element

Given t = (12, 45, 23, 45, 67, 34, 67, 56), find the third-largest distinct element without using max(), sorted(), or sort().'''


largest = float('-inf')
second_largest = float('-inf')
third_largest = float('-inf')

for i in t:
    if i > largest:
        third_largest = second_largest
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        third_largest = second_largest
        second_largest = i
    elif i > third_largest and i != second_largest and i != largest:
        third_largest = i

print("Third-largest distinct element:", third_largest)


'''Find all pairs with a target sum

Given t = (2, 7, 11, 15, 3, 6, 9) and target = 18, print every unique pair whose sum equals the target.'''

t = (2, 7, 11, 15, 3, 6, 9)
target = 18

for i in range(len(t)):
    for j in range(i + 1, len(t)):
        if t[i] + t[j] == target:
            print(t[i], t[j])

'''Flatten a nested tuple

Given t = ((1, 2), (3, 4, 5), (6,), (7, 8, 9)), convert it into a single tuple: (1, 2, 3, 4, 5, 6, 7, 8, 9). Do not use list comprehensions.'''

t = ((1, 2), (3, 4, 5), (6,), (7, 8, 9))

result = ()

for i in t:
    for j in i:
        result = result + (j,)

print(result)


'''Find the longest increasing continuous sequence

Given t = (3, 5, 7, 2, 4, 6, 8, 1, 9, 10, 11), find the longest continuous strictly increasing sequence and its length.'''


t = (3, 5, 7, 2, 4, 6, 8, 1, 9, 10, 11)

longest = (t[0],)
current = (t[0],)

for i in range(1, len(t)):
    if t[i] > t[i - 1]:
        current = current + (t[i],)
    else:
        current = (t[i],)

    if len(current) > len(longest):
        longest = current

print("Longest increasing sequence:", longest)
print("Length:", len(longest))






