def filter_numbers_divisible_by_13(input_list):
    """
    Filter numbers in the list that are divisible by 13.

    Args:
    - input_list (list): The list of numbers to filter.

    Returns:
    - list: A list containing numbers from input_list that are divisible by 13.
    """
    return list(filter(lambda x: x % 13 == 0, input_list))

try:
    # Prompt the user to enter a list of numbers
    input_string = input("Enter the list of numbers in the format [1, 2, 3]: ")

    # Evaluate the input string to convert it into a Python list
    my_list = eval(input_string)

    # Check if the list is empty
    if not my_list:
        print("This is an empty list. Please provide a list containing numbers.")
    else:
        divisible_by_13 = filter_numbers_divisible_by_13(my_list)

        # Check if there are numbers divisible by 13 in the list
        if not divisible_by_13:
            print("There are no numbers divisible by 13 in the list you provided.")
        else:
            print("Numbers divisible by 13:", divisible_by_13)

except ValueError as value_error:
    print("Invalid input: ", str(value_error))

except Exception as exception:
    print("An unknown error occurred:", str(exception))