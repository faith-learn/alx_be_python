
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temperature_input = input("Enter the temperature to convert: ")
        temperature_value = float(temperature_input)
        
        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        unit_input = unit_input.strip().upper()

        if unit_input == 'F':
            converted_temp = convert_to_celsius(temperature_value)
            print(f"{temperature_value}°F is {converted_temp}°C")
        elif unit_input == 'C':
            converted_temp = convert_to_fahrenheit(temperature_value)
            print(f"{temperature_value}°C is {converted_temp}°F")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
