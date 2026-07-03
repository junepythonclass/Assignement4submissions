#An operator is asymbol, character or anything in a statement that tell a computer what to do with an operant.
#An operant is what an operator acts upon
#There are different types of operator in python and some on these include;

#1. ARITHMETIC OPERATORS
#These are used to perform basic mathematical operations like addition, subtraction, multiplication and division.
#Examples:
#Exponential
num1 = 15
num2 = 4
print(num1**num2)

#Modulus
print(num1 % num2)

#Floor division
print(num1 // num2)

#Division
print(num1 / num2)


#2. COMPARISON OPERATORS
#Comparison operators compare values that is; it either returns True or False according to the condition
#Examples include;

#Not equal to
print(num1 != num2)

#Greater than or equal to
print(num1 >= num2)

#less tha or equal to
print(num1 <= num2)

#3. LOGICAL OPERATORS
#These are used to combine conditional statements.
#Logical operators pperform Logical AND, Logical NOT and Logical OR
#Examples
x = True
y = False
print(x or y)
#one of the conditions above should be fullfilled or true
print(x and y)
#Both values must fullfill the condition for it to be true
print(not x)

#4. ASIGNMENT OPERATORS
#These are used to asign values to the variables
#This operator is used to asign the value of the right side to the expression on the left side operant.
#Examples
num3 = 10
num4 = num3
print(num4)
num4 += num3
print(num4)
num4 *= num3
print(num4)

#5. IDENTITY OPERATORS
#These are used to check if two values are located on the same part of the memory.
#"is" and "is not" are identity operators
#"is" True if the operands are identical
#"is not" True if the operands are not identical
#Examples
num5 = 20
num6 = 10
num7 = num5
print(num5 is not num6)
print(num5 is num7)

#6. MEMBERSHIP OPERATORS
#These are used to test whether a value or variable is in sequence.
#"in" and "not in" are membership operators
#"in" True if value is found in the sequence
#"no in" True if value is not found in the sequence
#Example
n = 14
m = 10
numbers = [10, 15, 20, 25, 30]

if (n not in numbers):
    print("n is NOT present")
else:
    print("n is present") 

if (m in numbers):
    print("m is present")
else:
    print("m is not present")


#7. TERNARY OPERATOR
#These evaluate somethin based on a condition being true or false.
#they are also known as conditional expressions
#Example
num8, num9 = 2, 4
number = num8 if num8 < num9 else num9
print(number)


# DATA TYPES
#Data types are categorizations of data.
#They define the type of value stored in a variable and determine the operations that can be performed on that data.
#Each value is associated with a specific data type in python
#Examples

#1. NUMERIC DATA TYPES
#These are used to store numeric values.
#It can be an integer, floating number or complex number

#2. SEQUENCE DATA TYPES
#A sequence is an ordered collection of item whic can be different or similar data types
#Examples of sequence data types include;

#2.1 String
#Strings are used to store text data
#It is anything that is put in quotation

#2.2 List
#Lists are ordered and mutable collections used to store multiple items in a single variale.
#Elements in a list can be different data types and are accessed using indexing.
#Examples
a = [7, 8, 9]
print(a)

names = ["brenda", "grace", "desire"]
print(names[2])

#2.3 Tuple
#Tuples are ordered and imutable collections used to store multiple items in a single variable.
#Once created, tuple elements an not be modified and accessed using indexing.

#3. Boolean Data Type
#This represents two values: True or false.
#Mainly used in conditions and comparisons.

#4. Set Data Types
#Sets are unordered and mutable collections used to store unique elements.
#Elements are accessed by iteration throuhh the set since sets are unordered.
#Example
s = {"1000", "2000", "3000", "1000", "3000", "5000", "2000"}
print(s)

#5. Dictionary Data Types
#Dictionaries are used to store data in key:value pairs.
#Each key in a dictionary must be unique and values are accessed using their keys with square brackets.

#LOOPS
#Loops are used to iterate through sequence elementd using their index values with the help of range and len
#We use continue to skip over an iteration and we use a break to stop it.
#Example
z = 5
for r in range(0, z):
    print(r)

cars = ["benz", "limo", "bmw", "subaru"]
for make in range(len(cars)):
    print(cars[make])

#while Loops
#These repeatedly execute a block of code as long as the condition remains true.
#Example
q = 0
while (q < 3):
    q = q + 1
    print("early morning")

#infinite while loopa
# #An infinite while loops runs continuously because its condition always remains true.

#Nested Loops
#A nested loop is a loop inside another loop.
#The inner loop executes completely for every iteration of the outer loop.


#CONDITIONS
#Conditional statements are used to control the flow of execution in a program based on specific conditions.
#They allow programs to execute different blocks of code depending on whether a condition evaluates to True or false.
#Example
numbers = [10, 20, 30, 40, 50, 60]
if 80 not in numbers:
    print("80 is not found")