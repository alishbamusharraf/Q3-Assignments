#epoch used in Python

import time
epoch_time = time.time()
print("Current epoch time:", epoch_time)

#Getting the Current Time

import time
current_time = time.time()
print("Current time (seconds since epoch):", current_time)

#Getting the Formatted Time

import time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("Formatted time:", formatted_time)

#Using the datetime Module
from datetime import datetime
current_datetime = datetime.now()
formatted_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted time:", formatted_time)

#The clander
import calendar

# Display the calendar for the year 2006
print(calendar.year(2006))

import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the current date and time into a string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)

# Example of different formats
formatted_full_date = now.strftime("%A, %B %d, %Y")
print("Full formatted date:", formatted_full_date)

formatted_time = now.strftime("%I:%M %p")
print("Formatted time (12-hour):", formatted_time)


#Python Math Module

import math

# 1. Basic Mathematical Functions

# Absolute value
print("Absolute value of -5:", math.fabs(-5))  

# Power of a number (x^y)
print("2 raised to the power of 3:", math.pow(2, 3))  

# Square root
print("Square root of 16:", math.sqrt(16))  

# Logarithms
print("Logarithm base 10 of 100:", math.log(100, 10))  
print("Natural logarithm of 2:", math.log(2))  

# Exponential
print("Exponential of 2:", math.exp(2)) 


# 2. Trigonometric Functions

# Sine, Cosine, Tangent (angles in radians)
print("Sine of 30 degrees:", math.sin(math.radians(30)))  
print("Cosine of 60 degrees:", math.cos(math.radians(60)))  
print("Tangent of 45 degrees:", math.tan(math.radians(45)))  

# Inverse trigonometric functions
print("Arcsine of 0.5:", math.degrees(math.asin(0.5)))  
print("Arccosine of 0.5:", math.degrees(math.acos(0.5)))  
print("Arctangent of 1:", math.degrees(math.atan(1)))  


# 3. Rounding Functions

# Ceiling (smallest integer greater than or equal to x)
print("Ceiling of 3.14:", math.ceil(3.14))  

# Floor (largest integer less than or equal to x)
print("Floor of 3.14:", math.floor(3.14))  

# Truncation (remove decimal part)
print("Truncation of 3.14:", math.trunc(3.14))  


# 4. Factorial, Combinations, and Permutations

# Factorial of a number
print("Factorial of 5:", math.factorial(5))  

# Combinations (n choose k)
print("Combinations of 5 choose 2:", math.comb(5, 2))  

# Permutations (arrangements of k items from n items)
print("Permutations of 5 choose 2:", math.perm(5, 2))  


# 5. Constants

# Pi (π)
print("Value of Pi:", math.pi) 

# Euler's number (e)
print("Value of e:", math.e)  


# 6. Angle Conversion

# Convert degrees to radians
print("45 degrees in radians:", math.radians(45)) 

# Convert radians to degrees
print("Pi radians in degrees:", math.degrees(math.pi))  


# 7. Hyperbolic Functions

# Hyperbolic sine
print("Hyperbolic sine of 1:", math.sinh(1))  

# Hyperbolic cosine
print("Hyperbolic cosine of 1:", math.cosh(1))  

# Hyperbolic tangent
print("Hyperbolic tangent of 1:", math.tanh(1))  


#Creating NaN with float('nan')

nan_value = float('nan')
print("NaN Value:", nan_value)  # Output: nan

#Infinity

# Creating positive and negative infinity using float
positive_infinity = float('inf')
negative_infinity = float('-inf')

# Using math.inf for positive infinity
import math
positive_infinity_math = math.inf
negative_infinity_math = -math.inf

print("Positive Infinity:", positive_infinity)  
print("Negative Infinity:", negative_infinity) 
print("Positive Infinity (math):", positive_infinity_math)  
print("Negative Infinity (math):", negative_infinity_math) 
