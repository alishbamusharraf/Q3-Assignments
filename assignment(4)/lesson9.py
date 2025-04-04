def perform_division():
    try:
        # Taking user input for two numbers
        num1 = int(input("Enter the numerator (integer): "))
        num2 = int(input("Enter the denominator (integer): "))
        
        # Perform division
        result = num1 / num2
    
    except ValueError:
        # This block handles invalid input (e.g., non-integer input)
        print("Error: Invalid input! Please enter integers.")
    
    except ZeroDivisionError:
        # This block handles division by zero errors
        print("Error: Division by zero is not allowed.")
    
    else:
        # This block runs if no exception occurred in the try block
        print(f"The result of {num1} divided by {num2} is {result}.")
    
    finally:
        # This block will always run, regardless of whether an exception occurred or not
        print("Execution of the division operation is complete.")

# Call the function to perform the division
perform_division()

def process_file(file_name):
    try:
        # Trying to open and read the file
        with open(file_name, 'r') as file:
            data = file.read()
            # Let's simulate some processing of the file content
            if len(data) == 0:
                raise ValueError("The file is empty!")
            print("File content successfully read.")
            print("Processing data...")
            # Simulating processing, for example, we try to convert data to an integer
            processed_data = int(data.strip())
            print(f"Processed data: {processed_data}")
        
    except FileNotFoundError:
        # This block will execute if the file doesn't exist
        print(f"Error: The file '{file_name}' was not found.")
    
    except ValueError as ve:
        # This handles invalid content (like non-integer data in the file)
        print(f"Error: {ve}")
    
    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
    
    else:
        # If no exception occurred in the try block
        print("File processed successfully, no errors.")
    
    finally:
        # This block always runs, useful for cleanup actions
        print("File processing complete. Cleanup actions done.")

# User input for file name
file_name = input("Enter the name of the file to process: ")

# Call the function with the given file name
process_file(file_name)
# Example usage of the process_file function


#Python Code to Learn Error Handling
# This code demonstrates error handling in Python using try, except, else, and finally blocks.
# It includes two functions: perform_division and process_file.
# The perform_division function takes two integers as input and performs division,

def error_handling_demo():
    print("Welcome to the Python Error Handling Demo!\n")
    
    # 1. Demonstrating basic try and except
    try:
        x = 5 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    
    print("\n---\n")

    # 2. Handling multiple specific exceptions
    try:
        num = int(input("Enter a number to divide 100 by: "))  # User input for integer
        result = 100 / num
        print(f"100 divided by {num} is {result}.")
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    
    print("\n---\n")

    # 3. Using 'else' for successful execution
    try:
        num1 = int(input("Enter the numerator: "))  # User input for numerator
        num2 = int(input("Enter the denominator: "))  # User input for denominator
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input! Please enter integers.")
    else:
        print(f"The result of {num1} divided by {num2} is {result}.")
    
    print("\n---\n")

    # 4. Using 'finally' for cleanup actions
    try:
        print("Opening a file for reading...")
        file = open("sample.txt", "r")  # Trying to open a file that may not exist
        content = file.read()
        print("File content read successfully.")
        print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    finally:
        # Ensure file is closed whether the file was found or not
        try:
            file.close()
            print("File is closed.")
        except NameError:
            # If the file variable was never created (because of an error)
            print("No file to close.")
    
    print("\n---\n")

    # 5. Catching generic exceptions with 'Exception'
    try:
        number = int(input("Enter a number to square: "))
        if number < 0:
            raise Exception("Negative numbers are not allowed!")
        print(f"The square of {number} is {number**2}.")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n---\n")

    # 6. Raising custom exceptions manually
    try:
        age = int(input("Enter your age: "))
        if age < 18:
            raise ValueError("You must be at least 18 years old.")
        print(f"Your age is {age}. You are eligible!")
    except ValueError as ve:
        print(f"Error: {ve}")
    
    print("\n---\n")

    # 7. Demonstrating 'else' without 'except'
    try:
        num1 = int(input("Enter a number to double: "))
        result = num1 * 2
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")
    else:
        print(f"The doubled value is: {result}.")
    
    print("\n---\n")

# Call the function to execute the error handling demo
error_handling_demo()


#Using None as a Return Type

def no_return():
    print("This function doesn't return anything.")

result = no_return()  # result will be None
print(result)  # Output: None

# The function no_return doesn't have a return statement, so it returns None by default

#Using typing.NoReturn

from typing import NoReturn

def raise_error() -> NoReturn:
    raise ValueError("Something went wrong!")

def infinite_loop() -> NoReturn:
    while True:
        pass  # Infinite loop, never returns


#Function with No Return Type Hint 
def no_return_type():
    print("This function has no return type hint.")
