#Putting into consideration a market vender, with examples, discuss the concept of functions




#2. Function for Calculating the Total Cost
#Problem
#Customers buy different quantities of fruits.
#Instead of calculating manually every time, market vender can use a function.
def calculate_total(price, quantity):
    total = price * quantity
    print("Total is:", total)
#Example
#Tomatoes cost 3,000 UGX.
#Customer buys 4 kilograms.

calculate_total(3000,8)

#Output

#Total is: 12000



#Function for Printing a Receipt
#Problem
#Customers want to know what they bought.

def print_receipt(item, quantity, total):
    print("Receipt")
    print("Item:", item)
    print("Quantity:", quantity)
    print("Total:", total)
#Example
print_receipt("Tomatoes",3,9000)

#Output
#Receipt
#Item: Tomatoes
#Quantity: 3
#Total: 9000



#Function for Giving Change
#Problem
#Customers rarely pay the exact amount.
#market vender needs to calculate change quickly.

def calculate_change(amount_paid, total):
    change = amount_paid - total
    print("Change:", change)
#Example
#Customer pays
#20,000 UGX
#Bill is
#15,000 UGX
calculate_change(20000, 15000)
#Output
#Change: 5000



#Function for Calculating the Total Cost
#Problem
#Customers buy different quantities of fruits.
#Instead of calculating manually every time, Sarah can use a function.
def calculate_total(price, quantity):
    total = price * quantity
    print("Total is:", total)
#Example
#Tomatoes cost 3,000 UGX.
#Customer buys 4 kilograms.
calculate_total(3000,4)
#Output
#Total is: 12000