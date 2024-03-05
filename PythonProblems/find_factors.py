def find_factors(num):
    """
    Find the factors of a given integer.

    Parameters:
    - num: The integer for which factors are to be found.

    Returns:
    - A list of factors of the input number.
    - If the input number is 0, returns an empty list.
    """
    factors = []
    if num == 0:
        print("Factors of 0 are all integers")
    elif num > 0:
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
    else:
        num = abs(num)
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        factors = [-factor for factor in factors]
    return factors if num != 0 else []

def get_integer_input(prompt):
    value = int(input(prompt))
    return value

def main():
    try:
        num = get_integer_input("Enter an integer: ")
        factors = find_factors(num)
        if factors:
            print(f"The factors of {num} are {factors}")
    except ValueError as ve:
        print("Invalid input: ", str(ve))
    except Exception as e:
        print("An unknown error occurred: ", str(e))

if __name__ == '__main__':
    main()
