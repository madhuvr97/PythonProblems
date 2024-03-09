try:
    # Input validation
    a = int(input("Enter number1: "))
    b = int(input("Enter number2: "))

    # Swap the values using tuple unpacking
    a, b = b, a

    print(f"The value of a after swapping is {a}")
    print(f"The value of b after swapping is {b}")
except ValueError:
    print("Invalid input. Please enter valid integers.")
