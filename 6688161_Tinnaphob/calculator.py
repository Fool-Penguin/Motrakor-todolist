"""Simple calculator module supporting basic arithmetic operations.

This module provides a Calculator class that supports add, subtract,
multiply, and divide operations with error handling.
"""


class Calculator:
    """A simple calculator for basic arithmetic operations.

    Supports addition, subtraction, multiplication, and division
    with built-in error handling.
    """

    def __init__(self):
        """Initialize the calculator with last result as 0."""
        self.last_result = 0

    def add(self, a: float, b: float) -> float:
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The sum of a and b
        """
        self.last_result = a + b
        return self.last_result

    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers.

        Args:
            a: First number (minuend)
            b: Second number (subtrahend)

        Returns:
            The difference of a and b
        """
        self.last_result = a - b
        return self.last_result

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The product of a and b
        """
        self.last_result = a * b
        return self.last_result

    def divide(self, a: float, b: float) -> float:
        """Divide two numbers.

        Args:
            a: First number (dividend)
            b: Second number (divisor)

        Returns:
            The quotient of a and b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.last_result = a / b
        return self.last_result

    def get_last_result(self) -> float:
        """Get the last calculation result.

        Returns:
            The last result stored
        """
        return self.last_result


def calculate_velocity(distance: float, time: float) -> float:
    """Calculate velocity given distance and time.

    Velocity is calculated using the formula: velocity = distance / time

    Args:
        distance: The distance traveled (in any unit of length)
        time: The time taken (in any unit of time)

    Returns:
        The velocity (distance per unit time)

    Raises:
        ValueError: If time is zero or negative
    """
    if time <= 0:
        raise ValueError("Time must be greater than zero")
    return distance / time


def main() -> None:
    """Run an interactive calculator in the terminal."""
    calc = Calculator()
    print("=" * 50)
    print("Simple Calculator")
    print("=" * 50)
    print("Commands: add, subtract, multiply, divide, velocity, result, clear, exit")
    print()

    while True:
        try:
            command = input("Enter command: ").strip().lower()

            if command == "exit":
                print("Goodbye!")
                break

            elif command == "clear":
                calc = Calculator()
                print("Calculator cleared. Last result reset to 0.")

            elif command == "result":
                print(f"Last result: {calc.get_last_result()}")

            elif command in ["add", "subtract", "multiply", "divide"]:
                try:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))

                    if command == "add":
                        result = calc.add(a, b)
                    elif command == "subtract":
                        result = calc.subtract(a, b)
                    elif command == "multiply":
                        result = calc.multiply(a, b)
                    elif command == "divide":
                        result = calc.divide(a, b)

                    print(f"Result: {result}")
                except ValueError as e:
                    print(f"Error: {e}")

            elif command == "velocity":
                try:
                    distance = float(input("Enter distance: "))
                    time = float(input("Enter time: "))
                    result = calculate_velocity(distance, time)
                    print(f"Velocity: {result}")
                except ValueError as e:
                    print(f"Error: {e}")

            else:
                print("Unknown command. Try: add, subtract, multiply, divide, velocity, result, clear, exit")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
