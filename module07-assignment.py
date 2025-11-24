# Module 7 Assignment: Organizing Data with Lists and Tuples
# TechElectronics Inventory Tracking System

# Welcome message
print("=" * 60)
print("TECHELECTRONICS INVENTORY TRACKING SYSTEM")
print("=" * 60)

# TODO 1: Create product tuples
# Each product is a tuple: (product_id, name, price, quantity, category)
# Create at least 5 product tuples
# Example: product1 = ("P001", "Smartphone X", 799.99, 10, "Mobile Phones")
product1 = ("P01", "iPhone 14", 849.99, 50, "Mobile Phones")
product2 = ("P02", "Smart Printer", 399.99, 25, "Printers")
product3 = ("P03", "iPhone 16", 874.99, 75, "Mobile Phones")
product4 = ("P04", "Laptop", 599.99, 40, "Laptops")
product5 = ("P05", "Digital Camera", 249.99, 35, "Cameras")
# TODO 2: Create an inventory list containing all product tuples
# Example: inventory = [product1, product2, ...]
inventory = [product1, product2, product3, product4, product5]
# TODO 3: Display all products
# Use a print statement to show each product in the inventory
print("\nCurrent Inventory:")
print("-" * 60)
# Add your code here to display all products
print(inventory)
# TODO 4: Access specific elements
# Use indexing to:
# - Get and display the first product (store in first_product)
# - Get and display the last product (store in last_product)
# - Get and display the third product's name only (store in third_product_name)
# - Get and display the second product's price and quantity (store in second_price, second_quantity)

print("\n\nAccessing Specific Products:")
print("-" * 60)
# Add your code here
first_product = inventory[0]
print(first_product)
last_product = inventory[-1]
print(last_product)
third_product_name = inventory[2][1]
print(third_product_name)
second_price, second_quantity = inventory[1][2:4]
print(second_price, second_quantity)
# TODO 5: Use slicing to get subsets
# - Get and display the first 3 products (store in first_three)
# - Get and display products from index 2 to 4 (store in middle_products)
# - Get and display all products except the first one (store in all_except_first)

print("\n\nProduct Subsets Using Slicing:")
print("-" * 60)
# Add your code here
first_three = inventory[:3]
print(first_three)
middle_products = inventory[2:4]
print(middle_products)
all_except_first = inventory[1:]
print(all_except_first)
# TODO 6: Add new products to inventory
# Create 2 new product tuples and add them to the inventory list
# Use the .append() method

print("\n\nAdding New Products:")
print("-" * 60)
# Add your code here
product6 = ("P06", "Computer", 399.99, 20, "Laptops")
product7 = ("P07", "Polaroid Camera", 79.99, 50, "Cameras")
inventory.append(product6)
inventory.append(product7)
# TODO 7: Remove a product
# Remove the product at index 2 using .pop()
# Display what was removed and show the updated inventory

print("\n\nRemoving a Product:")
print("-" * 60)
# Add your code here
removed = inventory.pop(2)
print(removed)
print(inventory)
first_three = inventory[:3]
print(first_three)
middle_products = inventory[2:5]
print(middle_products)
all_except_first = inventory[1:]
print(all_except_first)
# TODO 8: Insert a product at a specific position
# Create a new product tuple and insert it at index 1
# Use the .insert() method

print("\n\nInserting a Product:")
print("-" * 60)
# Add your code here
product8 = ("P08", "iPhone 11", 749.99, 15, "Mobile Phones")
inventory.insert(1,product8)
print(inventory)
first_three = inventory[:3]
print(first_three)
middle_products = inventory[2:5]
print(middle_products)
all_except_first = inventory[1:]
print(all_except_first)
last_product = inventory[-1]
print(last_product)
third_product_name = inventory[2][1]
print(third_product_name)
second_price, second_quantity = inventory[1][2:4]
print(second_price, second_quantity)
# TODO 9: Create category lists
# Create separate lists for different categories
# For example: mobile_phones = [], laptops = [], audio = []
# Go through your inventory and add products to appropriate category lists

print("\n\nProducts by Category:")
print("-" * 60)
# Add your code here
phones = []
laptops = []
cameras = []
printers = []
for category in inventory:
    if category[4] == "Mobile Phones":
        phones.append(category)
    elif category[4] == "Cameras":
        cameras.append(category)
    elif category[4] == "Laptops":
        laptops.append(category)
    elif category[4] == "Printers":
        printers.append(category)
print(phones)
print(laptops)
print(cameras)
print(printers)
# TODO 10: Calculate inventory statistics
# Calculate and display:
# - Total number of products in inventory (store in total_products)
# - Total value of all products (price * quantity for each product) (store in total_value)
# - List of all product names (store in product_names)
# - List of all product prices (store in product_prices)

print("\n\nInventory Statistics:")
print("-" * 60)
# Add your code here
total_products = len(inventory)
print(total_products)
total_value = sum(q[2] * q[3] for q in inventory)
print(f"{total_value:.2f}")
product_names = []
for name in inventory:
    product_names.append(name[1])
print(product_names)
product_prices = []
for price in inventory:
    product_prices.append(price[2])
print(product_prices)
# TODO 11: Find expensive products using list comprehension
# Use a list comprehension to create a list of products that cost more than $500
# Store in variable: expensive_products
# Display these expensive products
# Hint: expensive_products = [product for product in inventory if product[2] > 500]

