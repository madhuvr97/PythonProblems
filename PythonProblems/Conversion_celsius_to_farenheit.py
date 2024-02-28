def convert_celsius_to_fahrenheit(celsius):
    degree_fahrenheit = (9/5*celsius) + 32
    return degree_fahrenheit

try:
    celsius = float(input("Enter the temperature in degree celsius: "))
    degree_fahrenheit = convert_celsius_to_fahrenheit(celsius)
    print("The temperature in fahrenheit is {:.2f}.".format(degree_fahrenheit))  # Limit output to 2 decimal places
except ValueError:
    print("Invalid input. Please enter a valid number.")