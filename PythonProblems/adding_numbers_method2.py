def add_numbers(*args):
    result = sum(args)
    return result

try:
    numbers = input("Enter the list of numbers you want to add: ")
    numbers_list = eval(numbers)
    add_numbers_list = add_numbers(*numbers_list)
    print("Sum of the numbers:", add_numbers_list)
except NameError:
    print("NameError: Enter a valid input format (e.g., [1, 2, 3])")
except SyntaxError:
    print("SyntaxError: Invalid input format. Please use a valid list format.")
except Exception as e:
    print("An unknown error occurred:", str(e))
