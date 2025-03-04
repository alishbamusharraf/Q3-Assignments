#  7.Bitwise AND oR XOR NOT Left Shift Right Shift.

a = 5     
b = 7   
result = a & b
print(f"{a} & {b} = {result} (binary: {bin(result)})")  

# Bitwise OR
result = a | b
print(f"{a} | {b} = {result} (binary: {bin(result)})")  

# Bitwise XOR
result = a ^ b
print(f"{a} ^ {b} = {result} (binary: {bin(result)})")  

# Bitwise NOT
result = ~a
print(f"~{a} = {result} (binary: {bin(result)})")  
# Bitwise Left Shift
result = a << 2
print(f"{a} << 1 = {result} (binary: {bin(result)})")  

# Bitwise Right Shift
result = a >> 2
print(f"{a} >> 1 = {result} (binary: {bin(result)})")  