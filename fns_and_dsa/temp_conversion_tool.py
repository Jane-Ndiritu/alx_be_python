FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def  convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp = input("Enter the temperature to convert:")
scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
if temp.endswith("F"):
    fahrenheit = float(temp[:-1])
    celsius = convert_to_celsius(fahrenheit)
    print(f"{fahrenheit}F is {celsius:.2f}C")
elif temp.endswith("C"):
    celsius = float(temp[:-1])
    fahrenheit = convert_to_fahrenheit(celsius)
    print(f"{celsius}C is {fahrenheit:.2f}F")
else:
    print("Invalid input format.")