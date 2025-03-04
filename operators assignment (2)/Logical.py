# 4. Logical Operators :  and, or, not


x = 10
y = 5
z = 20

# and operator
result = (x > y) and (z > x)  
print(f"(x > y) and (z > x): {result}")

result = (x < y) and (z > x)  
print(f"(x < y) and (z > x): {result}")

# or operator
result = (x > y) or (z < x) 
print(f"( x > y) or (z < x): {result}")

result = (x < y) or (z < x)  
print(f"(x < y) or (z < x): {result}")

# not operator
result = not(X > Y)  
print(f"not(x > y): {result}")

result = not(x < y) 
print(f"not(x < y): {result}")
