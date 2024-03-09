def compute_hcf(x,y):
    while y:
        x, y = y, x % y
    return x

def get_positive_integer(prompt):
        value = int(input(prompt))
        return value

try:
    x = get_positive_integer("Enter the first number: ")
    if x < 0:
        raise ValueError("Please enter a positive integer...")
    y = get_positive_integer("Enter the second number: ")
    if y < 0:
        raise ValueError("Please enter a positive integer...")
    if x == 0 and y == 0:
        print("HCF of 0 and 0 is undefined.")
    else:
        hcf = compute_hcf(x,y)
        print(f"The hcf of {x} and {y} is {hcf}")
except ValueError as ve:
    print("Invalid input: ", str(ve))
except Exception as e:
    print("An unknown error occurred: ", str(e))