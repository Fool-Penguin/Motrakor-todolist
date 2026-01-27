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
