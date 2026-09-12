'''Given:

employees = {
    "E01": {"name": "Ali", "salary": 45000},
    "E02": {"name": "Sara", "salary": 55000},
    "E03": {"name": "John", "salary": 40000},
    "E04": {"name": "Zoya", "salary": 65000}
}

Write a program to:

Find the employee with the highest salary.
Find the average salary.
Display employees earning more than the average salary.
Increase everyone's salary by 10%.
Store the updated salaries in the dictionary.'''

employees = {
    "E01": {"name": "Ali", "salary": 45000},
    "E02": {"name": "Sara", "salary": 55000},
    "E03": {"name": "John", "salary": 40000},
    "E04": {"name": "Zoya", "salary": 65000}
}

# 1. Find employee with highest salary
highest_employee = max(employees, key=lambda emp: employees[emp]["salary"])

print("Highest Salary Employee:")
print(employees[highest_employee]["name"], employees[highest_employee]["salary"])


# 2. Find average salary
total_salary = sum(emp["salary"] for emp in employees.values())
average_salary = total_salary / len(employees)

print("\nAverage Salary:", average_salary)


# 3. Display employees earning more than average salary
print("\nEmployees earning more than average:")

for emp_id, emp in employees.items():
    if emp["salary"] > average_salary:
        print(emp_id, emp["name"], emp["salary"])


# 4. Increase everyone's salary by 10%
# 5. Store updated salaries in dictionary

for emp in employees.values():
    emp["salary"] = emp["salary"] * 1.10


print("\nUpdated Employee Salaries:")

for emp_id, emp in employees.items():
    print(emp_id, emp["name"], emp["salary"])



'''Write a function that accepts a dictionary containing integer values and returns the number of even and odd values.'''

def count_even_odd(d):
    even = 0
    odd = 0

    for value in d.values():
        if value % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


d = {"a": 10, "b": 15, "c": 22, "d": 31, "e": 40}

print(count_even_odd(d))


'''
Write a function that combines two dictionaries. If a key exists in both dictionaries, add their values.
'''

def add_common_values(d1, d2):
    result = {}

    for key in d1:
        result[key] = d1[key]

    for key in d2:
        if key in result:
            result[key] += d2[key]
        else:
            result[key] = d2[key]

    return result


d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 5, "c": 10, "d": 15}

print(add_common_values(d1, d2))

'''Write a function to calculate the sum of all values without using sum().'''

def dictionary_sum(d):
    total = 0

    for value in d.values():
        total += value

    return total


d = {"a": 10, "b": 20, "c": 30}

print(dictionary_sum(d))






















