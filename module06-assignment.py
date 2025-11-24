# Module 6 Assignment: Functions and Modular Programming
# TechRetail Sales Analysis System

# Welcome message
print("=" * 60)
print("TECHRETAIL SALES ANALYSIS SYSTEM")
print("=" * 60)

# Sample quarterly sales data 
# Format: [product_name, category, price, quantity_sold, employee_id]
sales_data = [
    ["Smartphone Pro", "Phones", 899.99, 15, "E101"],
    ["Laptop Ultra", "Computers", 1299.99, 10, "E105"],
    ["Wireless Earbuds", "Audio", 149.99, 30, "E101"],
    ["Smart Watch", "Wearables", 249.99, 12, "E102"],
    ["Gaming Console", "Gaming", 499.99, 8, "E103"],
    ["Bluetooth Speaker", "Audio", 79.99, 25, "E102"],
    ["Tablet Lite", "Computers", 399.99, 18, "E104"],
    ["Digital Camera", "Cameras", 599.99, 5, "E105"],
    ["VR Headset", "Gaming", 299.99, 7, "E103"],
    ["Fitness Tracker", "Wearables", 129.99, 22, "E104"],
    ["Smartphone Plus", "Phones", 699.99, 20, "E101"],
    ["Laptop Basic", "Computers", 899.99, 14, "E105"]
]

# Employee information
# Format: {employee_id: [name, commission_rate]}
employees = {
    "E101": ["Alex Johnson", 0.05],
    "E102": ["Sarah Williams", 0.045],
    "E103": ["James Brown", 0.04],
    "E104": ["Lisa Davis", 0.05],
    "E105": ["Michael Wilson", 0.055]
}

# TODO 1: Sales Analysis Functions
# 1.1 Create a function to calculate total sales revenue
# REQUIRED FUNCTION NAME: calculate_total_sales
def calculate_total_sales():
    """
    Calculates the total revenue from all sales.
    
    Returns:
        float: The total sales revenue.
    """
    # Your code here
    total = 0
    for sale in sales_data:
        total += sale[2] *sale[3]
    return total


# 1.2 Create a function to calculate the total sales for a specific category
# REQUIRED FUNCTION NAME: calculate_category_sales
def calculate_category_sales(category):
    """
    Calculates the total revenue from sales in a specific product category.
    
    Args:
        category (str): The product category to calculate sales for.
        
    Returns:
        float: The total sales revenue for the specified category.
    """
    # Your code here
    x = 0
    total_sales = 0
    for row in sales_data:
        if row[1] == category:
            total_sales += row[2] * row[3]
        x = x + 1
    return total_sales



# 1.3 Create a function to find the best-selling product
# REQUIRED FUNCTION NAME: find_best_selling_product
# Should return tuple: (product_name, total_revenue)
# Your function here
best_product=["",0]
best_selling_product = ("",0)
def find_best_selling_product():
    for product in sales_data:
        revenue = product [2] * product [3]
        if revenue > best_product[1]:
            best_product[1] = revenue
            best_product[0] = product[0]
        best_selling_product=best_product[0], best_product[1]
    return best_selling_product

        
    
# TODO 2: Commission Calculation Functions
# 2.1 Create a function to calculate commission for a specific employee
# REQUIRED FUNCTION NAME: calculate_employee_commission
def calculate_employee_commission(employee_id):
    """
    Calculates the commission earned by a specific employee.
    
    Args:
        employee_id (str): The unique identifier of the employee.
        
    Returns:
        float: The commission amount earned.
    """
    # Your code here
    total = 0
    for item in sales_data:
        if item[4] == employee_id:
            total += item[2] * item [3]
    for emp_id in employees:
        rate = employees[employee_id][1]
        commission = total * rate
    return commission

# 2.2 Create a function to calculate total commission for all employees
# REQUIRED FUNCTION NAME: calculate_total_commission
# Should return float: total commission for all employees
# Your function here

