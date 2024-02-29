def find_largest_number(*numbers):
    """
    Finds the largest number in a given list of numbers.

    Parameters:
    - numbers: A list of numbers.

    Returns:
    - The largest number in the list.
    """
    if not numbers:
        raise ValueError("No numbers provided")

    return max(numbers)


try:
    numbers = eval(input("Enter the list of numbers in the format [1, 2, 3]: "))
    largest_number = find_largest_number(*numbers)
    print("The largest number in the list is:", largest_number)
except NameError:
    print("NameError: Enter a valid input format (e.g., [1, 2, 3])")
except SyntaxError:
    print("SyntaxError: Invalid input format. Please use a valid list format.")
except ValueError as ve:
    print("ValueError:", str(ve))
except Exception as e:
    print("An unknown error occurred:", str(e))