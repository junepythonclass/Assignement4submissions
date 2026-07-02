#The Concept of a Function (Using a Ugandan Market Vendor)
#example
'''
In mathematics, a function is what we use to assign one outcome to a input.
This means that every input has only one corresponding result.
'''

#lets take a market vender selling tomatoes
'''
Suppose the vendor sells 1 kilogram of tomatoes for UGX 4,000. 
The total cost depends on the number of kilograms a customer buys
i.e.
if 
f(x) = 4000x
where
x = number of kilograms bought
f(x) = total cost in Uganda shillings

Input (Domain): Number of kilograms bought (x)
Output (Range): Total amount paid (f(x))
'''
#In Python
'''
A function is a reusable block of code that performs a specific task. 
Instead of writing the same code many times,
you write it once inside a function and call it whenever you need it.
'''
#example 
#uisng a market vender selling tomatoes again
'''
lets say a Ugandan market vendor sells tomatoes at UGX 4,000 per kilogram.
We can create a Python function to calculate the total cost.
'''
#the function
def calculate_cost(kilograms):
    price_per_kg = 4000
    total = kilograms * price_per_kg
    return total

print(calculate_cost(3)) #= 12000

#explanation
'''
def is the keyword used to create a function.
calculate_cost is the function name.
kilograms is the input (parameter).
return gives back the total cost.
3 is the argument(value corresponding to the parameter)
'''

#example2
#lets calculate the cost of bananas
'''
if the vendor is selling one bunch of bananas for UGX 8,000.
'''
#the function
def banana_cost(bunches):
    return bunches * 8000

print(banana_cost(2)) #= 16000

#explanation
'''
def is the keyword used to create the function.
bunches is the parameter
banana_cost is the function name.
return will gives us back the total cost.
2 is the argument(value corresponding to the parameter)
'''

#reasons why functions are important in python
'''
Functions help programmers to;
  reuse code without writing it repeatively
  simplify ccode making easy to read through
  save time that would be used to rewrite code
  ease editing of code so we can make changes
'''

#in a nutshell
'''
a function is a named block of reusable code 
that performs a specific task and can accept inputs (parameters)
and return an output. 
Python function can repeatedly calculate prices quickly and 
accurately without having to rewriting the same code.
'''
