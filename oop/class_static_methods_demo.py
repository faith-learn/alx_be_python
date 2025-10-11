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
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b


# Demonstration
if __name__ == "__main__":
    # Using static method (no access to class attributes)
    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}")

    # Using class method (access to class attribute)
    product_result = Calculator.multiply(10, 5)
    print(f"Product: {product_result}")