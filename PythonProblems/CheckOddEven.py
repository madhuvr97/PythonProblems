try:
    num = int(input("Enter a number: "))

    if num > 0 and num % 2 == 0:
        print("The number you entered is positive and is even.")
    elif num > 0 and num % 2 == 1:
        print("The number you entered is positive and is odd.")
    else:
        # Additional condition to check if the number is negative
        if num < 0:
            print("The number you entered is negative.")
        else:
            print("The number you entered is not a valid integer.")

except ValueError as ve:
    print("Enter valid input: ", str(ve))
