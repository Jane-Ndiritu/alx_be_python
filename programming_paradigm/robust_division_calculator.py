def safe_divide(numerator, denominator):
    """Safely divides two numbers with error handling."""
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            return "Cannot divide by zero"
        return f"The result of the division is {numerator / denominator}"

    except ValueError:
        return "Error: Invalid input"
