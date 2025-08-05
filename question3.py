def factorial(n):
    # Check if the number is negative
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    # Base case for 0 or 1
    if n == 0 or n == 1:
        return 1
    # Recursive case for other numbers
    return n * factorial(n - 1)
