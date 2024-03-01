def sum_of_natural_numbers(limit):
    """
    Calculate the sum of the first n natural numbers.

    Args:
    - limit (int): The limit until which to calculate the sum.

    Returns:
    - int: The sum of the first n natural numbers.
    """
    return int((limit * (limit + 1)) / 2)

while True:
    try:
        limit = int(input("Enter the limit until which you want to calculate the sum of natural numbers: "))
        if limit <= 0:
            print("Please enter a positive integer.")
        else:
            print(f"The sum of the first {limit} natural numbers is {sum_of_natural_numbers(limit)}.")
            break
    except ValueError as value_error:
        print("Invalid input: ", str(value_error))
    except Exception as exception:
        print("An unknown error occurred:", str(exception))
