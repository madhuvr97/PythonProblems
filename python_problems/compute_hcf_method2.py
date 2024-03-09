def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def compute_hcf(x, y):
    hcf = 1
    smaller = min(x, y)
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf


try:
    print("Enter two positive integers to find their HCF.")
    x = get_positive_integer("Enter the first number: ")
    y = get_positive_integer("Enter the second number: ")

    if x == 0 and y == 0:
        print("HCF of 0 and 0 is undefined.")
    else:
        hcf = compute_hcf(x, y)
        print(f"HCF of {x} and {y} is {hcf}")

except KeyboardInterrupt:
    print("\nProgram terminated by user.")
except Exception as exception:
    print("An unknown error occurred:", str(exception))