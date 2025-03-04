# 5.Identity Operators: is, is not

a = [7, 3, 7]  
b = a         
c = [7, 7, 9]   

# is operator
result = a is b  
print(f"a is b: {result}")

result = a is c  
print(f"a is c: {result}")

# is not operator
result = a is not b  
print(f"a is not b: {result}")

result = a is not c  
print(f"a is not c: {result}")