def is_palindrome(input_string):
    # Remove non-alphanumeric characters and convert to lowercase
    input_string = ''.join(char.lower() for char in input_string if char.isalnum())
    reverse_string = input_string[::-1]
    return input_string == reverse_string

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    if is_palindrome(input_string):
        print(f"The input string {input_string} is a palindrome")
    else:
        print(f"The input string {input_string} is not a palindrome")
