def generate_primes(limit):
    """
    Generates prime numbers up to the given limit.

    Parameters:
    - limit: An integer specifying the upper limit until which prime numbers should be generated.

    Returns:
    - A list containing prime numbers up to the specified limit.
    """
    if limit < 2:
        return []  # No prime numbers less than 2

    prime_list = [2]  # Initialize the list with the first prime number, 2

    for num in range(3, limit + 1):
        for divisor in range(3, num):
            if num % divisor == 0:
                break
        else:
            prime_list.append(num)
    return prime_list


def main():
    try:
        limit = int(input("Enter the limit until which you want the prime numbers to be printed: "))
        if limit < 2:
            print("No prime numbers in the specified range.")
        else:
            primes = generate_primes(limit)
            print("Prime numbers up to", limit, "are:", primes)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the limit.")


if __name__ == "__main__":
    main()
