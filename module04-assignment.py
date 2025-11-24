# Module 4 Assignment: Conditional Logic in Business Decision-Making
# FastFunds Financial - Loan Approval System

# Welcome message
print("=" * 60)
print("FASTFUNDS FINANCIAL - BUSINESS LOAN EVALUATION SYSTEM")
print("=" * 60)

# In a real system, you would collect this information through input()
# For this assignment, we'll use predefined variables for testing
# IMPORTANT: Do not modify these variable names or types
business_name = "TechSolutions Inc."
years_in_operation = 3.5
annual_revenue = 280000
credit_score = 690
requested_amount = 150000
business_type = "Technology"  # Options: "Retail", "Service", "Manufacturing", "Technology"

# Display the application details
print(f"\nLOAN APPLICATION DETAILS:")
print(f"Business Name: {business_name}")
print(f"Years in Operation: {years_in_operation:.1f} years")
print(f"Annual Revenue: ${annual_revenue:,.2f}")
print(f"Credit Score: {credit_score}")
print(f"Requested Loan Amount: ${requested_amount:,.2f}")
print(f"Business Type: {business_type}")
print("\nPROCESSING APPLICATION...")

# TODO 1: Check if applicant meets basic eligibility requirements
# Implement the rules for basic eligibility using if-else statements
# Store result in: meets_basic_requirements (bool)
# Also store reasons for any failures in: eligibility_reasons (list)

eligibility_reasons = []

if years_in_operation >= 2:
    meets_basic_requirements = True
else:
    meets_basic_requirements = False
    eligibility_reasons.append("Years in Operation")
    
if annual_revenue >= 100000:
    meets_basic_requirements = True
else:
    meets_basic_requirements = False
    eligibility_reasons.append("Annual Revenue")

if credit_score >= 600:
    meets_basic_requirements = True
else:
    meets_basic_requirements = False
    eligibility_reasons.append("Credit Score")

if requested_amount >= 25000 and requested_amount <= 500000:
    meets_basic_requirements = True
else:
    meets_basic_requirements = False
    eligibility_reasons.append("Requested Loan Amount")

    

     
# TODO 2: Determine risk assessment tier (Low, Medium, High, Very High)
# Use nested conditionals or logical operators to implement the risk assessment rules
# Store result in: risk_tier (string)
risk_tier = "Very High"
if meets_basic_requirements and years_in_operation >= 5 and credit_score >= 720 and annual_revenue >= 300000:
    risk_tier = "Low"
elif meets_basic_requirements and years_in_operation >= 3 and credit_score >= 650 and annual_revenue >= 150000:
    risk_tier = "Medium"
elif meets_basic_requirements:
    risk_tier = "High"

# TODO 3: Calculate maximum approvable loan amount based on risk tier
# Implement the loan amount approval rules
# Store result in: max_loan_amount (float)

if risk_tier == "High":
    max_loan_amount = 50%  annual_revenue
elif risk_tier == "Very High":
    max_loan_amount = 25%  annual_revenue
else:
    max_loan_amount = 80%  annual_revenue

# TODO 4: Apply industry-specific considerations
# Implement additional criteria based on business type
# Store result in: passes_industry_check (bool)
# Store any industry-specific reasons in: industry_reasons (list)

industry_reasons = []

if business_type.lower() == "retail":
    if years_in_operation < 3:
        if max_loan_amount > 150000:
            passes_industry_check = False
            industry_reasons.append("Years in Operation")
        else:
            passes_industry_check = True
    else:
        passes_industry_check = True
if business_type.lower() == "service":
    if credit_score < 650:
        if max_loan_amount >200000:
            passes_industry_check = False
            industry_reasons.append("Credit Score")
        else:
            passes_industry_check = True
    else:
        passes_industry_check = True
if business_type.lower() == "manufacturing":
    if annual_revenue < 250000:
        passes_industry_check = False
        industry_reasons.append("Annual Revenue")
    else:
        passes_industry_check = True
if business_type.lower() == "technology":
    if years_in_operation < 3:
        if credit_score >= 700:
            passes_industry_check = True
        else:
            passes_industry_check = False
            industry_reasons.append("Credit Score")
    else:
        passes_industry_check = True
        
# TODO 5: Determine applicable interest rate
# Implement interest rate determination rules based on risk tier and business type
# Store result in: interest_rate (float)

if risk_tier == "Low":
    interest_rate = 6
elif risk_tier == "Medium":
    interest_rate = 8
elif risk_tier == "High":
    interest_rate = 11
else:
    interest_rate = 14
if business_type.lower() == "techonology":
    interest_rate = interest_rate - 0.5
if business_type.lower() == "manufacturing" and years_in_operation < 3:
    interest_rate = interest_rate + 0.5
    
# TODO 6: Make final decision (Approved, Conditionally Approved, or Denied)
# Combine all the previous assessments to make a final decision
# Store result in: decision (string)
# Store final approved amount in: approved_amount (float)

if meets_basic_requirements and passes_industry_check and max_loan_amount >= requested_amount:
    decision = "APPROVED"
elif meets_basic_requirements and passes_industry_check:
    decision = "CONDITIONALLY APPROVED"
else:
    decision = "DENIED"
 
print(f"\n \n \n \n \n")
print("=" *5 + f"LOAN DECISION" +"=" *5)
print(f"Decision: {decision}")
print(f"Risk Assessment: {risk_tier} Risk \n ")
print(f"Loan Details:")
print(f"- Requested Amount: ${requested_amount}")
print(f"- Approved Amount: ${max_loan_amount}")
print(f"- Interest Rate: {interest_rate}%  \n")
print(f"Reasons: {eligibility_reasons}, {industry_reasons}")
print(f" \n Recommendations:")
# TODO 7: Generate and display detailed response
# Output the final decision with explanations, including reasons and recommendations
# Use the exact format shown in the Required Output Format section