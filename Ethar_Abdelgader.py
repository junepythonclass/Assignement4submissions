# Putting into consideration a market vendor, with examples, discuss the concept of functions.

# A function is a block of code that performs a specific task.
# In a market, functions help a vendor perform common tasks quickly and accurately.


# Function for Calculating the Cost of Items
# Problem:
# A customer buys several kilograms of onions.
# The vendor needs a quick way to calculate the total amount.

def calculate_cost(price_per_kg, kilograms):
    total = price_per_kg * kilograms
    print("Amount to Pay:", total)

# Example:
# Onions cost 2,500 UGX per kilogram.
# Customer buys 6 kilograms.

calculate_cost(2500, 6)

# Output:
# Amount to Pay: 15000



# Function for Applying a Discount
# Problem:
# The vendor gives loyal customers a discount.

def apply_discount(total_bill, discount):
    final_bill = total_bill - discount
    print("Final Bill:", final_bill)

# Example:
# Total bill is 30,000 UGX.
# Discount is 2,000 UGX.

apply_discount(30000, 2000)

# Output:
# Final Bill: 28000



# Function for Calculating Change
# Problem:
# The customer pays more than the total bill.
# The vendor calculates the remaining balance.

def give_change(amount_paid, bill):
    balance = amount_paid - bill
    print("Balance:", balance)

# Example:
# Customer pays 50,000 UGX.
# Bill is 42,000 UGX.

give_change(50000, 42000)

# Output:
# Balance: 8000



# Function for Displaying Purchase Details
# Problem:
# The vendor wants to show the customer what they purchased.

def display_purchase(item, quantity, total):
    print("Purchase Details")
    print("Product:", item)
    print("Quantity:", quantity)
    print("Amount:", total)

# Example:
# Customer buys 5 bunches of bananas for 10,000 UGX.

display_purchase("Bananas", 5, 10000)

# Output:
# Purchase Details
# Product: Bananas
# Quantity: 5
# Amount: 10000