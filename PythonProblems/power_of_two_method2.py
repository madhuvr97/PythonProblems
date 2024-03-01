def calculate_powers_of_two(terms):
    """
    Calculate the powers of 2 up to the given number of terms.

    Args:
    - terms (int): The number of terms to calculate.

    Returns:
    - list: A list containing the powers of 2 up to the specified number of terms.
    """
    return [2 ** x for x in range(terms)]

try:
    terms = int(input("How many terms? "))

    if terms < 0:
        print("Please enter a positive number.")
    else:
        powers_of_two = calculate_powers_of_two(terms)
        print("The total terms are:", terms)
        for i in range(terms):
            print("2^", i, "=", powers_of_two[i])

except ValueError as value_error:
    print("Invalid input: ", str(value_error))
except Exception as exception:
    print("An unknown error occurred:", str(exception))
