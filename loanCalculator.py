# Get details of loan payments
money_owed = float(input("How much money you owe in dollars?\n")) # e.g., $50,000.00
apr = float(input("What is the annual percentage rate of the loan (APR)?\n")) # e.g., 3.92 for 3.92%
payments_per_month = float(input("How much will you pay off each month in dollars?\n")) # e.g., $1,000.00 per month
months = int(input("How many months do you want to see the results for ?\n")) # e.g., 24 months

monthly_interest_rate = apr / 100 / 12 # convert APR percentage to a decimal and get monthly rate
total_paid = 0.0 # initialize total paid

for i in range(months):
    # Calculate interests to pay each month
    interest_paid = money_owed * monthly_interest_rate

    # Add in interest
    money_owed = money_owed + interest_paid

    # Make payment
    money_owed = money_owed - payments_per_month
    total_paid = total_paid + payments_per_month

print('paid', payments_per_month, 'of which', interest_paid, 'was interest', end='')
print('Now I owe', money_owed, 'with total paid of', total_paid)

