def generate_fibonacci_series(limit):
    """
    Generate a Fibonacci series up to the given limit.

    Args:
    - limit (int): The number of Fibonacci numbers to generate.

    Returns:
    - list: A list containing the Fibonacci series up to the specified limit.
    """
    fibonacci_series = [0, 1]  # Base Fibonacci sequence

    if limit == 1:
        return [0]  # Return [0] for the first Fibonacci number
    elif limit == 2:
        return fibonacci_series  # Return the base Fibonacci sequence
    else:
        n1, n2 = 0, 1
        for _ in range(2, limit):
            n3 = n1 + n2
            n1, n2 = n2, n3
            fibonacci_series.append(n3)
        return fibonacci_series

# Interactive interface for user input
while True:
    try:
        limit = int(input("Enter the limit until which you want to print the Fibonacci series: "))
        if limit <= 0:
            print("Limit must be a positive integer.")
        else:
            print(generate_fibonacci_series(limit))
            break
    except ValueError as ve:
        print("Invalid input: ", str(ve))
    except Exception as e:
        print("An unknown error occurred", str(e))
