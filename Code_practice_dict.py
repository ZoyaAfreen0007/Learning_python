'''Employee Salary Analysis

Given:

employees = {
    "E01": {"name": "Ali", "salary": 45000, "dept": "IT"},
    "E02": {"name": "Sara", "salary": 65000, "dept": "HR"},
    "E03": {"name": "John", "salary": 55000, "dept": "IT"},
    "E04": {"name": "Zoya", "salary": 75000, "dept": "Finance"},
    "E05": {"name": "Aman", "salary": 60000, "dept": "IT"}
}

Write a function:

analyze_employees(employees)

Return:

Employee with highest salary
Employee with lowest salary
Average salary
Number of employees in each department
Employees earning above average salary'''



def analyze_employees(employees):
    total_salary = 0
    count = 0

    highest = None
    lowest = None

    dept_count = {}
    
    # First pass: salary, highest, lowest, departments
    for emp_id, details in employees.items():
        name = details["name"]
        salary = details["salary"]
        dept = details["dept"]

        total_salary += salary
        count += 1

        if highest is None or salary > highest["salary"]:
            highest = {
                "id": emp_id,
                "name": name,
                "salary": salary
            }

        if lowest is None or salary < lowest["salary"]:
            lowest = {
                "id": emp_id,
                "name": name,
                "salary": salary
            }

        if dept in dept_count:
            dept_count[dept] += 1
        else:
            dept_count[dept] = 1

    average = total_salary / count

    # Employees earning above average
    above_average = []

    for emp_id, details in employees.items():
        if details["salary"] > average:
            above_average.append(details["name"])

    return {
        "highest_salary": highest,
        "lowest_salary": lowest,
        "average_salary": average,
        "department_count": dept_count,
        "above_average": above_average
    }


result = analyze_employees(employees)

print(result)


'''Shopping Cart Analyzer ⭐⭐
cart = {
    "Laptop": {"price": 60000, "quantity": 1},
    "Mouse": {"price": 800, "quantity": 2},
    "Keyboard": {"price": 1500, "quantity": 1}
}

Write:

cart_analysis(cart)

Find:

Total number of items
Total bill
Most expensive product
Product with highest quantity
Average product price'''





def cart_analysis(cart):
    total_items = 0
    total_bill = 0
    most_expensive_product = None
    highest_quantity_product = None
    total_price = 0

    for product, details in cart.items():
        price = details["price"]
        quantity = details["quantity"]

        total_items += quantity
        total_bill += price * quantity
        total_price += price

        if (most_expensive_product is None or
                price > cart[most_expensive_product]["price"]):
            most_expensive_product = product

        if (highest_quantity_product is None or
                quantity > cart[highest_quantity_product]["quantity"]):
            highest_quantity_product = product

    average_product_price = total_price / len(cart)

    return {
        "Total items": total_items,
        "Total bill": total_bill,
        "Most expensive product": most_expensive_product,
        "Product with highest quantity": highest_quantity_product,
        "Average product price": average_product_price
    }


cart = {
    "Laptop": {"price": 60000, "quantity": 1},
    "Mouse": {"price": 800, "quantity": 2},
    "Keyboard": {"price": 1500, "quantity": 1}
}

print(cart_analysis(cart))

















