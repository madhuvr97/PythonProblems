try:
    # Take input from the user to determine the number of terms
    terms = int(input("How many terms? "))

    # Check if the input is non-negative
    if terms < 0:
        print("Please enter a non-negative number.")
    else:
        # Calculate the powers of 2 using a lambda function and map
        powers_of_two = list(map(lambda x: 2 ** x, range(terms)))

        # Display the total number of terms
        print("The total terms are:", terms)

        # Display each power of 2 along with its exponent
        for i in range(terms):
            print("2^", i, "=", powers_of_two[i])

except ValueError as value_error:
    # Handle the case where the input is not an integer
    print("Invalid input: ", str(value_error))

except Exception as exception:
    # Handle any other unexpected errors
    print("An unknown error occurred:", str(exception))
