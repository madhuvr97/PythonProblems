def sort_words_in_string(input_string):
    """
    Sorts the words in the input string in alphabetical order and prints them.

    Args:
    - input_string (str): The input string containing words to be sorted.

    Returns:
    - None
    """
    if not input_string.strip():
        print("Input string is empty or contains only whitespace characters.")
        return

    words = [word.lower() for word in input_string.split()]
    words.sort()

    print("The sorted words are:")
    for word in words:
        print(word)


if __name__ == "__main__":
    input_string = input("Enter the string to be sorted: ")
    sort_words_in_string(input_string)
