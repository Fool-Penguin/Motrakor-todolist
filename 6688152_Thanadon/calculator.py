"""Simple calculator module with basic arithmetic operations."""


def add(a, b):
    "Add two numbers."
    return a + b


def subtract(a, b):
    "Subtract two numbers."
    return a - b


def multiply(a, b):
    "Multiply two numbers."
    return a * b


def divide(a, b):
    "Divide two numbers."
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate_velocity(distance, time):
    "Calculate velocity based on distance and time"
    if time <= 0:
        raise ValueError("Time must be greater than zero")
    return distance / time


def main():
    """Interactive calculator main function."""
    print("=" * 40)
    print("Simple Calculator")
    print("=" * 40)
    
    while True:
        print("\nOperations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Calculate Velocity")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "6":
            print("Thank you for using the calculator!")
            break
        
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please try again.")
            continue
        
        try:
            if choice == "5":
                distance = float(input("Enter distance: "))
                time = float(input("Enter time: "))
                result = calculate_velocity(distance, time)
                print(f"Velocity: {result}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == "1":
                    result = add(num1, num2)
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == "2":
                    result = subtract(num1, num2)
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == "3":
                    result = multiply(num1, num2)
                    print(f"Result: {num1} × {num2} = {result}")
                elif choice == "4":
                    result = divide(num1, num2)
                    print(f"Result: {num1} ÷ {num2} = {result}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
