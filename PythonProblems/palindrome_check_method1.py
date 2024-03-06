input_string = input("Enter the string: ")
reverse_string = input_string[::-1]
if input_string == reverse_string:
    print(f"The input string {input_string} is a palindrome")
else:
    print(f"The input string {input_string} is not a palindrome")