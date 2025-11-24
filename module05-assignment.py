# Module 5 Assignment: Loops and Repetition in Business Applications
# QuickMart Sales Analysis

# Welcome message
print("=" * 60)
print("QUICKMART SALES ANALYSIS")
print("=" * 60)

# Monthly sales data per store (in thousands of dollars)
# Data structure: Dictionary with store locations as keys
# Each store contains a list of 12 monthly sales figures (Jan-Dec)
sales_data = {
    "Downtown": [120.5, 115.8, 131.2, 140.5, 150.2, 160.1, 155.3, 148.9, 152.5, 160.8, 165.2, 180.3],
    "Suburb Mall": [85.6, 90.2, 93.5, 100.8, 110.5, 115.7, 120.2, 118.5, 125.6, 130.2, 140.8, 155.5],
    "Westside": [95.2, 88.7, 92.3, 100.5, 105.8, 110.2, 115.7, 120.5, 125.8, 130.2, 135.5, 145.8],
    "University": [55.3, 60.2, 65.8, 70.5, 65.2, 50.1, 45.2, 55.8, 80.5, 85.9, 90.2, 95.3]
}

# Store locations
locations = list(sales_data.keys())

# List of month names for reporting
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

# TODO 1: Calculate the total sales for each month across all stores
# Initialize a list to store the total monthly sales
monthly_totals = []

# Your loop code here:
# Hint: For each month index, sum the sales from all stores
# REQUIRED: Use a for loop with range(12) for months
# REQUIRED: Use a nested for loop to iterate through stores
x = "Downtown"
y = 0
total = 0
for month in range(12):
    for store in sales_data:
        x = store
        total += sales_data[x][y]
        if x == "University":
            x = "Downtown"
    monthly_totals.append(total)
    total = 0
    y = y + 1


# TODO 2: Find the month with the highest and lowest total sales
# Initialize variables to track highest and lowest sales
highest_month_index = 0
lowest_month_index = 0
highest_sales = 0
lowest_sales = 100000  # Start with infinity for comparison

# Your loop code here:
# Hint: Compare each monthly total against current highest/lowest
x = 0
for mtotal in range(len(monthly_totals)):
    if  monthly_totals[x] > highest_sales:
        highest_sales =  monthly_totals[x]
        highest_month_index = mtotal
    if  monthly_totals[x] < lowest_sales:
        lowest_sales =  monthly_totals[x]
        lowest_month_index = mtotal
    x = x + 1 

# TODO 3: Calculate the average monthly sales across all stores
# Your loop code here:
# Store result in: average_monthly_sales (float)
# Hint: Calculate the sum of all monthly totals and divide by the number of months
average_monthly_sales = sum(monthly_totals)/len(months)

# TODO 4: Find the store with the highest annual sales
# Initialize variables to track the best performing store
best_store = ""
best_store_sales = 0

# Your loop code here:
# REQUIRED: Use a for loop to iterate through stores
# Update best_store and best_store_sales variables
x = "Downtown"
for stores in sales_data:
    x + store
    store_sales= sum(sales_data[x])
    if store_sales > best_store_sales:
        best_store_sales = store_sales
        best_store = x


# TODO 5: Generate a monthly performance report using a while loop
# The report should show each month's total sales and whether it was above or below the monthly average
# Your while loop code here:
# REQUIRED: Use a while loop with a counter variable
# Store performance messages in: performance_report (list)
performance_report = []
x = 0
while x < len(months):
    if monthly_totals[x] < average_monthly_sales:
        performance_report.append(f"{months[x]} {monthly_totals[x]:.2f} Below Average")
    elif monthly_totals[x] > average_monthly_sales:
        performance_report.append(f"{months[x]} {monthly_totals[x]:.2f} Above Average")
    else:
        performance_report.append(f"{months[x]} {monthly_totals[x]:.2f} Average")
    x = x + 1

# TODO 6: Bonus challenge - Identify consecutive months with increasing sales
# Your loop code here:
# Store the length of longest streak in: longest_growth_streak (int)
# Store the starting month index in: growth_streak_start (int)
 
x = 1
longest_growth_streak = 0
growth_streak_start = 0
for num in monthly_totals:
    if num > monthly_totals[x-1]:
        longest_growth_streak +=1
        growth_streak_start = x
    

# Print final summary
print("\n" + "=" * 60)
print("QUICKMART SALES ANALYSIS SUMMARY")
print("=" * 60)
# Print your calculated results here
print(f"Best Month: {months[highest_month_index]} - ${highest_sales:.2f}")
print(f"Worst Month: {months[lowest_month_index]} - ${lowest_sales:.2f}")
print(f"Average Monthly Sales: ${average_monthly_sales:.2f}")
print(f"Best Performing Store: {best_store} - ${best_store_sales:.2f}")
print(f"Longest Growth Streak: {longest_growth_streak} starting in {months[growth_streak_start]}")