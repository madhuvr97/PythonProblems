def count_number_of_each_vowels(input_string):
    """
    Counts the number of occurrences of each vowel (a, e, i, o, u) in the given string.

    Args:
    - input_string (str): The input string to count vowels from.

    Returns:
    - dict: A dictionary containing the count of each vowel.
    """
    # Initialize a dictionary to store the count of each vowel
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Convert the input string to lowercase for case-insensitive counting
    input_string = input_string.lower().replace(" ","")

    # Iterate through each character in the string
    if input_string.isalpha():
        for char in input_string:
            # Check if the character is a vowel
            if char in vowel_count:
                # Increment the count of the vowel
                vowel_count[char] += 1
    else:
        return None

    return vowel_count

# Test the function
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    vowels_count = count_number_of_each_vowels(input_string)
    if vowels_count is None:
        print("You haven't entered any alphabetic characters...")
    else:
        print("Number of occurrences of each vowel:")
        for vowel, count in vowels_count.items():
            print(f"{vowel}: {count}")
