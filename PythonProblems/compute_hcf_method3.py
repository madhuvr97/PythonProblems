def compute_hcf(x,y):
    while y:
        x, y = y, x % y
    return x

def get_positive_integer(prompt):
    try:
        value = int(input(prompt))
        if value < 0:
            print("Please enter a positive integer.")
        else:
            return value
    except ValueError:
        print("Invalid input. Please enter an integer.")

try:
    x = get_positive_integer("Enter the first number: ")
    y = get_positive_integer("Enter the second number: ")
    if x == 0 and y == 0:
        print("HCF of 0 and 0 is undefined.")
    else:
        hcf = compute_hcf(x,y)
        print(f"The hcf of {x} and {y} is {hcf}")
except Exception as exception:
    print("An unknown error occurred:", str(exception))