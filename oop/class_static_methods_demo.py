# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: works like a normal function but inside a class.
        It does not access class or instance attributes."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: has access to the class (cls).
        It can use class attributes and modify them if needed."""
        # CORRECTED: Changed 'Type' to lowercase 'type' to match expected output
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Demonstration
if __name__ == "__main__":
    # Using static method (no access to class attributes)
    sum_result = Calculator.add(10, 5)
    # CORRECTED: Changed print statement to "The sum is: 15"
    print(f"The sum is: {sum_result}")

    # Using class method (access to class attribute)
    product_result = Calculator.multiply(10, 5)
    # CORRECTED: Changed print statement to "The product is: 50"
    print(f"The product is: {product_result}")