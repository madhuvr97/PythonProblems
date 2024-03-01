class Converter:
    @staticmethod
    def km_to_mile(kms):
        """
        Convert kilometers to miles.

        Parameters:
        - kms: The distance travelled in kilometers.

        Returns:
        - The distance travelled in miles.
        """
        return 0.621371 * kms

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """
        Convert Celsius to Fahrenheit.

        Parameters:
        - celsius: The temperature in Celsius.

        Returns:
        - The temperature in Fahrenheit.
        """
        return (celsius * 9 / 5) + 32


try:
    choice = int(input("Enter 1 to convert kilometers to miles, 2 to convert Celsius to Fahrenheit: "))

    if choice == 1:
        kms = float(input("Enter the distance travelled in kilometers: "))
        if kms < 0:
            print("Distance travelled cannot be negative.")
        else:
            miles = Converter.km_to_mile(kms)
            print("You have travelled {:.2f} miles.".format(miles))

    elif choice == 2:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = Converter.celsius_to_fahrenheit(celsius)
        print("Temperature in Fahrenheit: {:.2f}".format(fahrenheit))

    else:
        print("Invalid choice. Please enter either 1 or 2.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
