# 6.Membership Operators: in, not in

# List example
fruits = ["apple", "banana", "cherry", "date"]

# in operator
result = "banana" in fruits  
print(f"'banana' in fruits: {result}")

result = "mango" in fruits  
print(f"'mango' in fruits: {result}")

# not in operator
result = "apple" not in fruits  
print(f"'apple' not in fruits: {result}")

result = "orange" not in fruits  
print(f"'orange' not in fruits: {result}")

# String example
sentence = "Python is fun!"

# in operator with string
result = "Python" in sentence  
print(f"'Python' in sentence: {result}")

result = "java" in sentence  
print(f"'java' in sentence: {result}")

# not in operator with string
result = "fun" not in sentence  
print(f"'fun' not in sentence: {result}")

result = "ruby" not in sentence 
print(f"'ruby' not in sentence: {result}")
