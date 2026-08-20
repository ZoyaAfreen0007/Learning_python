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



