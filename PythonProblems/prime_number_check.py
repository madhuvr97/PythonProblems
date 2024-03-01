def is_prime(num):
    """
    Checks if a number is prime.

    Parameters:
    - num: An integer number to be checked for primality.

    Returns:
    - A string indicating whether the number is prime or not.
    """
    if num == 1:
        return "The number is not prime"
    elif num == 0:
        return "The number you entered is zero"
    elif num < 0:
        return "The number you entered is negative and there is no concept of negative prime numbers"
    else:
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                return "The number is not prime"

        return "The number is prime"


try:
    num = int(input("Enter a number: "))
    check_number = is_prime(num)
    print(check_number)

except ValueError as ve:
    print("Invalid input: ", str(ve))

except Exception as e:
    print("An unknown error occurred", str(e))
