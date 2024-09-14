# Loan calculator

print('Welcome to the Loan Calculator!')

loan_amount = float(input('What is the loan amount? '))

loan_duration_years = float(input('How many years for the loan? '))

apr = float(input('What is the loan APR? ')) * 0.01

monthly_interest_rate = apr / 12
loan_duration_months = loan_duration_years * 12

MONTHLY_PAYMENT = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-loan_duration_months)))

print(f'Your monthly payment will be ${MONTHLY_PAYMENT:.2f}.')