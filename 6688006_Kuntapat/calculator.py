"""
Simple Calculator Module

This module provides basic arithmetic operations: add, subtract, multiply, and divide.
"""


def add(a, b):
    """Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b


def subtract(a, b):
    """Subtract two numbers and return the result.
    
    Args:
        a: First number
        b: Second number to subtract from a
    
    Returns:
        The difference (a - b)
    """
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The product of a and b
    """
    return a * b


def divide(a, b):
    """Divide two numbers and return the result.
    
    Args:
        a: Dividend (numerator)
        b: Divisor (denominator)
    
    Returns:
        The quotient (a / b)
    
    Raises:
        ValueError: If b is zero (division by zero)
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def velocity(distance, time):
    """Calculate velocity given distance and time.
    
    Args:
        distance: The distance traveled
        time: The time taken
    
    Returns:
        The velocity (distance / time)
    
    Raises:
        ValueError: If time is zero (division by zero)
    """
    if time == 0:
        raise ValueError("Time cannot be zero")
    return distance / time