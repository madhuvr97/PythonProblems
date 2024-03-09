def compute_factorial(num):
    """
    Computes the factorial of a non-negative integer using recursion.

    Parameters:
    - num: An integer for which factorial needs to be computed.

    Returns:
    - The factorial of the input number.
    - If num is 0, returns 1 (by definition).
    - If num is negative, returns None.
    """
    if num < 0:
        return None  # Factorial of negative numbers is undefined
    elif num == 0:
        return 1  # Factorial of 0 is 1
    else:
        # Recursively compute factorial
        return num * compute_factorial(num - 1)

try:
    num = int(input("Enter a non-negative integer: "))
    factorial_result = compute_factorial(num)
    if factorial_result is None:
        print("Factorial of negative numbers is undefined")
    else:
        print(f"The factorial of {num} is {factorial_result}")
except ValueError as ve:
    print("Invalid input: ", str(ve))
except Exception as e:
    print("An unknown error occurred", str(e))
