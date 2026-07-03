#A function is a named reusable block of code that performs a specific task.
# Instead of writing the same code many times, you write it once inside a function and call it whenever you need it.
# Functions are self contained and they are used in a process.

#Imagine a market vendor who sells fruits. Every time a customer comes, the vendor follows the same process:

#1. Greets the customer.
#2. Weighs the fruits.
#3. Calculates the total cost.
#4. Receives payment.
#5. Gives the customer their change.

#The vendor repeats these steps for every customer. 
# Rather than learning the process again each time, the vendor simply follows the same routine. 
# In programming, this routine is called a function.

#Examples; calculate the total amount of the tomatoes 

#dynamic function
# you can reuse the function without entering the function to change it, 
# by changing the arguments that correspond to the paraments given.
def total_amount(quantity, unit_amount):
    amount = quantity * unit_amount
    print(amount)

total_amount(8, 1500)
total_amount(2, 9000)

#Example 2
def toma(quantity):
    print(quantity * 2000)

toma(10)

#static function
# To do any chnage you must enter the function, if you are to reuse it.
#Example 1
def login():
    user_name = input("enter name")
    user_ID = input("enter ID")
    login_details = user_name, user_ID
    print(login_details)

login()

#Example 2
def tomatoes():
    print(2000)

tomatoes()


# Applicability of functions in relation to one another using a market example;

#Example
# total bill of items bought from the market.
def individual_price(quantity1, unit_amount2):
    amount2  =  quantity1 * unit_amount2
    print(amount2)
    return amount2

eggs = individual_price(13, 1500)
bananas = individual_price(12, 1200)
melon = individual_price(5, 2000)
salt = individual_price(5, 1000)
grand_total = eggs + bananas + melon + salt

print("Grand_total:", grand_total)

#Example 2
#stock before a sale
def check_stock(stock):
    invent = stock > 0 
    return invent

def sell_item():
    print("Sale completed")

check_stock(10)
sell_item()