print("\n\nExpensive Products (> $500):")
print("-" * 60)
# Add your code here
expensive_products = [money for money in inventory if money[2]>500]
print(expensive_products)
# TODO 12: Low stock alert using list comprehension
# Use a list comprehension to create a list of products with quantity less than 5
# Store in variable: low_stock
# Display these low stock products
# Hint: low_stock = [product for product in inventory if product[3] < 5]

print("\n\nLow Stock Alert (< 5 units):")
print("-" * 60)
# Add your code here
low_stock = [num for num in inventory if num[3]<5]
print(low_stock)
# TODO 13: Create price list using list comprehension
# Use a list comprehension to create a list of all product prices (store in original_prices)
# Then use another comprehension to apply a 10% discount to all prices (store in discounted_prices)
# Display both the original and discounted price lists

print("\n\nPrice Lists:")
print("-" * 60)
# Add your code here
original_prices = [ogp[2] for ogp in inventory]
print(original_prices)
discounted_prices = [dp[2]*0.9 for dp in inventory]
print(discounted_prices)
# TODO 14: Product name formatting using list comprehension
# Use a list comprehension to create a list of all product names in uppercase (store in uppercase_names)
# Then create another list with product codes (first 3 chars of ID + first 3 chars of name) (store in product_codes)
# Display both lists

print("\n\nFormatted Product Names:")
print("-" * 60)
# Add your code here
uppercase_names = [name[1].upper() for name in inventory]
print(uppercase_names)
product_codes = []
for thing in inventory:
    char = thing[0][:3]
    cname = thing[1][:3]
    string = f"{char}{cname}"
    product_codes.append(string)
print(product_codes)
# TODO 15: Using Loops to Process Inventory
# Use a for loop to:
# - Count how many products are in the "Mobile Phones" category (store in mobile_count)
# - Calculate the total value of all "Laptops" in stock (store in laptop_value)
# - Find the most expensive product in the inventory (store in most_expensive)

print("\n\nLoop-Based Analysis:")
print("-" * 60)
# Add your code here
mobile_count = 0
for phone in inventory:
    if phone[4] == "Mobile Phones":
        mobile_count += 1
print(mobile_count)
laptop_value = 0
for laptop in inventory:
    if laptop[4] == "Laptops":
        laptop_value += laptop[2]*laptop[3]
print(f"{laptop_value:.2f}")
pricing = 0
for ep in inventory:
    if ep[2] > pricing:
        pricing = ep[2]
        most_expensive = ep
        print(most_expensive)
# TODO 16: Using Conditionals with Lists
# Use loops and conditionals to:
# - Create a list of products that need restocking (quantity < 5) (store in restock_list)
# - Create a list of high-value items (price > $500 AND quantity > 10) (store in high_value_items)
# - Count products in different price ranges: under $100, $100-$500, over $500 (store counts in price_ranges dictionary)

print("\n\nConditional Analysis:")
print("-" * 60)
# Add your code here
restock_list = [q for q in inventory if q[3] < 5]
print(restock_list)
high_value_items = [hv for hv in inventory if hv[2]> 500 and hv[3] > 10]
print(high_value_items)
under_one = 0
for lm in inventory:
    if lm[2] < 100:
        under_one += 1
one_to_five = 0
for mm in inventory:
    if mm[2] >100 and mm[2] < 500:
        one_to_five +=1
over_five = 0
for hm in inventory:
    if hm[2] > 500:
        over_five += 1
price_ranges = [under_one, one_to_five, over_five]
print(price_ranges)
# TODO 17: Define and Use Functions
# Define these functions:
# - calculate_product_value(product): returns price * quantity for a product tuple
# - find_products_by_category(inventory, category): returns list of products in given category
# - apply_discount(inventory, discount_percent): returns new inventory with discounted prices
# Then use these functions to:
# - Calculate total inventory value
# - Find all "Audio" products
# - Create a new inventory with 15% discount applied

print("\n\nFunction-Based Operations:")
print("-" * 60)
# Add your code here
def calculate_product_value(pr):
    for pr in inventory:
        return pr[2] * pr[3]
print(calculate_product_value(inventory))
def find_products_by(inventory, category):
    thing_in_category = []
    for thing in inventory:
        if thing[4] == category:
            thing_in_category.append(thing)
    return thing_in_category
print(find_products_by(inventory,"Audio"))
def apply_discount(inventory, discount_price):
    newinv = []
    for stuff in inventory:
        newinv.append(stuff[2]*discount_price)
    return newinv
print(apply_discount(inventory, 0.85))
# TODO 18: Combine Loops, Functions, and List Operations
# Create a function generate_inventory_report(inventory) that:
# - Uses loops to analyze the inventory
# - Returns a dictionary with:
#   - 'total_products': total number of products
#   - 'total_value': sum of all (price * quantity)
#   - 'categories': list of unique categories
#   - 'low_stock': list of products with quantity < 5
#   - 'average_price': average price of all products
# Call the function and display the report

print("\n\nComprehensive Inventory Report:")
print("-" * 60)
# Add your code here
def generate_inventory_report(inventory):
    total_products = len(inventory)
    total_value = sum(p[2] * p[3] for p in inventory)
    categories = []
    for ctg in inventory:
        if ctg[4] != categories:
            categories.append(ctg[4])
    low_stock = []
    for li in inventory:
        if li[3] < 5:
            low_stock.append(li)
    denom = 0
    total = 0
    for ai in inventory:
        total += ai[2]
        denom += 1
    average_price = total / denom
    dictionary = [total_products, total_value, categories, low_stock, average_price]
    return dictionary
print(generate_inventory_report(inventory))