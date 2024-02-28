def convert_km_to_mile(kms):
    """
    Convert kilometers to miles.

    Parameters:
    - kms: The distance travelled in kilometers.

    Returns:
    - The distance travelled in miles.
    """
    miles = 0.62 * kms
    return miles


try:
    kms = float(input("Enter the distance travelled in kilometers: "))
    if kms < 0:
        print("Distance travelled cannot be negative.")
    else:
        miles = convert_km_to_mile(kms)
        print("You have travelled {:.2f} miles.".format(miles))  # Limit output to 2 decimal places
except ValueError:
    print("Invalid input. Please enter a valid number.")
