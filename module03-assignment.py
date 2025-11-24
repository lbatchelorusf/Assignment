# Module 3 Assignment: String Manipulation, User Input, and Formatted Output

# Welcome message
print("=" * 50)
print("CUSTOMER ORDER PROCESSING SYSTEM")
print("=" * 50)
print("Please enter the following information:\n")

# TODO: Collect customer information
# Use input() with the exact prompts specified
# Apply .strip() and appropriate formatting

customer_name = input("Enter customer name: ").strip().title()
customer_email = input("Enter customer email: ").strip().lower()


# TODO: Collect order information
# Remember to strip whitespace from all inputs

product_name = input("Enter product name: ").strip().title()
old_quantity = input("Enter quantity: ").strip()
old_unit_price = input("Enter unit price: ").strip()

# TODO: Process the information
# 1. Convert quantity to int and unit_price to float
# 2. Calculate subtotal = quantity * unit_price
# 3. Calculate tax_amount = subtotal * 0.085
# 4. Calculate order_total = subtotal + tax_amount
quantity = int(old_quantity)
unit_price = float(old_unit_price)
subtotal = quantity * unit_price
tax_amount = subtotal * 0.085
order_total = subtotal + tax_amount

# TODO: Display order summary
# Use f-strings to format the output as shown in the example
print("  \n  \n  \n")
print("ORDER SUMMARY")
print("=" *13)
print(f"Customer: {customer_name}")
print(f"Email: {customer_email}")
print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8.5%): ${tax_amount:.2f}")
print(f"Order Total: ${order_total:.2f}")