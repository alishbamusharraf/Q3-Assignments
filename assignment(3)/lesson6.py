# Working with Lists and Tuples

# Accessing List Elements
numbers = [1, 2, 3, 4, 5]

print(numbers[0]) 
print(numbers[-1])  
print(numbers[-2])  

# Modifying List Elements
numbers[0] = 10
print(numbers)  

# Adding an element at the end of the list
numbers.append(6)
print(numbers) 
# Inserting an element at a specific position
numbers.insert(1, 20)  
print(numbers)  

# List Methods

# Removing an element by value
numbers.remove(20)
print(numbers)  

# Popping the last element
last = numbers.pop() 
print(last)    
print(numbers)  

# Slicing Lists

# Slicing a list
subset = numbers[1:4]  # Gets elements from index 1 to 3
print(subset)  

# Slicing with step
step_subset = numbers[::2]  # Every second element
print(step_subset)  

#List Comprehension

# Example of a list comprehension
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  

# Length of a List

length = len(numbers)
print(length)  

# Nested Lists
 
# Example of a nested list
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][1])  

# Tuples in Python

# Creating a tuple
my_number = (1, 2, 3)

# Accessing Elements
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  

# Slicing a tuple
print(my_tuple[1:3])  

# Immutability

my_number = (1, 2, 3)
my_number[0] = 10  

# Tuple Operations

# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result) 

# Repetition
result = tuple1 * 3
print(result) 

# Membership check
print(3 in tuple1)  

# Tuple Unpacking

# Define a tuple
person = ("Alishba", 18, "musharraf ali")

# Unpack the tuple into variables
name, age, fatherName = person

# Print the unpacked values
print(name)        
print(age)         
print(fatherName)  

#  Nested Tuples

person = ("Alishba", (18,), ("Python", "JavaScript"))

# Accessing elements
name = person[0]
age, = person[1]
skills = person[2]

print(name)        
print(age)       
print(skills)    

# Tuple Methods

my_tuple = (1, 2, 3, 2, 4, 2)
count = my_tuple.count(2)
print(count) 
my_tuple = (10, 20, 30, 20, 40)
index = my_tuple.index(20)
print(index)  

# Dictionaries in Python
#Creating a Dictionary

# Using curly braces
my_dict = {"name": "Alishba", "age": 18, "profession": "Web Developer"}

# Using dict() constructor
my_dict = dict(name="Alishba", age=18, profession="Web Developer")

print(my_dict)

# Accessing Values

my_dict = {"name": "Alishba", "age": 18, "profession": "Web Developer"}

# Access values
name = my_dict["name"]
age = my_dict["age"]

print(name) 
print(age)  

my_dict = {"name": "Alishba", "age": 18, "profession": "Web Developer"}

# Access values
name = my_dict.get("name")
location = my_dict.get("location", "nazimaabad")

print(name)     
print(location) 

# Modifying a Dictionary

my_dict = {"name": "Alishba", "age": 18}

# Update with another dictionary
my_dict.update({"profession": "Web Developer", "location": "nazimaba"})

# Update with an iterable of key-value pairs
my_dict.update([("age", 19), ("hobby", "cooking,coding,driving")])

print(my_dict)

# Deleting Items

my_dict = {"name": "Alishba", "age": 18, "profession": "Web Developer"}

# Delete the key "age"
del my_dict["age"]

print(my_dict)

# Iterating Over a Dictionary

# Example dictionary
my_dict = {'name': 'Alishba', 'age': 18, 'city': 'karachi'}

# Iterating over keys
for key in my_dict:
    print(key)

# Practical example :
# Building a Phonebook:
 
 # Initialize phonebook
phonebook = {}

# Function to add a contact
def add_contact(name, number):
    phonebook[name] = number
    print(f"Contact '{name}' added successfully!")

# Function to update a contact
def update_contact(name, number):
    if name in phonebook:
        phonebook[name] = number
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

# Function to delete a contact
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

# Function to search for a contact
def search_contact(name):
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"Contact '{name}' not found.")

# Function to display all contacts
def display_contacts():
    if phonebook:
        print("Phonebook Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("Your phonebook is empty.")

# Phonebook menu
def phonebook_menu():
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Display All Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            add_contact(name, number)
        elif choice == "2":
            name = input("Enter name: ")
            number = input("Enter new phone number: ")
            update_contact(name, number)
        elif choice == "3":
            name = input("Enter name: ")
            delete_contact(name)
        elif choice == "4":
            name = input("Enter name: ")
            search_contact(name)
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            print("Exiting phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the phonebook application
if __name__ == "__main__":
    phonebook_menu()