def calculate_total_commission():
    tcommission = 0
    total = 0
    rate = 0
    x = 0
    scommission = 0
    tcommission = 0
    for item in sales_data:
        for emp_id in employees:
            if emp_id == item[4]:
                total = item[2] * item [3]
                rate = employees[emp_id][1]
                scommission = total * rate
                tcommission += scommission
    return tcommission

# TODO 3: Report Generation Functions
# 3.1 Create a function to generate a sales summary report
# REQUIRED FUNCTION NAME: generate_sales_summary
def generate_sales_summary(include_categories=True):
    """
    Generates a formatted sales summary report.
    
    Args:
        include_categories (bool, optional): Whether to include category breakdown.
            Defaults to True.
        
    Returns:
        str: Formatted report string.
    """
    # Your code here
    string2 = ""
    for item in sales_data:
        money = item[2] * item[3]
        string = f"Product: {item[0]} "
        if include_categories == True:
            string += f"Category: {item[1]} "
        string += f"Total Sales: ${money} "
        string2 += string
    return string2


# 3.2 Create a function to generate an employee performance report
# REQUIRED FUNCTION NAME: generate_employee_report
# Should return string with employee sales and commissions
# Your function here
def generate_employee_report():
    string2=""
    emp_report = []
    commiss_total = 0
    for employee_id in employees:
        for sale in sales_data:
            money_total = sale[2] * sale[3]
        commiss_total +=money_total * employees[employee_id][1]
        string1 = f"Employee: {employees[employee_id][0]} Sales: ${money_total} Commission: ${commiss_total} "
        string2 += string1
    return string2

    
# TODO 4: Utility Functions
# 4.1 Create a function to get all products in a specific category
# REQUIRED FUNCTION NAME: get_products_by_category
def get_products_by_category(category):
    """
    Returns all products belonging to a specific category.
    
    Args:
        category (str): The product category to filter by.
        
    Returns:
        list: List of products in the specified category.
    """
    # Your code here
    products = []
    x = 0
    for thing in sales_data:
        if sales_data[x][1] == category:
            products.append(thing)
        x = x + 1
    return products


# 4.2 Create a function to calculate the average sale price
# REQUIRED FUNCTION NAME: calculate_average_sale_price
# Should return float: average sale price across all transactions
# Your function here
def calculate_average_sale_price():
    total = 0
    denominator = 0
    for sale in sales_data:
        total += sale[2] * sale[3]
        denominator += sale[3]
    average = total/denominator
    return average

# Main program flow - function calls to demonstrate your system
# REQUIRED FUNCTION NAME: main
def main():
    print("\nTECHRETAIL QUARTERLY SALES ANALYSIS")
    print("-" * 40)
    
    # Calculate and display total sales
    print("\nTOTAL QUARTERLY SALES:")
    # Your function call here
    print(calculate_total_sales())
    # Display category sales
    print("\nSALES BY CATEGORY:")
    categories = ["Phones", "Computers", "Audio", "Wearables", "Gaming", "Cameras"]
    # Your code to display sales for each category
    print(calculate_category_sales("Phones"))
    print(calculate_category_sales("Computers"))
    print(calculate_category_sales("Audio"))
    print(calculate_category_sales("Wearables"))
    print(calculate_category_sales("Gaming"))
    print(calculate_category_sales("Cameras"))
    # Display best-selling product
    print("\nBEST-SELLING PRODUCT:")
    # Your function call here
    print(find_best_selling_product())
    # Display employee commissions
    print("\nEMPLOYEE COMMISSIONS:")
    # Your code to display commission for each employee
    print(calculate_employee_commission("E101"))
    print(calculate_employee_commission("E102"))
    print(calculate_employee_commission("E103"))
    print(calculate_employee_commission("E104"))
    print(calculate_employee_commission("E105"))
    # Generate and display sales summary report
    print("\nQUARTERLY SALES SUMMARY REPORT:")
    # Your function call here
    print(generate_sales_summary())
    # Generate and display employee performance report
    print("\nEMPLOYEE PERFORMANCE REPORT:")
    # Your function call here
    print(generate_employee_report())
# Run the main program
if __name__ == "__main__":
    main()
print(main())
