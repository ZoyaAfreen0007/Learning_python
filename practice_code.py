
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
