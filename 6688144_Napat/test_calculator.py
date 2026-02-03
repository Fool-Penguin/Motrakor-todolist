"""
Unit tests for the Simple Calculator Module
"""

import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    """Test cases for the add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2, -3) == -5
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(5, -3) == 2
    
    def test_add_zeros(self):
        """Test adding zeros."""
        assert add(0, 0) == 0
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    """Test cases for the subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(5, 3) == 2
    
    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        assert subtract(-2, -3) == 1
    
    def test_subtract_mixed_numbers(self):
        """Test subtracting positive and negative numbers."""
        assert subtract(5, -3) == 8
    
    def test_subtract_zeros(self):
        """Test subtracting zeros."""
        assert subtract(0, 0) == 0
    
    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0


class TestMultiply:
    """Test cases for the multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(3, 4) == 12
    
    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        assert multiply(-3, -4) == 12
    
    def test_multiply_mixed_numbers(self):
        """Test multiplying positive and negative numbers."""
        assert multiply(3, -4) == -12
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
    
    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        assert multiply(2.5, 4.0) == 10.0


class TestDivide:
    """Test cases for the divide function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide(10, 2) == 5
    
    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        assert divide(-10, -2) == 5
    
    def test_divide_mixed_numbers(self):
        """Test dividing positive and negative numbers."""
        assert divide(10, -2) == -5
    
    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        assert divide(10.0, 2.5) == 4.0
    
    def test_divide_by_zero(self):
        """Test dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
