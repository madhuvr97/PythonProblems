def compute_hcf(x, y):
    hcf = 1
    smaller = min(x, y)
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf

try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    if x <= 0 or y <= 0:
        print("Please enter positive integers.")
    else:
        hcf = compute_hcf(x, y)
        print(f"HCF of {x} and {y} is {hcf}")
except ValueError as value_error:
    print("Invalid input: ", str(value_error))
except Exception as exception:
    print("An unknown error occurred:", str(exception))
