def add_numbers(*args):
    result = sum(args)
    return result

numbers = input("enter the list of numbers you want to add seperated by a space: ")
numbers_list = list(map(int, numbers.split()))
add_2_numbers = add_numbers(*numbers_list)
print(add_2_numbers)