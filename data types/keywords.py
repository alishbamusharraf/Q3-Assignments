# Special Keywords 
# In Python, special keywords are closely tied to various data types and operations. 

# async, await, if, elif, else, True, False, None, try, except, finally, 
# raise, global, nonlocal,import, from, as,class, def, return, yield,for, while, break, continue,and, or, not


# async, await:

import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    print("Data fetched")

async def main():
    await fetch_data()

asyncio.run(main())

# if, elif, else:

age = 18

if age < 18:
    print("Underage")
elif age >= 18 and age < 60:
    print("Adult")
else:
    print("Senior Citizen")

# True, False, None:

x = True
y = False
z = None

#  check using booleans
if x:
    print("a is True")

if not y:
    print("b is False")

# Using None to represent an absence of value
if z is None:
    print("c has no value (None)")

# try, except, finally, raise:
# using raise

def check_value(value):
    if value < 0:
        raise ValueError("Value must be non-negative")
    return value

try:
    check_value(-5)
except ValueError as a:
    print(a)  

try:
    x = 10 / 0 
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")

# for, while, break, continue:

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        continue  # Skip "banana"
    print(fruit)

count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break  

# and, or, not:

a = True
b = False

print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False


# Here's the some examples of keywords are used in python.





