def compute_factorial(num):
    """
    Computes the factorial of a non-negative integer.

    Parameters:
    - num: An integer for which factorial needs to be computed.

    Returns:
    - The factorial of the input number.
    - If num is 0, returns 1 (by definition).
    - If num is negative, returns None.
    """
    if num == 0:
        return 1  # Factorial of 0 is 1
    elif num < 0:
        return None  # Factorial of negative numbers is undefined
    else:
        factorial_result = 1  # Initialize the factorial result
        for i in range(1, num + 1):
            factorial_result *= i
        return factorial_result

try:
    num = int(input("Enter a number: "))
    factorial = compute_factorial(num)
    if num < 0:
        print("Factorial of negative numbers is undefined")
    else:
        print(f"The factorial of {num} is {factorial}")

except ValueError as ve:
    print("Invalid input: ", str(ve))
except Exception as e:
    print("An unknown error occurred", str(e))
