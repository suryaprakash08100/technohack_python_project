def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 1.8) + 32

def main():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.1f} degree Celsius is equal to {fahrenheit:.1f} degree Fahrenheit")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for Celsius.")

if __name__ == "__main__":
    main()
