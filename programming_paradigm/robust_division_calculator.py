# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Try converting inputs to float
        num = float(numerator)
        den = float(denominator)

        # Try performing division
        result = num / den
        
        # CORRECTED: Changed the format string to match the expected output
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        # Previous correction for the numeric error message
        return "Error: Please enter numeric values only."

# Example usage
if __name__ == "__main__":
    # Taking inputs from the user
    numerator = input("Enter numerator: ")
    denominator = input("Enter denominator: ")

    # Call the function and display result
    print(safe_divide(numerator, denominator))