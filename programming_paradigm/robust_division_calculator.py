# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Try converting inputs to float
        num = float(numerator)
        den = float(denominator)

        # Try performing division
        result = num / den
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        # Corrected error message to match the expected output exactly.
        return "Error: Please enter numeric values only."

# Example usage
if __name__ == "__main__":
    # Taking inputs from the user
    numerator = input("Enter numerator: ")
    denominator = input("Enter denominator: ")

    # Call the function and display result
    print(safe_divide(numerator, denominator))