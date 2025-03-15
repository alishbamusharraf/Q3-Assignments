# The if Statement

age = 18
if age >= 18:
    print("you are an adult")


 # The else Statement

age = 17
if age >= 18:
    print("you are an adult")  
else:
    print("you are a minor")


 # The elif Statement 

age = 18    
if age >= 18:
    print("you are an adult")
elif age == 17:
    print("you are a minor")
else:
    print("you are a child")

# Nested if Statements

age = 70
if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are not a senior citizen.")
else:
    print("You are a minor.")


# for loop with else (No break)

numbers = [10, 20, 30, 40, 50]
target = 35

for number in numbers:
    if number == target:
        print(f"{target} found in the list!")
        break
else:
    print(f"{target} not found in the list.")


#for loop with break (Skipping else)

numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:
    if number == target:
        print(f"{target} found in the list!")
        break
else:
    # This block will be skipped because of the 'break'
    print(f"{target} not found in the list.")


# Searching with else

numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:
    if number == target:
        print(f"{target} found in the list!")
        break  # Exit the loop as soon as the target is found
else:
    # This block will be executed if the loop completes without finding the target
    print(f"{target} not found in the list.")


# Thw while loop

counter = 1

while counter <= 5:
    print(f"Counter: {counter}")
    counter += 1  # Increment the counter to avoid an infinite loop

# Controlling loops

#break 
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop!")
        break  # Exit the loop when i equals 5
    print(i)

#continue
for i in range(1, 10):
    if i == 5:
        print("Skipping the iteration!")
        continue  # Skip the rest of the code block and continue with the next iteration
    print(i)

# Nested loops   

for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i: {i}, j: {j}")






