# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services
services = {"Graphic Design": 130, "Data Analytics": 150, "Website Development":200, "Promotional Content": 145, "General IT": 100}

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {"company_name": "Green Goat Co", "contact_person": "Choi Seungcheol", "email": "s.coups@ggc.com", "phone": "407-017-0525"}
customer2 = {"company_name": "Yellow Tiger LLC", "contact_person": "Kwon Soonyoung", "email": "hoshi@yellowtiger.com", "phone": "407-017-0915"}
customer3 = {"company_name": "Red Ram Inc", "contact_person": "Lee Jihoon", "email": "woozi@redraminc.com", "phone": "407-017-0914"}
customer4 = {"company_name": "Blue Bat Group", "contact_person": "Lee Seokmin", "email": "dk.dokyeom@bluebat.com", "phone": "407-017-0218"}

# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}
customers = {"C001": customer1, "C002": customer2, "C003": customer3, "C004": customer4}
# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
print(customers)
# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here
c002_info = customers["C002"]
print(c002_info)
c003_contact = customers["C003"]["contact_person"]
print(c003_contact)
c999_info = customers.get("C999", "customer not found")
print(c999_info)
# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here
customers["C001"]["phone"] = "407-017-0808"
customers["C002"]["industry"] = "Music"
print(customers)
# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}

print("\n\nProject Information:")
print("-" * 60)
# Add your code here
project1 = {"name": "Hype Vibes", "service": "Graphic Design", "hours": 12, "budget": 17000}
project2 = {"name": "horanghae", "service": "Website Development", "hours": 17, "budget": 1400}
project3 = {"name": "HxW Beam", "service": "Data Analytics", "hours": 13, "budget": 1500}
project4 = {"name": "CBZ Prime Time", "service": "Promotional Content", "hours": 10, "budget": 4000}
project5 = {"name": "HBD", "service": "General IT", "hours": 80, "budget": 800000}
projects = {"C001": [project1], "C002": [project2], "C003": [project3, project5], "C004": [project4]}
print(projects)
# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
for clist in projects.values():
    for ctr in clist:
        rate = services[ctr["service"]]
        ctr["cost"] = rate * ctr["hours"]
        print(ctr["name"], "-->", ctr["cost"])
# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here
print(list(projects.keys()))
print(list(projects.values()))
print(len(projects))
# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here
service_counts = {}
for plist in projects.values():
    for p in plist:
        service = p["service"]
        service_counts[service] = service_counts.get(service,0) + 1
print(service_counts)
# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here
total_hours = sum(p["hours"] for clist in projects.values() for p in clist)
print(f"Total Hours:", total_hours)
total_budget = sum([q["budget"] for clist in projects.values() for q in clist])
print("Total Budget:", total_budget)
avg_budget = total_budget/(len(projects)+1)
print(avg_budget)
budget = [x["budget"] for clist in projects.values() for x in clist]
max_budget = max(budget)
print(max_budget)
min_budget = min(budget)
print(min_budget)
# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)
# Add your code here
for cid, plist in projects.items():
    totalBudget = sum(p["budget"] for p in plist)
    totalHours = sum(p["hours"] for p in plist)
    print(f"Customer: {cid}, total budget: {totalBudget}, total hours: {totalHours}")
# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
print(adjusted_rates)
# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects

print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
active_customers = {cid: customers[cid] for cid in projects if cid in customers}
print(active_customers)
# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
customer_budgets = {}
for cid, plist in projects.items():
    ctrBudget = sum(p["budget"] for p in plist)
    customer_budgets[cid] = ctrBudget
print(customer_budgets)
# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension

print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
service_tiers = {}
for item in services:
    if services[item] < 100:
        service_tiers[item] = "Basic"
    if services[item] >= 100 and services[item] <= 199:
        service_tiers[item] = "Standard"
    if services[item] >= 200:
        service_tiers[item] = "Premium"
print(service_tiers)
# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
def validate_customer(customers):
    required = {"company_name", "contact_person", "email", "phone"}
    return required.issubset(customers.keys())
for cid, cdata in customers.items():
    print(cid, validate_customer(cdata))


# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses

print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here
project1["status"] = "active"
project2["status"] = "completed"
project3["status"] = "pending"
project4["status"] = "completed"
project5["status"] = "active"
status_counts = {}
status_counts["active"] = 2
status_counts["completed"] = 2
status_counts["pending"] = 1
print(status_counts)
# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
def analyze_customer_budgets(projects):
    cbud = {"C001" : 0, "C002" : 0, "C003": 0, "C004" : 0}
    total_bud = 0
    for clist in projects.values():
        for ct in clist:
            total_bud += ct["budget"]
            average_bud = total_bud / 2
            for cid in customers:
                cbud[cid] = [total_bud, average_bud]
    print(cbud)
print(analyze_customer_budgets(projects))        
# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations

print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
def recommended_services(customer_id, customers, projects, services):
    pass