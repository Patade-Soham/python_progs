def divide_numbers():
    try:
        # Taking input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Performing division
        result = num1 / num2
        print(f"Result of division: {result}")
    
    except ValueError:
        print("Error: Invalid input! Please enter numeric values.")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        print("Program execution completed.")

# Run the function
divide_numbers()
