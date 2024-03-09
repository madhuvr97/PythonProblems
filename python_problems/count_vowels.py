def count_vowels(input_string):
    """
    Counts the number of vowels (a, e, i, o, u) in the given string.

    Args:
    - input_string (str): The input string to count vowels from.

    Returns:
    - int: The number of vowels in the input string.
    """
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Convert the input string to lowercase for case-insensitive counting
    input_string = input_string.lower()

    # Initialize a counter for vowels
    vowel_count = 0

    # Iterate through each character in the string
    if input_string.isalpha():
        for char in input_string:
            # Check if the character is a vowel
            if char in vowels:
                # Increment the vowel count
                vowel_count += 1
    else:
        return None

    return vowel_count

# Test the function
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    vowels_count = count_vowels(input_string)
    if vowels_count is None:
        print("You haven't entered any alphabetic characters...")
    else:
        print(f"Number of vowels in the string: {vowels_count}")

