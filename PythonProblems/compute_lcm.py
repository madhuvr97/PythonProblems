def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

def compute_lcm(x,y):
    lcm = (x * y) // compute_hcf(x,y)
    return lcm

try:
    x = int(input("Enter the first number: "))
    if x < 0:
        raise ValueError("Please enter a positive integer...")
    y = int(input("Enter the second number: "))
    if y < 0:
        raise ValueError("Please enter a positive integer...")
    elif x == 0 and y == 0:
        print("LCM of 0 and 0 is undefined.")
    else:
        lcm = compute_lcm(x,y)
        print(f"lcm of {x} and {y} is {lcm}")
except ValueError as ve:
    print("Invalid input: ", str(ve))
except Exception as e:
    print("An unknown error occurred: ", str(e))